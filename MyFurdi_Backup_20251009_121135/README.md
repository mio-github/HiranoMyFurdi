# MyFurdi アプリ開発資料パッケージ

## 📦 パッケージ概要

**バージョン**: 1.1.0
**作成日**: 2025年10月2日
**対象**: 開発チーム・デザインチーム

このパッケージには、MyFurdi（FURDI会員向けフィットネスサポートアプリ）の開発に必要な全ドキュメント、ワイヤーフレーム、モックアプリが含まれています。

---

## 📁 ファイル構成

### 圧縮ファイル
- **`MyFurdi_Deliverables_20251002.zip`** (281KB)

### 展開後のフォルダ構成

```
MyFurdi/
├── base-documents/              # 設計ドキュメント
│   ├── MyFurdi_設計概要.md
│   ├── MyFurdi_アプリ設計概要とデザインポリシー.md
│   ├── MyFurdi_画面一覧と機能詳細.md
│   ├── MyFurdi_画面機能分析.md (chocoZAP参考)
│   └── MyFurdi_DNA検査機能仕様.md
│
├── wireframes/                   # ワイヤーフレーム・デザイン
│   ├── 01_home_screen.svg
│   ├── 02_report_screen.svg
│   ├── 03_qrcode_screen.svg
│   ├── 04_reward_screen.svg
│   ├── 05_menu_screen.svg
│   ├── 06_dna_result_screen.svg
│   ├── screen_transition_diagram.svg
│   ├── design_tokens.json
│   ├── figma_components.json
│   ├── figma_import_guide.md
│   └── wireframe_specifications.md
│
└── app-mock/                     # モックアプリ
    ├── src/
    │   ├── components/
    │   │   ├── HomeScreen.tsx
    │   │   ├── ReportScreen.tsx
    │   │   ├── QRCodeScreen.tsx
    │   │   ├── RewardScreen.tsx
    │   │   ├── MenuScreen.tsx
    │   │   ├── DNAResultScreen.tsx
    │   │   └── TabBar.tsx
    │   ├── App.tsx
    │   └── index.css
    ├── package.json
    └── README.md
```

---

## 🚀 クイックスタート

### 1. ドキュメントの確認

まず `base-documents/` フォルダ内のドキュメントを確認してください：

1. **MyFurdi_アプリ設計概要とデザインポリシー.md**
   - アプリ全体のデザイン方針
   - カラーパレット、タイポグラフィ、レイアウト
   - Flutter開発のベストプラクティス

2. **MyFurdi_画面一覧と機能詳細.md**
   - 全画面の詳細仕様（19画面）
   - 画面遷移図
   - 開発リソース情報

3. **MyFurdi_DNA検査機能仕様.md**
   - DNA検査結果表示機能の詳細
   - 外部サービス連携仕様

### 2. ワイヤーフレームの確認

`wireframes/` フォルダ内のSVGファイルを開いて、各画面のレイアウトを確認：

- **全6画面のワイヤーフレーム**: iPhone 14 Pro サイズ (393×852px)
- **画面遷移図**: 全画面の遷移関係を可視化

#### Figmaへのインポート

1. `figma_import_guide.md` を参照
2. SVGファイルをFigmaにインポート
3. `design_tokens.json` を使ってデザインシステムを構築
4. `figma_components.json` でコンポーネント仕様を確認

### 3. モックアプリの起動

インタラクティブなReactモックアプリを起動して、実際の動作を確認できます。

```bash
# モックアプリフォルダへ移動
cd app-mock

# 依存関係をインストール
npm install

# 開発サーバー起動
npm run dev
```

ブラウザで http://localhost:5173 にアクセス

**実装済み機能**:
- ✅ タブバーによる6画面切り替え
- ✅ メニューからDNA検査画面への遷移
- ✅ iPhoneフレームシミュレーション
- ✅ iOS風デザイン（フラットデザイン、カード型UI）

---

## 📱 実装済み画面

### メイン画面（タブバー）
1. **ホーム画面** - ダッシュボード、チャレンジ、混雑状況
2. **レポート画面** - 運動記録、体組成データ、来館履歴
3. **入館証画面** - QRコード表示
4. **リワード画面** - バッジ、チャレンジ、実績
5. **メニュー画面** - プロフィール、設定、各種情報

### サブ画面
6. **DNA検査結果画面** (NEW)
   - 総合評価タブ（レーダーチャート）
   - 筋肉タイプタブ
   - 代謝タブ
   - 怪我リスクタブ
   - 詳細データタブ

---

## 🎨 デザイン仕様

### カラーパレット

| 用途 | カラー | コード |
|-----|--------|--------|
| **Primary** | FURDI Pink | `#FF69B4` |
| **Primary Light** | FURDI Pink Light | `#FFE4E1` |
| **Primary Dark** | FURDI Pink Dark | `#FF1493` |
| **Neutral** | iOS Gray 50 | `#F5F5F5` |
| **Text Primary** | iOS Text | `#1C1C1E` |
| **Text Secondary** | iOS Text Secondary | `#3A3A3C` |
| **Success** | Green | `#4CAF50` |
| **Info** | Blue | `#2196F3` |

### タイポグラフィ

- **フォント**: SF Pro Display / SF Pro Text (iOS標準)
- **見出し Large**: 24px Bold
- **見出し Medium**: 18px Bold
- **本文 Large**: 16px Regular
- **本文 Medium**: 14px Regular
- **本文 Small**: 12px Regular
- **キャプション**: 11px Regular

### レイアウトグリッド

- **カラム数**: 12
- **ガター幅**: 8px
- **画面マージン**: 左右16px
- **セクション間ギャップ**: 15px

---

## 🔧 技術スタック

### モックアプリ（プロトタイピング）
- **React** 18.3
- **TypeScript** 5.5
- **Vite** 5.4
- **Tailwind CSS** 3.4
- **Lucide React** (アイコン)

### 本番実装推奨
- **Framework**: Flutter 3.x
- **State Management**: Riverpod / Provider
- **API**: REST API / GraphQL
- **Database**: Firebase / Supabase
- **Analytics**: Firebase Analytics

---

## 📊 開発フェーズ

### Phase 1（初期リリース）
- ログイン・認証
- ホーム画面（基本機能）
- レポート画面
- 入館証画面（QRコード）
- リワード画面（基本機能）
- メニュー画面
- 混雑状況確認
- お知らせ・FAQ
- プッシュ通知

### Phase 2（拡張機能）
- ✅ DNA検査結果画面（実装完了）
- リワード詳細（ランクシステム）
- 通知センター高度化
- データエクスポート

### Phase 3（将来構想）
- AIチャットボット
- ウェアラブル連携
- コミュニティ機能

---

## 🔐 外部サービス連携

### 既存連携
- **PIXFORMANCE** - AIマシン連携
- **TANITA** - 体組成計連携
- **SECOM** - 入退館管理
- **YouTube** - 動画トレーニング

### 新規連携（Phase 2）
- **GeneQuest / MYCODE / ジーンライフ** - DNA検査サービス
- **Apple Health** - ヘルスデータ連携（iOS）
- **Google Fit** - フィットネスデータ連携（Android）

---

## 📝 開発者向けドキュメント

### ワイヤーフレーム仕様書
`wireframes/wireframe_specifications.md` に以下が含まれます：

- 各画面の詳細仕様
- レイアウト構造（サイズ、マージン、パディング）
- **Flutter実装コード例**
- コンポーネント仕様
- アクセシビリティ対応

### デザイントークン
`wireframes/design_tokens.json` - Figma/開発で使用可能な形式：

- カラーパレット
- タイポグラフィ
- スペーシング
- ボーダー半径
- シャドウ
- コンポーネント定義

### Figmaコンポーネント
`wireframes/figma_components.json` - 全コンポーネント仕様：

- ナビゲーション（TabBar, StatusBar, Header）
- カード（BasicCard, GradientCard, ChallengeCard）
- ボタン（Primary, Secondary, IconButton）
- データ表示（BarChart, RadarChart, QRCode）

---

## ✅ チェックリスト

### デザインレビュー
- [ ] 全ドキュメントを確認
- [ ] ワイヤーフレームSVGを確認
- [ ] モックアプリで動作確認
- [ ] FigmaでUIコンポーネントを作成
- [ ] iOSデザインガイドライン準拠を確認

### 開発準備
- [ ] Flutter環境セットアップ
- [ ] デザイントークンをFlutter Themeに変換
- [ ] 外部API仕様書を確認
- [ ] Firebase/Supabaseプロジェクト作成
- [ ] CI/CDパイプライン設定

---

## 📞 サポート・お問い合わせ

### ドキュメントに関する質問
- 設計・仕様: `MyFurdi_画面一覧と機能詳細.md` を参照
- デザイン: `MyFurdi_アプリ設計概要とデザインポリシー.md` を参照
- DNA機能: `MyFurdi_DNA検査機能仕様.md` を参照

### 技術的な質問
- モックアプリ: `app-mock/README.md` を参照
- ワイヤーフレーム: `wireframes/wireframe_specifications.md` を参照
- Figmaインポート: `wireframes/figma_import_guide.md` を参照

---

## 📄 ライセンス・利用規約

このパッケージに含まれるすべての資料は、FURDI社の内部開発用途に限定されます。外部への共有・配布は禁止されています。

---

## 🔄 更新履歴

| 日付 | バージョン | 更新内容 |
|-----|----------|---------|
| 2024-XX-XX | 1.0.0 | 初版作成 |
| 2025-10-02 | 1.1.0 | DNA検査結果画面追加、全6画面のワイヤーフレーム・モックアプリ完成 |

---

**Happy Coding! 💪🏋️‍♀️**
