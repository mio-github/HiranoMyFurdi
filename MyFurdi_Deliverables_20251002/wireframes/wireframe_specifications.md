# MyFurdi ワイヤーフレーム仕様書

## ドキュメント情報
- **バージョン**: 1.0.0
- **作成日**: 2025-10-02
- **対象**: 開発チーム（Flutter/iOS/Android）
- **画面数**: 5画面 + 遷移図

---

## 目次
1. [概要](#概要)
2. [共通仕様](#共通仕様)
3. [各画面詳細仕様](#各画面詳細仕様)
4. [画面遷移仕様](#画面遷移仕様)
5. [実装ガイドライン](#実装ガイドライン)

---

## 概要

### アプリケーション情報
- **アプリ名**: MyFurdi
- **対象OS**: iOS 14.0+, Android 8.0+
- **開発フレームワーク**: Flutter 3.x
- **デザインシステム**: iOS Human Interface Guidelines準拠
- **ターゲットデバイス**: iPhone 14 Pro (393×852)を基準

### ファイル構成
```
wireframes/
├── 01_home_screen.svg              # ホーム画面
├── 02_report_screen.svg            # レポート画面
├── 03_qrcode_screen.svg            # 入館証画面
├── 04_reward_screen.svg            # リワード画面
├── 05_menu_screen.svg              # メニュー画面
├── screen_transition_diagram.svg   # 画面遷移図
├── design_tokens.json              # デザイントークン
├── figma_components.json           # コンポーネント仕様
├── figma_import_guide.md           # Figmaインポートガイド
└── wireframe_specifications.md     # 本ドキュメント
```

---

## 共通仕様

### 1. 画面サイズとレイアウト

#### デバイスサイズ
```dart
// Flutter実装例
class ScreenSizes {
  static const double width = 393.0;   // iPhone 14 Pro
  static const double height = 852.0;  // iPhone 14 Pro

  // Safe Area
  static const double statusBarHeight = 44.0;
  static const double tabBarHeight = 60.0;
  static const double headerHeight = 60.0;

  // Content Area
  static const double contentHeight = 688.0;  // 852 - 44 - 60 - 60
}
```

#### レイアウトグリッド
- **カラム数**: 12
- **ガター幅**: 8px
- **画面マージン**: 左右16px
- **セクション間ギャップ**: 15px

### 2. カラーパレット

#### Primary Colors
```dart
class AppColors {
  // Primary
  static const Color furdiPink = Color(0xFFFF69B4);
  static const Color furdiPinkLight = Color(0xFFFFE4E1);
  static const Color furdiPinkDark = Color(0xFFFF1493);

  // Neutral
  static const Color white = Color(0xFFFFFFFF);
  static const Color gray50 = Color(0xFFF5F5F5);
  static const Color gray100 = Color(0xFFE5E5E7);
  static const Color gray500 = Color(0xFF3A3A3C);
  static const Color gray900 = Color(0xFF1C1C1E);
  static const Color black = Color(0xFF000000);

  // Semantic
  static const Color success = Color(0xFF4CAF50);
  static const Color error = Color(0xFFFF0000);
  static const Color info = Color(0xFF2196F3);
  static const Color warning = Color(0xFFFF9800);
}
```

#### グラデーション
```dart
// Primary Gradient
const LinearGradient primaryGradient = LinearGradient(
  begin: Alignment.topLeft,
  end: Alignment.bottomRight,
  colors: [Color(0xFFFF69B4), Color(0xFFFF1493)],
);
```

### 3. タイポグラフィ

#### フォント設定
```dart
class AppTextStyles {
  static const String fontFamily = 'SF Pro Display';

  // Headings
  static const TextStyle headingLarge = TextStyle(
    fontSize: 24,
    fontWeight: FontWeight.bold,
    color: AppColors.gray900,
    height: 1.33,
  );

  static const TextStyle headingMedium = TextStyle(
    fontSize: 18,
    fontWeight: FontWeight.bold,
    color: AppColors.gray900,
    height: 1.33,
  );

  // Body
  static const TextStyle bodyLarge = TextStyle(
    fontSize: 16,
    fontWeight: FontWeight.normal,
    color: AppColors.gray900,
    height: 1.5,
  );

  static const TextStyle bodyMedium = TextStyle(
    fontSize: 14,
    fontWeight: FontWeight.normal,
    color: AppColors.gray900,
    height: 1.43,
  );

  static const TextStyle bodySmall = TextStyle(
    fontSize: 12,
    fontWeight: FontWeight.normal,
    color: AppColors.gray500,
    height: 1.5,
  );

  static const TextStyle caption = TextStyle(
    fontSize: 11,
    fontWeight: FontWeight.normal,
    color: AppColors.gray500,
    height: 1.45,
  );

  static const TextStyle tabLabel = TextStyle(
    fontSize: 9,
    fontWeight: FontWeight.normal,
    color: AppColors.gray500,
    height: 1.33,
  );
}
```

### 4. 共通コンポーネント

#### Status Bar
- **高さ**: 44px
- **背景色**: #FFFFFF
- **テキスト**: 14px, #000000
- **要素**:
  - 左: 時刻表示（"9:41"）
  - 右: システムアイコン（電波・Wi-Fi・バッテリー）

```dart
Widget buildStatusBar() {
  return Container(
    height: 44,
    color: Colors.white,
    padding: EdgeInsets.symmetric(horizontal: 20),
    child: Row(
      mainAxisAlignment: MainAxisAlignment.spaceBetween,
      children: [
        Text('9:41', style: TextStyle(fontSize: 14)),
        Text('📶 🔋', style: TextStyle(fontSize: 12)),
      ],
    ),
  );
}
```

#### Header
- **高さ**: 60px
- **背景色**: #FFFFFF
- **タイトル**: 18px, Bold, #1C1C1E
- **中央配置**

```dart
Widget buildHeader(String title) {
  return Container(
    height: 60,
    color: Colors.white,
    alignment: Alignment.center,
    child: Text(
      title,
      style: AppTextStyles.headingMedium,
    ),
  );
}
```

#### Tab Bar
- **高さ**: 60px
- **背景色**: #FFFFFF
- **上ボーダー**: 1px, #E5E5E7
- **アイコンサイズ**: 24×24
- **ラベルサイズ**: 9px
- **アクティブカラー**: #FF69B4
- **非アクティブカラー**: #3A3A3C

```dart
Widget buildTabBar(int selectedIndex) {
  return Container(
    height: 60,
    decoration: BoxDecoration(
      color: Colors.white,
      border: Border(top: BorderSide(color: AppColors.gray100)),
    ),
    child: Row(
      mainAxisAlignment: MainAxisAlignment.spaceAround,
      children: [
        _buildTabItem('🏠', 'ホーム', 0, selectedIndex),
        _buildTabItem('📊', 'レポート', 1, selectedIndex),
        _buildTabItem('🎫', '入館証', 2, selectedIndex),
        _buildTabItem('🏆', 'リワード', 3, selectedIndex),
        _buildTabItem('⚙️', 'メニュー', 4, selectedIndex),
      ],
    ),
  );
}

Widget _buildTabItem(String icon, String label, int index, int selected) {
  final isActive = index == selected;
  final color = isActive ? AppColors.furdiPink : AppColors.gray500;

  return Column(
    mainAxisAlignment: MainAxisAlignment.center,
    children: [
      Text(icon, style: TextStyle(fontSize: 24, color: color)),
      SizedBox(height: 4),
      Text(
        label,
        style: AppTextStyles.tabLabel.copyWith(
          color: color,
          fontWeight: isActive ? FontWeight.bold : FontWeight.normal,
        ),
      ),
    ],
  );
}
```

#### Card Component
```dart
Widget buildCard({
  required Widget child,
  double? height,
  EdgeInsets? padding,
}) {
  return Container(
    height: height,
    margin: EdgeInsets.symmetric(horizontal: 16),
    padding: padding ?? EdgeInsets.all(16),
    decoration: BoxDecoration(
      color: Colors.white,
      borderRadius: BorderRadius.circular(12),
      border: Border.all(color: AppColors.gray100),
    ),
    child: child,
  );
}
```

#### Button Components
```dart
// Primary Button
Widget buildPrimaryButton({
  required String label,
  required VoidCallback onPressed,
}) {
  return Container(
    height: 48,
    child: ElevatedButton(
      onPressed: onPressed,
      style: ElevatedButton.styleFrom(
        backgroundColor: AppColors.furdiPink,
        foregroundColor: Colors.white,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(16),
        ),
      ),
      child: Text(label, style: TextStyle(fontSize: 13, fontWeight: FontWeight.bold)),
    ),
  );
}

// Secondary Button
Widget buildSecondaryButton({
  required String label,
  required VoidCallback onPressed,
}) {
  return Container(
    height: 48,
    child: OutlinedButton(
      onPressed: onPressed,
      style: OutlinedButton.styleFrom(
        foregroundColor: AppColors.furdiPink,
        side: BorderSide(color: AppColors.furdiPink, width: 2),
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(16),
        ),
      ),
      child: Text(label, style: TextStyle(fontSize: 13, fontWeight: FontWeight.bold)),
    ),
  );
}
```

---

## 各画面詳細仕様

### 1. ホーム画面 (Home Screen)
**ファイル**: `01_home_screen.svg`

#### レイアウト構造
```
[Status Bar]          44px
[Header]              60px
[Content Area]        688px
  - Challenge Card    140px
  - Gap               15px
  - Visit Summary     140px
  - Gap               15px
  - Congestion Card   120px
  - Gap               15px
  - Health Data Card  180px
  - Bottom Padding    78px
[Tab Bar]             60px
```

#### 主要要素

##### 1.1 Challenge Card
- **サイズ**: 361×140 (margin: 16px)
- **背景**: #FFFFFF
- **ボーダー**: 1px #E5E5E7
- **角丸**: 12px

**要素**:
- タイトル: "🎯 今日のチャレンジ" (14px, Bold)
- チャレンジ内容カード:
  - 背景: #FFE4E1
  - 角丸: 8px
  - 高さ: 60px
  - テキスト: "体重を記録する" (13px)
  - サブテキスト: "報酬: デイリーバッジ 🏅" (11px, #FF69B4)
- アクションボタン:
  - 高さ: 32px
  - 背景: #FF69B4
  - テキスト: "1タップで記録する" (13px, Bold, #FFFFFF)

##### 1.2 Visit Summary Card
- **サイズ**: 361×140
- **主要機能**:
  - 連続来店表示: "🔥 5日連続来店中！" (20px, Bold)
  - 週間進捗:
    - ラベル: "今週の来店" (12px)
    - 値: "3/4回" (12px, Bold, 右寄せ)
    - プログレスバー: 高さ8px, 角丸4px, 背景#F5F5F5, 塗り#FF69B4
  - 前回来店: "昨日 18:30" (12px)

##### 1.3 Congestion Card
- **サイズ**: 361×120
- **要素**:
  - 店舗名: "📍 渋谷店（お気に入り）" (12px, #3A3A3C)
  - ステータス:
    - インジケーター: 直径12px, #4CAF50
    - テキスト: "かなり空いています" (16px, Bold)
    - 利用率: "現在の利用率: 25%" (11px)
  - アクションボタン×2:
    - "詳しく見る" (Primary)
    - "今から行く" (Secondary)
    - 各160×28, 角丸14px

##### 1.4 Health Data Card
- **サイズ**: 361×180
- **タブ**: 体重（アクティブ）、体脂肪、歩数
- **データ表示**:
  - 数値: "54.2 kg" (28px, Bold)
  - 変化: "↓ -0.3kg (前回比)" (13px, #4CAF50)
  - コメント: "順調に減っています✨" (13px, #4CAF50)
- **記録ボタン**: 333×32, 角丸16px, #FF69B4

#### 実装コード例
```dart
class HomeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Column(
        children: [
          buildStatusBar(),
          buildHeader('おはようございます、さくらさん！'),
          Expanded(
            child: SingleChildScrollView(
              padding: EdgeInsets.only(bottom: 16),
              child: Column(
                children: [
                  SizedBox(height: 16),
                  _buildChallengeCard(),
                  SizedBox(height: 15),
                  _buildVisitSummaryCard(),
                  SizedBox(height: 15),
                  _buildCongestionCard(),
                  SizedBox(height: 15),
                  _buildHealthDataCard(),
                ],
              ),
            ),
          ),
          buildTabBar(0),
        ],
      ),
    );
  }
}
```

---

### 2. レポート画面 (Report Screen)
**ファイル**: `02_report_screen.svg`

#### レイアウト構造
```
[Status Bar]          44px
[Header]              60px
[Tab Filter]          50px
[Content Area]        638px
  - Chart Card        220px
  - Gap               15px
  - Summary Card      100px
  - Gap               15px
  - Exercise List     180px
  - Bottom Padding    108px
[Tab Bar]             60px
```

#### 主要要素

##### 2.1 Tab Filter
- **高さ**: 50px
- **タブ**: 運動記録（アクティブ）、体組成、来館履歴
- **アクティブスタイル**:
  - テキスト: 13px, Bold, #FF69B4
  - アンダーライン: 2px, #FF69B4

##### 2.2 Period Filter Chips
- **位置**: タブ下、左寄せ (margin: 16px)
- **サイズ**: 40×28, 角丸14px
- **種類**: 週（アクティブ）、月、年
- **アクティブ**: 背景#FF69B4, テキスト#FFFFFF
- **非アクティブ**: 背景#FFFFFF, ボーダー1px #E5E5E7

##### 2.3 Chart Card
- **サイズ**: 361×220
- **タイトル**: "トレーニング時間（週）" (14px, Bold)
- **棒グラフ**:
  - 棒幅: 40px
  - 棒間隔: 10px
  - 色: #FF69B4
  - 角丸: 4px
  - ラベル: 曜日表示 (10px, #3A3A3C)

##### 2.4 Summary Card
- **サイズ**: 361×100
- **タイトル**: "今週のサマリー" (14px, Bold)
- **統計カード×2**:
  - サイズ: 160×50, 角丸8px
  - 背景: #F5F5F5
  - ラベル: 10px, #3A3A3C
  - 値: 20px, Bold
  - 単位: 12px
  - 例: "総時間 245分", "消費カロリー 1,250kcal"

##### 2.5 Exercise List
- **アイテム高さ**: 60px
- **ディバイダー**: 1px, #E5E5E7
- **要素**:
  - タイトル: 13px, Bold
  - タイムスタンプ: 11px, #3A3A3C (右寄せ)
  - メトリクス: 11px, #3A3A3C (例: "⏱ 45分  💪 中")

---

### 3. 入館証画面 (QR Code Screen)
**ファイル**: `03_qrcode_screen.svg`

#### レイアウト構造
```
[Status Bar]          44px
[Header]              60px
[Content Area]        688px
  - Gap               46px
  - QR Code Display   263px
  - Gap               27px
  - Info Cards        170px (3×50 + 2×10)
  - Store Selection   60px
  - Usage Guide       35px
  - Auto-update       35px
  - Tips Card         60px
  - Bottom Padding    -8px
[Tab Bar]             60px
```

#### 主要要素

##### 3.1 QR Code Display
- **外枠サイズ**: 263×263, 角丸16px
- **ボーダー**: 2px, #E5E5E7
- **背景**: #FFFFFF
- **QRコード領域**: 223×223, 角丸8px
- **インナーボーダー**: 4px, #F5F5F5
- **中央配置**
- **QRパターン**: 簡略化されたシンボル表示

##### 3.2 Info Cards
**3つのカード（各50px高さ、10pxギャップ）**:

1. **会員IDカード**
   - 背景: #F5F5F5, 角丸8px
   - ラベル: "会員ID" (12px, #3A3A3C, 左寄せ)
   - 値: "FUR-2024-0123" (12px, Bold, 右寄せ)

2. **お名前カード**
   - ラベル: "お名前"
   - 値: "さくら様"

3. **有効期限カード**
   - ラベル: "有効期限"
   - 値: "2025年12月31日"

##### 3.3 Store Selection Card
- **サイズ**: 361×60, 角丸12px
- **ボーダー**: 1px, #E5E5E7
- **アイコン**: 🏪 (40px円形、#FFE4E1背景)
- **テキスト**:
  - ラベル: "利用店舗" (10px)
  - 店舗名: "渋谷店" (13px, Bold)
- **右矢印**: ⌄ (16px, #3A3A3C)

##### 3.4 Usage Guide Link
- **アイコン**: ⓘ (16px円形、ボーダー1.5px #FF69B4)
- **テキスト**: "入館方法を見る" (13px, #FF69B4)

##### 3.5 Auto-update Notice
- **テキスト**: "QRコードは30秒ごとに自動更新されます" (11px)
- **ステータス**: 緑丸 + "有効" (11px, #4CAF50)

##### 3.6 Tips Card
- **サイズ**: 361×60, 角丸8px
- **背景**: #FFE4E1
- **タイトル**: "💡 初めての方へ" (11px, Bold, #FF69B4)
- **説明**: 2行、10px

---

### 4. リワード画面 (Reward Screen)
**ファイル**: `04_reward_screen.svg`

#### レイアウト構造
```
[Status Bar]          44px
[Header]              60px
[Tab Filter]          50px
[Content Area]        638px
  - Challenge Card    380px
  - Bonus Card        60px
  - Progress Card     100px
  - Bottom Padding    98px
[Tab Bar]             60px
```

#### 主要要素

##### 4.1 Today's Challenge Card
- **サイズ**: 361×380
- **タイトル**: "🎯 今日のチャレンジ" (14px, Bold)
- **進捗表示**: "3/5" (右上、ピルシェイプ)

**チャレンジアイテム（5つ）**:
- **完了アイテム（3つ）**:
  - 背景: #E8F5E9
  - ボーダー: 1px, #4CAF50
  - チェックマーク: 円形16px, #4CAF50背景
  - 例: "アプリを開く" → "報酬: デイリースタンプ 🎫"

- **未完了アイテム（2つ）**:
  - 背景: #FFFFFF
  - ボーダー: 1px, #E5E5E7
  - チェックボックス: 円形16px、空
  - アクションボタン付き (70×26, #FF69B4)

##### 4.2 Bonus Card
- **サイズ**: 361×60, 角丸8px
- **背景**: グラデーション (#FF69B4 → #FF1493)
- **タイトル**: "🎁 全達成ボーナス" (13px, Bold, #FFFFFF)
- **説明**: "5つすべて達成で特別バッジ獲得！" (11px, #FFFFFF, opacity 0.9)

##### 4.3 Progress Card
- **サイズ**: 361×100
- **タイトル**: "💪 継続は力なり" (13px, Bold)
- **達成率**: "今週のチャレンジ達成率: 85%" (12px)
- **プログレスバー**: 333×8, 角丸4px, 85%塗り
- **メッセージ**: "あと少しで週間目標達成！" (11px, #FF69B4)

---

### 5. メニュー画面 (Menu Screen)
**ファイル**: `05_menu_screen.svg`

#### レイアウト構造
```
[Status Bar]          44px
[Header]              60px
[Content Area]        688px
  - Profile Card      140px
  - Gap               15px
  - Usage Guide       235px (40 + 180 + 15)
  - Gap               15px
  - Content Section   175px (40 + 135)
  - Gap               15px
  - Settings Section  90px (40 + 50)
  - Bottom Padding    -2px
[Tab Bar]             60px
```

#### 主要要素

##### 5.1 Profile Card
- **サイズ**: 361×140, 角丸16px
- **背景**: グラデーション (#FF69B4 → #FF1493)
- **アバター**: 50px円形、#FFFFFF背景
- **ユーザー名**: "さくら様" (16px, Bold, #FFFFFF)
- **会員ID**: "FUR-2024-0123" (12px, #FFFFFF, opacity 0.9)
- **統計カード×3** (各103×50):
  - 背景: #FFFFFF (opacity 0.2)
  - ラベル: 10px, #FFFFFF
  - 値: 16px, Bold, #FFFFFF
  - 例: "会員歴 3ヶ月", "来店回数 52回", "バッジ 15個"

##### 5.2 Usage Guide Section
**セクションヘッダー**:
- サイズ: 361×40, 角丸12px
- 背景: #FFFFFF, ボーダー1px #E5E5E7
- タイトル: "利用ガイド" (11px, Bold)

**リストカード**:
- サイズ: 361×180
- アイテム×4 (各45px + ディバイダー):
  - アイコン: 30px円形、#FFE4E1背景
  - タイトル: 13px
  - 矢印: › (16px, #3A3A3C)
  - 例: "📖 はじめての方へ", "🎬 アプリの使い方"

##### 5.3 Content Section
- **構成**: セクションヘッダー40px + リスト135px
- **アイテム×3**:
  - "🎬 動画トレーニング一覧"
  - "🔔 お知らせ一覧" (バッジ付き: "3")
  - "❓ FAQ・よくある質問"
- **バッジ**: 30×18, 角丸9px, #FF0000背景

##### 5.4 Settings Section
- **セクションヘッダー**: 40px
- **ログアウトボタン**:
  - サイズ: 361×50, 角丸12px
  - 背景: #FFFFFF, ボーダー1px #E5E5E7
  - テキスト: "🚪 ログアウト" (13px, Bold, #FF0000)
  - 中央配置

---

## 画面遷移仕様

### 遷移図
**ファイル**: `screen_transition_diagram.svg`

### ナビゲーション構造

#### タブバーナビゲーション（主要遷移）
```
Home ←→ Report
  ↓       ↓
  ↓       ↓
QRCode ←→ Reward ←→ Menu
```

全画面間でタブバーによる直接遷移が可能

#### アクション遷移

1. **ホーム → レポート**
   - トリガー: 健康データ詳細タップ
   - アニメーション: Slide (right to left, 300ms)

2. **ホーム → リワード**
   - トリガー: チャレンジ達成
   - アニメーション: Slide (right to left, 300ms)

3. **メニュー → 各コンテンツ**
   - トリガー: リストアイテムタップ
   - アニメーション: Slide (right to left, 300ms)

#### モーダル遷移

1. **混雑状況詳細**
   - トリガー: "詳しく見る"ボタン
   - アニメーション: Modal (bottom to top, 250ms)

2. **体重記録**
   - トリガー: "記録する"ボタン
   - アニメーション: Modal (bottom to top, 250ms)

### 実装コード例

```dart
// Navigator 2.0 / Go Router推奨
class AppRouter {
  static const String home = '/';
  static const String report = '/report';
  static const String qrcode = '/qrcode';
  static const String reward = '/reward';
  static const String menu = '/menu';

  static Route<dynamic> generateRoute(RouteSettings settings) {
    switch (settings.name) {
      case home:
        return _buildRoute(HomeScreen());
      case report:
        return _buildRoute(ReportScreen());
      case qrcode:
        return _buildRoute(QRCodeScreen());
      case reward:
        return _buildRoute(RewardScreen());
      case menu:
        return _buildRoute(MenuScreen());
      default:
        return _buildRoute(HomeScreen());
    }
  }

  static PageRoute _buildRoute(Widget screen) {
    return PageRouteBuilder(
      pageBuilder: (context, animation, secondaryAnimation) => screen,
      transitionsBuilder: (context, animation, secondaryAnimation, child) {
        const begin = Offset(1.0, 0.0);
        const end = Offset.zero;
        const curve = Curves.easeOut;

        var tween = Tween(begin: begin, end: end).chain(
          CurveTween(curve: curve),
        );

        return SlideTransition(
          position: animation.drive(tween),
          child: child,
        );
      },
      transitionDuration: Duration(milliseconds: 300),
    );
  }
}

// Tab切り替え（Instant）
void switchTab(int index) {
  setState(() {
    _selectedIndex = index;
  });
  // No animation, instant switch
}
```

---

## 実装ガイドライン

### 1. レスポンシブ対応

#### デバイス対応
- **iPhone**: 12, 13, 14, 14 Pro, 15シリーズ
- **Android**: Samsung Galaxy, Pixel各種

```dart
class ResponsiveLayout {
  static double getWidth(BuildContext context) {
    final screenWidth = MediaQuery.of(context).size.width;
    return screenWidth.clamp(320.0, 428.0);  // Min/Max幅
  }

  static double getCardWidth(BuildContext context) {
    return getWidth(context) - 32;  // 左右margin 16px
  }

  static EdgeInsets getPagePadding(BuildContext context) {
    return EdgeInsets.symmetric(
      horizontal: 16,
      vertical: 0,
    );
  }
}
```

### 2. アクセシビリティ

#### 必須対応項目
- [ ] 最小タッチターゲット: 44×44 px
- [ ] コントラスト比: 4.5:1以上（WCAG AA）
- [ ] フォントサイズ: 最小11px
- [ ] スクリーンリーダー対応（Semantics Widget）
- [ ] ダイナミックフォントサイズ対応

```dart
// タッチターゲット最小サイズ確保
Widget ensureMinTouchTarget({
  required Widget child,
  required VoidCallback onTap,
}) {
  return InkWell(
    onTap: onTap,
    child: ConstrainedBox(
      constraints: BoxConstraints(
        minWidth: 44,
        minHeight: 44,
      ),
      child: child,
    ),
  );
}

// Semantics対応例
Semantics(
  label: 'ホームタブ',
  button: true,
  selected: _selectedIndex == 0,
  child: _buildTabItem('🏠', 'ホーム', 0, _selectedIndex),
)
```

### 3. パフォーマンス

#### 最適化ポイント
1. **画像**: WebP形式、適切なサイズ
2. **リスト**: ListView.builder使用
3. **状態管理**: Provider/Riverpod
4. **アニメーション**: 60fps維持

```dart
// リスト最適化
ListView.builder(
  itemCount: exercises.length,
  itemBuilder: (context, index) {
    return ExerciseListItem(
      data: exercises[index],
    );
  },
  physics: BouncingScrollPhysics(),  // iOS風スクロール
)
```

### 4. ネイティブ機能統合

#### iOS対応
- **Safe Area**: 自動対応
- **Haptic Feedback**: タップ時振動
- **Dark Mode**: 自動切り替え

```dart
// Haptic Feedback
import 'package:flutter/services.dart';

void onButtonPressed() {
  HapticFeedback.lightImpact();
  // Button action
}

// Safe Area
SafeArea(
  child: Scaffold(
    body: /* content */,
  ),
)
```

#### Android対応
- **Material Ripple**: タップエフェクト
- **System Navigation**: ジェスチャー対応

### 5. テスト

#### 必須テスト項目
- [ ] ユニットテスト: ビジネスロジック
- [ ] ウィジェットテスト: 各コンポーネント
- [ ] インテグレーションテスト: 画面遷移
- [ ] Golden Test: ビジュアルリグレッション

```dart
// Widget Test例
testWidgets('Home screen shows challenge card', (tester) async {
  await tester.pumpWidget(MyApp());

  expect(find.text('🎯 今日のチャレンジ'), findsOneWidget);
  expect(find.text('体重を記録する'), findsOneWidget);
});
```

---

## チェックリスト

### デザイン確認
- [ ] 全5画面のレイアウト確認
- [ ] カラーパレット一貫性
- [ ] タイポグラフィ統一
- [ ] スペーシング規則（8の倍数）
- [ ] iOS HIG準拠

### 実装確認
- [ ] 共通コンポーネント実装
- [ ] 画面遷移実装
- [ ] タブバーナビゲーション
- [ ] レスポンシブ対応
- [ ] アクセシビリティ対応

### テスト確認
- [ ] 各画面の表示テスト
- [ ] 画面遷移テスト
- [ ] タップアクションテスト
- [ ] 実機テスト（iOS/Android）

---

## 参考資料

### デザインガイドライン
- [iOS Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/ios)
- [Material Design 3](https://m3.material.io/)
- [Flutter Design Principles](https://docs.flutter.dev/resources/architectural-overview)

### ツール
- **Figma**: `figma_import_guide.md`参照
- **Design Tokens**: `design_tokens.json`
- **Components**: `figma_components.json`

---

## バージョン履歴

| バージョン | 日付 | 更新内容 |
|---------|------|---------|
| 1.0.0 | 2025-10-02 | 初版リリース - 全5画面仕様策定 |

---

## お問い合わせ

仕様に関する質問や追加要件がある場合は、プロジェクトリードまでご連絡ください。
