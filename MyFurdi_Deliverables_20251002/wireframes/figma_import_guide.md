# MyFurdi Figma インポートガイド

## 概要
このフォルダのワイヤーフレームSVGファイルをFigmaにインポートして、デザインを開始するためのガイドです。

## ファイル一覧

### ワイヤーフレームSVG（全画面）
- `01_home_screen.svg` - ホーム画面
- `02_report_screen.svg` - レポート画面
- `03_qrcode_screen.svg` - 入館証画面
- `04_reward_screen.svg` - リワード画面
- `05_menu_screen.svg` - メニュー画面
- `screen_transition_diagram.svg` - 画面遷移図

### デザインシステムファイル
- `design_tokens.json` - カラー、タイポグラフィ、スペーシング定義
- `figma_components.json` - コンポーネント仕様

---

## Figmaへのインポート手順

### Step 1: SVGファイルのインポート

1. **新規Figmaファイルを作成**
   - Figmaを開き、新しいデザインファイルを作成
   - ファイル名: "MyFurdi App Wireframes"

2. **各SVGをインポート**
   ```
   File > Import > 各SVGファイルを選択
   ```
   - 各画面ごとに別々のFrameとしてインポート
   - サイズ: 393 × 852 px（iPhone 14 Pro）

3. **ページ構成の推奨**
   ```
   📄 Cover（カバーページ）
   📄 Wireframes（全5画面）
   📄 Flow Diagram（画面遷移図）
   📄 Components（共通コンポーネント）
   📄 Design System（カラー・タイポグラフィ）
   ```

### Step 2: デザイントークンの設定

#### カラーパレット設定
`design_tokens.json`を参照して、Figma Stylesを作成：

**Primary Colors**
- `Primary/Pink` - #FF69B4
- `Primary/Pink Light` - #FFE4E1
- `Primary/Pink Dark` - #FF1493

**Neutral Colors**
- `Neutral/White` - #FFFFFF
- `Neutral/Gray 50` - #F5F5F5
- `Neutral/Gray 100` - #E5E5E7
- `Neutral/Gray 900` - #1C1C1E
- `Neutral/Black` - #000000

**Semantic Colors**
- `Success/Green` - #4CAF50
- `Error/Red` - #FF0000
- `Info/Blue` - #2196F3

#### タイポグラフィ設定
Text Stylesを作成：

| Style Name | Font | Size | Weight | Line Height |
|-----------|------|------|--------|-------------|
| Heading/Large | SF Pro | 24px | Bold | 32px |
| Heading/Medium | SF Pro | 18px | Bold | 24px |
| Body/Large | SF Pro | 16px | Regular | 24px |
| Body/Medium | SF Pro | 14px | Regular | 20px |
| Body/Small | SF Pro | 12px | Regular | 18px |
| Caption | SF Pro | 11px | Regular | 16px |

> **注意**: SF ProフォントがFigmaで利用できない場合は、**Inter**または**Roboto**で代用可能

### Step 3: 共通コンポーネントの作成

#### 1. Tab Bar Component
```
Frame: 393 × 60 px
背景: #FFFFFF
Border Top: 1px #E5E5E7

[タブアイテム × 5]
- Icon: 24×24
- Label: 9px
- Active State: #FF69B4
- Inactive State: #3A3A3C
```

#### 2. Card Component
```
Auto Layout: Vertical
Padding: 16px
Corner Radius: 12px
Background: #FFFFFF
Border: 1px #E5E5E7
```

#### 3. Button Primary
```
Auto Layout: Horizontal
Padding: 12px 24px
Corner Radius: 14px
Background: #FF69B4
Text: #FFFFFF, 13px Bold
```

#### 4. Button Secondary
```
Auto Layout: Horizontal
Padding: 12px 24px
Corner Radius: 14px
Background: #FFFFFF
Border: 2px #FF69B4
Text: #FF69B4, 13px Bold
```

#### 5. Status Bar (iOS)
```
Frame: 393 × 44 px
背景: #FFFFFF
時刻: 14px, Left: 20px
アイコン: Right: 20px
```

### Step 4: Auto Layout設定

各画面要素にAuto Layoutを適用：

1. **垂直スタック（縦並び）**
   - Spacing: 16px（基本）
   - Padding: 16px（画面端）

2. **水平スタック（横並び）**
   - Spacing: 12px（基本）
   - Spacing: 8px（密なレイアウト）

3. **Grid Layout**
   - Columns: 2 or 3
   - Gutter: 12px
   - Margin: 16px

### Step 5: Variant設定

#### Tab Bar Variants
```
Property 1: Selected Tab
- Home
- Report
- QRCode
- Reward
- Menu

Property 2: State
- Default
- Active
```

#### Button Variants
```
Property 1: Type
- Primary
- Secondary
- Text

Property 2: Size
- Large (Height: 48px)
- Medium (Height: 40px)
- Small (Height: 32px)

Property 3: State
- Default
- Pressed
- Disabled
```

---

## レイアウトグリッド設定

### Mobile Grid（iPhone 14 Pro）
```
Width: 393px
Height: 852px
Columns: 12
Gutter: 8px
Margin: 16px

Safe Area:
- Top: 44px（Status Bar）
- Bottom: 60px（Tab Bar）
```

### 各画面の構造

#### ホーム画面
```
[Status Bar] 44px
[Header] 60px
[Content Area] 688px
  - Card 1: Challenge (140px)
  - Spacing: 15px
  - Card 2: Visit Summary (140px)
  - Spacing: 15px
  - Card 3: Congestion (120px)
  - Spacing: 15px
  - Card 4: Health Data (180px)
[Tab Bar] 60px
```

#### レポート画面
```
[Status Bar] 44px
[Header] 60px
[Tab Filter] 50px
[Chart Card] 220px
[Summary Card] 100px
[List Card] 180px
[Tab Bar] 60px
```

---

## インタラクション設定（Prototype）

### 画面遷移
1. **Tab Bar遷移**（全画面共通）
   ```
   Trigger: On Tap
   Action: Navigate to [画面名]
   Animation: Instant（タブ切り替え）
   ```

2. **アクション遷移**
   ```
   Trigger: On Tap
   Action: Navigate to [画面名]
   Animation: Move In (Right to Left, 300ms)
   Easing: Ease Out
   ```

3. **モーダル表示**
   ```
   Trigger: On Tap
   Action: Open Overlay
   Animation: Move In (Bottom to Top, 250ms)
   Easing: Ease Out
   ```

### ホバー・アクティブ状態
- Buttons: Opacity 0.8 on Hover
- Cards: Shadow elevation on Hover
- List Items: Background #F5F5F5 on Hover

---

## プラグイン推奨

### デザイン効率化
1. **Stark** - アクセシビリティチェック（コントラスト比）
2. **Iconify** - アイコンライブラリ（Lucide icons推奨）
3. **Content Reel** - ダミーテキスト・画像生成
4. **Auto Layout** - 自動レイアウト調整

### 開発連携
1. **Zeplin** - デザイン仕様書自動生成
2. **Figma to Code** - React/Flutter コード生成
3. **Design Tokens** - トークンエクスポート

---

## デザインシステムの拡張

### フェーズ1: ワイヤーフレーム（現在）
- ✅ 基本レイアウト
- ✅ 画面遷移
- ✅ 主要コンポーネント

### フェーズ2: ビジュアルデザイン
- [ ] 写真・イラスト素材
- [ ] アイコンセット
- [ ] グラデーション・エフェクト
- [ ] アニメーション仕様

### フェーズ3: デザイントークン
- [ ] JSON/YAMLエクスポート
- [ ] Flutter Theme生成
- [ ] ダークモード対応

---

## チェックリスト

### インポート完了後の確認事項
- [ ] 全5画面のSVGをインポート
- [ ] カラースタイル設定（10色以上）
- [ ] テキストスタイル設定（6種類以上）
- [ ] Tab Barコンポーネント作成
- [ ] Cardコンポーネント作成（3種類）
- [ ] Buttonコンポーネント作成（Variants設定）
- [ ] Auto Layout適用（全コンポーネント）
- [ ] レイアウトグリッド設定
- [ ] 画面遷移プロトタイプ設定
- [ ] アクセシビリティチェック（Stark）

### デザインレビューポイント
- [ ] iOSデザインガイドライン準拠
- [ ] タッチターゲット最小44×44 px
- [ ] コントラスト比 4.5:1以上
- [ ] テキストサイズ最小11px
- [ ] 一貫したスペーシング（8の倍数）

---

## 参考リソース

### 公式ドキュメント
- [iOS Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/ios)
- [Material Design 3](https://m3.material.io/)
- [Figma Best Practices](https://www.figma.com/best-practices/)

### デザインインスピレーション
- FURDI公式サイト: https://furdi.jp/
- chocoZAP アプリ（参考アプリ）
- Apple Fitness+
- Nike Training Club

---

## サポート

### よくある質問

**Q: SVGの一部が正しくインポートされません**
A: Figmaは一部のSVG効果に対応していません。手動で再作成するか、シンプルなシェイプに置き換えてください。

**Q: フォントが見つかりません**
A: SF Pro → Inter、Noto Sans JPで代用可能です。

**Q: プロトタイプが動作しません**
A: Frameが正しく設定されているか確認してください。各画面は393×852pxのFrameである必要があります。

---

## 更新履歴

| 日付 | バージョン | 更新内容 |
|-----|----------|---------|
| 2025-10-02 | 1.0.0 | 初版作成 |
