# MyFurdi - IDENSIL PDF連携仕様書

## 概要

IDENSIL（イデンシル）DNA検査サービスと連携し、ユーザーの検査結果PDFをMyFurdiアプリ内でダウンロード・閲覧できる機能の技術仕様書です。

**作成日**: 2025年10月23日
**バージョン**: 1.0.0
**ステータス**: 設計段階（連携方式確定待ち）

---

## IDENSIL サービス概要

### サービス提供元
- **サービス名**: IDENSIL（イデンシル）
- **提供会社**: 株式会社グリスタ
- **公式サイト**: https://idensil.jp/
- **対象**: 業務用高精度遺伝子分析サービス

### 検査内容
- **分析項目数**: 32個の遺伝子型
- **分析対象**: フィットネス・スポーツに特化
- **分析機器**: MassARRAY®（病院の臨床検査機器）
- **監修**: 順天堂大学スポーツ遺伝学・行動遺伝学研究者

### 検査結果提供形式
- **フォーマット**: PDF
- **想定ページ数**: 32ページ
- **想定ファイルサイズ**: 3-5MB
- **内容**:
  - 総合評価（レーダーチャート等）
  - 32項目の遺伝子型詳細
  - 各項目の科学的根拠
  - トレーニング・栄養推奨事項

---

## 連携方式の検討

### 方式A: IDENSIL API直接連携

#### 概要
IDENSILのサーバーから、MyFurdiアプリが直接PDFを取得する方式。

#### データフロー
```
[IDENSIL Server]
    ↓ API Request (ユーザーID紐付け)
[MyFurdi Backend API]
    ↓ PDF Stream
[MyFurdi App]
    ↓ Download/View
[ユーザーのデバイス]
```

#### メリット
- ✅ リアルタイムで最新データを取得可能
- ✅ ストレージコスト不要（PDF保存不要）
- ✅ データ同期の手間なし
- ✅ IDENSILでPDFが更新された場合、即座に反映

#### デメリット
- ❌ IDENSILのAPIダウン時に取得不可
- ❌ IDENSIL側のAPI仕様に依存
- ❌ 認証・セキュリティ管理が複雑
- ❌ 通信コストが発生（毎回ダウンロード）

#### 技術要件
- IDENSIL API仕様書
- OAuth 2.0またはAPI Key認証
- ユーザーID紐付けルール（MyFurdi ⇔ IDENSIL）
- PDFストリーミング対応

#### API設計例
```typescript
// MyFurdi Backend → IDENSIL
GET https://api.idensil.jp/v1/reports/{idensilUserId}/pdf
Headers:
  Authorization: Bearer {API_KEY}
  X-Client-ID: {FURDI_CLIENT_ID}

Response: PDF Binary Stream
```

---

### 方式B: 新PIX経由のPDF保持

#### 概要
IDENSILから受け取ったPDFを新PIXサーバーに保存し、MyFurdiアプリは新PIXから取得する方式。

#### データフロー
```
[IDENSIL Server]
    ↓ PDF提供（初回または更新時）
[新PIX Server - PDF Storage]
    ↓ API Request
[MyFurdi Backend API]
    ↓ PDF Stream
[MyFurdi App]
    ↓ Download/View
[ユーザーのデバイス]
```

#### メリット
- ✅ IDENSIL APIに依存しない（オフライン対応可能）
- ✅ ダウンロード速度が速い（自社サーバーから配信）
- ✅ PDF加工・最適化が可能
- ✅ アクセスログ・分析が容易

#### デメリット
- ❌ ストレージコスト発生
- ❌ PDF同期処理が必要
- ❌ データ二重管理のリスク
- ❌ 初期移行作業が必要

#### 技術要件
- 新PIXサーバーのストレージ容量
- PDF同期バッチ処理（定期 or イベント駆動）
- ユーザーID紐付けDB
- ファイル命名規則

#### API設計例
```typescript
// MyFurdi Backend → 新PIX
GET https://pix-api.furdi.jp/v1/dna/reports/{userId}/pdf
Headers:
  Authorization: Bearer {FURDI_AUTH_TOKEN}

Response: PDF Binary Stream
```

---

## 推奨方式の選定基準

| 評価項目 | 方式A (IDENSIL直接) | 方式B (新PIX経由) |
|---------|---------------------|-------------------|
| **初期開発コスト** | 高（API連携複雑） | 中（ストレージ構築） |
| **運用コスト** | 低（ストレージ不要） | 高（ストレージ費用） |
| **可用性** | IDENSIL依存 | 高（自社管理） |
| **レスポンス速度** | 中（外部API） | 高（自社サーバー） |
| **データ鮮度** | 常に最新 | 同期タイミング依存 |
| **拡張性** | IDENSIL仕様依存 | 高（自由度大） |
| **セキュリティ** | IDENSIL側管理 | 自社管理 |

### 推奨
**フェーズ1（MVP）**: 方式Aまたは方式Bのいずれかを確定
**フェーズ2（安定運用）**: 方式B（新PIX経由）を推奨

**理由**:
- 可用性とレスポンス速度の向上
- 将来的なデータ分析・加工の柔軟性
- ユーザー体験の向上（高速ダウンロード）

---

## ユーザーID紐付け仕様

### データモデル
```typescript
interface DNATestUser {
  userId: string;              // MyFurdi ユーザーID
  idensilUserId: string;       // IDENSIL ユーザーID
  testDate: string;            // 検査実施日 (YYYY-MM-DD)
  reportStatus: 'pending' | 'ready' | 'downloaded';
  pdfUrl?: string;             // 方式Bの場合のPDF URL
  lastSyncedAt?: string;       // 最終同期日時
  createdAt: string;
  updatedAt: string;
}
```

### DB テーブル設計（例）
```sql
CREATE TABLE dna_test_users (
  user_id VARCHAR(255) PRIMARY KEY,
  idensil_user_id VARCHAR(255) UNIQUE NOT NULL,
  test_date DATE NOT NULL,
  report_status ENUM('pending', 'ready', 'downloaded') DEFAULT 'pending',
  pdf_url TEXT,
  last_synced_at TIMESTAMP,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  INDEX idx_idensil_user_id (idensil_user_id),
  INDEX idx_test_date (test_date)
);
```

---

## API仕様

### 1. DNA検査状態確認
```
GET /api/v1/dna/status/:userId
```

**レスポンス**:
```json
{
  "hasTest": true,
  "testDate": "2024-08-15",
  "reportStatus": "ready",
  "pdfAvailable": true,
  "lastSyncedAt": "2024-10-23T10:30:00Z"
}
```

---

### 2. PDFダウンロード

#### 方式A: IDENSIL API経由
```
GET /api/v1/dna/pdf/:userId
```

**処理フロー**:
1. MyFurdi Backend: ユーザーIDからIDENSIL UserIDを取得
2. MyFurdi Backend → IDENSIL API: PDF取得リクエスト
3. IDENSIL API → MyFurdi Backend: PDFストリーミング
4. MyFurdi Backend → App: PDFストリーミング

**レスポンス**:
- Content-Type: `application/pdf`
- Content-Disposition: `attachment; filename="IDENSIL_DNA_Report_12345_20240815.pdf"`

#### 方式B: 新PIX経由
```
GET /api/v1/dna/pdf/:userId
```

**処理フロー**:
1. MyFurdi Backend: ユーザーIDからPDF URLを取得
2. MyFurdi Backend → 新PIX: PDF取得リクエスト
3. 新PIX → MyFurdi Backend: PDFストリーミング
4. MyFurdi Backend → App: PDFストリーミング

**レスポンス**:
- Content-Type: `application/pdf`
- Content-Disposition: `attachment; filename="IDENSIL_DNA_Report_12345_20240815.pdf"`

---

### 3. IDENSIL連携設定

```
POST /api/v1/dna/connect
```

**リクエスト**:
```json
{
  "userId": "12345",
  "idensilUserId": "IDEN987654",
  "authToken": "optional_auth_token"
}
```

**レスポンス**:
```json
{
  "success": true,
  "message": "IDENSIL連携が完了しました",
  "testDate": "2024-08-15"
}
```

---

## ファイル命名規則

### PDFファイル名形式
```
IDENSIL_DNA_Report_{userId}_{testDate}.pdf
```

**例**:
```
IDENSIL_DNA_Report_12345_20240815.pdf
```

### ストレージパス（方式Bの場合）
```
/storage/dna-reports/{year}/{month}/{userId}/
  └── IDENSIL_DNA_Report_{userId}_{testDate}.pdf
```

**例**:
```
/storage/dna-reports/2024/08/12345/
  └── IDENSIL_DNA_Report_12345_20240815.pdf
```

---

## セキュリティ要件

### 認証・認可
- ✅ ユーザー本人のみがPDFダウンロード可能
- ✅ JWT認証必須
- ✅ ダウンロードログの記録

### データ保護
- ✅ PDF転送時のHTTPS必須
- ✅ ストレージ暗号化（方式Bの場合）
- ✅ アクセス権限管理（IAM）

### プライバシー
- ✅ GDPR / 個人情報保護法準拠
- ✅ 同意取得の記録
- ✅ データ削除権の保証

---

## アプリ側実装（Flutter）

### PDFダウンロード処理
```dart
Future<void> downloadDNAPdf(String userId) async {
  try {
    // 1. APIからPDFを取得
    final response = await http.get(
      Uri.parse('https://api.furdi.jp/v1/dna/pdf/$userId'),
      headers: {
        'Authorization': 'Bearer $authToken',
      },
    );

    if (response.statusCode == 200) {
      // 2. ファイル名を取得
      final contentDisposition = response.headers['content-disposition'];
      final fileName = _extractFileName(contentDisposition)
        ?? 'IDENSIL_DNA_Report_$userId.pdf';

      // 3. ローカルに保存
      final directory = await getApplicationDocumentsDirectory();
      final file = File('${directory.path}/$fileName');
      await file.writeAsBytes(response.bodyBytes);

      // 4. 保存完了通知
      showToast('PDFをダウンロードしました');

      // 5. PDFビューアーで開く（オプション）
      await openPdf(file.path);
    } else {
      throw Exception('PDF取得失敗: ${response.statusCode}');
    }
  } catch (e) {
    showError('PDFのダウンロードに失敗しました: $e');
  }
}
```

### PDFビューアー
推奨パッケージ:
- **flutter_pdfview**: ネイティブPDFビューアー
- **syncfusion_flutter_pdfviewer**: 高機能PDFビューアー

---

## エラーハンドリング

### エラーケース

| エラーコード | 原因 | 対処法 |
|------------|------|--------|
| `404` | PDF未登録 | 「検査結果が未登録です」表示 |
| `403` | 認証エラー | 再ログイン促進 |
| `500` | サーバーエラー | 「しばらくしてから再度お試しください」 |
| `503` | IDENSIL APIダウン | 「現在サービスが利用できません」 |

### ユーザー向けメッセージ例
```typescript
const errorMessages = {
  404: 'DNA検査結果がまだ登録されていません。検査完了後、再度お試しください。',
  403: 'ログイン情報が無効です。再度ログインしてください。',
  500: 'サーバーエラーが発生しました。しばらくしてから再度お試しください。',
  503: '現在サービスが利用できません。時間をおいてから再度お試しください。',
  network: 'ネットワーク接続を確認してください。',
};
```

---

## 運用・監視

### モニタリング項目
- PDF ダウンロード成功率
- ダウンロード応答時間（P50, P95, P99）
- エラー発生率（エラーコード別）
- ストレージ使用量（方式Bの場合）
- IDENSIL API レスポンス時間

### アラート設定
- ダウンロード成功率 < 95%
- 平均応答時間 > 5秒
- 5xx エラー率 > 5%

---

## テストケース

### 1. 正常系
- ✅ 有効なユーザーIDでPDFダウンロード成功
- ✅ ダウンロードしたPDFが正しく開ける
- ✅ ファイル名が正しい形式

### 2. 異常系
- ✅ 未登録ユーザーID → 404エラー
- ✅ 認証トークン無効 → 403エラー
- ✅ ネットワークエラー → 適切なエラーメッセージ
- ✅ PDF破損時の検出とエラー処理

### 3. パフォーマンス
- ✅ 3MB PDFのダウンロード時間 < 5秒
- ✅ 同時100リクエスト処理可能

---

## 今後の課題・検討事項

### 確定待ち項目
- [ ] IDENSIL側のAPI仕様確認
- [ ] 新PIXサーバーの仕様確定
- [ ] ユーザーID紐付けルールの確定
- [ ] 連携方式（A or B）の最終決定

### 将来的な拡張
- [ ] PDF自動更新・通知機能
- [ ] オフライン閲覧機能（キャッシュ）
- [ ] PDF内検索機能
- [ ] 複数言語対応（英語レポート等）
- [ ] レポート比較機能（過去との比較）

---

## 参考資料

### 外部リンク
- [IDENSIL公式サイト](https://idensil.jp/)
- [株式会社グリスタ](https://www.glista.co.jp/)

### 内部ドキュメント
- `MyFurdi_DNA検査機能仕様.md` - DNA検査結果表示機能の全体仕様
- 新PIXシステム仕様書（作成予定）
- IDENSIL API仕様書（提供後に追記予定）

---

## 更新履歴

| 日付 | バージョン | 更新内容 |
|-----|----------|---------|
| 2025-10-23 | 1.0.0 | 初版作成。方式A・B の技術仕様策定 |
