# MyFurdi App Mock

MyFurdi（女性専用AIパーソナルトレーニングジム FURDI 会員向けアプリ）のモックアプリです。

## 🎨 特徴

- **iOSネイティブデザイン**: Apple Human Interface Guidelines (HIG) に準拠
- **FURDIブランド**: ピンク (#FF69B4) を基調とした女性向けデザイン
- **レスポンシブ**: iPhone 14 Pro サイズ (393px) に最適化
- **フルインタラクティブ**: すべての画面を切り替えて閲覧可能

## 📱 実装画面

### 1. ホーム画面
- 時間帯別の挨拶
- 今日のチャレンジカード
- 来店サマリー（連続日数、週間進捗）
- 混雑状況クイックビュー
- 健康データサマリー（タブ切替）
- クイックアクション
- 週次サマリー

### 2. レポート画面
- 運動記録（グラフ表示）
- 体組成データ（推移グラフ）
- 来館履歴（カレンダービュー）

### 3. 入館証画面
- QRコード表示
- 会員情報
- 店舗選択
- 利用案内

### 4. リワード画面
- 今日のチャレンジ（日次）
- 週間・月間チャレンジ
- マイバッジコレクション
- 実績・ランクシステム

### 5. メニュー画面
- ユーザープロフィール
- 各種設定
- コンテンツへのアクセス
- ログアウト

## 🚀 セットアップ

### 必要な環境
- Node.js 18.x 以上
- npm または yarn

### インストール

```bash
# 依存関係のインストール
npm install
```

### 開発サーバーの起動

```bash
# 開発サーバー起動（ポート3000）
npm run dev
```

ブラウザで http://localhost:3000 を開くと、モックアプリが表示されます。

### ビルド

```bash
# プロダクションビルド
npm run build

# ビルドのプレビュー
npm run preview
```

## 🛠 技術スタック

- **React 18**: UIライブラリ
- **TypeScript**: 型安全性
- **Vite**: 高速ビルドツール
- **Tailwind CSS**: ユーティリティファーストCSS
- **Lucide React**: アイコンライブラリ

## 📐 デザイン仕様

### カラーパレット

```css
/* FURDIブランドカラー */
--furdi-pink: #FF69B4
--furdi-pink-light: #FFE4E1
--furdi-pink-dark: #FF1493

/* iOSシステムカラー */
--ios-gray: #F5F5F5
--ios-text: #1C1C1E
--ios-text-secondary: #3A3A3C
--ios-separator: #E5E5E7
```

### タイポグラフィ

- **フォント**: -apple-system, BlinkMacSystemFont, SF Pro
- **見出し**: 20-24px, Bold (700)
- **本文**: 14-16px, Regular (400)
- **キャプション**: 12px, Regular (400)

### レイアウト

- **画面幅**: 393px (iPhone 14 Pro)
- **カードマージン**: 16px
- **カード角丸**: 10-12px
- **ボタン高さ**: 44px (最小タッチターゲット)

## 🎯 iOS ネイティブ要素

### 実装されたiOS特有のデザイン

- **Safe Area**: ノッチ対応の上部スペース
- **タブバー**: iOS標準のボトムタブナビゲーション
- **カードデザイン**: iOS標準のシャドウとエレベーション
- **アクティブステート**: タップ時のスケールアニメーション (0.95)
- **プログレスバー**: iOS標準の角丸プログレスバー
- **セグメントコントロール**: タブ切替UI

### インタラクション

- **タップフィードバック**: `active:scale-95` によるボタン縮小
- **スムーズトランジション**: 300ms の遷移アニメーション
- **スクロール**: `-webkit-overflow-scrolling: touch` による慣性スクロール

## 📝 設計ドキュメント

詳細な設計仕様は以下のドキュメントを参照してください：

- `base-documents/MyFurdi_設計概要.md`
- `base-documents/MyFurdi_画面機能分析.md`
- `base-documents/MyFurdi_アプリ設計概要とデザインポリシー.md`
- `base-documents/MyFurdi_画面一覧と機能詳細.md`

## 🔄 次のステップ

このモックアプリをベースに、以下の実装に進むことができます：

1. **Flutterへの移植**: React コンポーネントを Flutter Widget に変換
2. **API連携**: バックエンドAPIとの接続
3. **状態管理**: Riverpod/Provider の導入
4. **認証**: Firebase Authentication の実装
5. **データ永続化**: ローカルDB（SQLite/Hive）の実装

## 📄 ライセンス

© 2024 FURDI. All rights reserved.
