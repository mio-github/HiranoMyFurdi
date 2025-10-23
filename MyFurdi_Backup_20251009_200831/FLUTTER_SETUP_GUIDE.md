# MyFurdi Flutter実装ガイド

## 📱 ReactモックからFlutterへの移行手順

このガイドでは、現在のReactモックアプリをFlutterで実装し、実際のiPhoneで動かすまでの手順を説明します。

---

## ステップ1: Flutter環境のセットアップ

### 1.1 Flutterのインストール

```bash
# Homebrewでインストール（推奨）
brew install --cask flutter

# PATHを通す（~/.zshrc または ~/.bashrc に追加）
export PATH="$PATH:/usr/local/Caskroom/flutter/bin"

# 設定を反映
source ~/.zshrc
```

### 1.2 Flutter環境の確認

```bash
# Flutterのバージョン確認
flutter --version

# 環境診断（不足しているツールを確認）
flutter doctor

# iOS開発に必要なツールの確認
flutter doctor --verbose
```

### 1.3 必要なツールのインストール

**Xcode**（すでにインストール済みの場合はスキップ）:
```bash
# Xcodeがインストールされているか確認
xcode-select -p

# インストールされていない場合
# App StoreからXcodeをインストール
# https://apps.apple.com/jp/app/xcode/id497799835

# Xcode Command Line Toolsのインストール
sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer
sudo xcodebuild -runFirstLaunch

# ライセンスに同意
sudo xcodebuild -license accept
```

**CocoaPods**（iOSの依存関係管理）:
```bash
sudo gem install cocoapods
pod setup
```

### 1.4 iOSシミュレータの確認

```bash
# 利用可能なシミュレータ一覧
xcrun simctl list devices

# iPhoneシミュレータを起動
open -a Simulator
```

---

## ステップ2: Flutterプロジェクトの作成

### 2.1 プロジェクトの作成

```bash
# プロジェクトフォルダに移動
cd "/Volumes/KIOXIA/Developments/withAI/Vercel/Furdi/MyFURDI /HiranoMyFurdi"

# Flutterプロジェクトを作成
flutter create myfurdi_flutter_app --org jp.furdi.app

# プロジェクトに移動
cd myfurdi_flutter_app
```

### 2.2 プロジェクト構造

```
myfurdi_flutter_app/
├── lib/
│   ├── main.dart              # アプリのエントリーポイント
│   ├── screens/               # 各画面
│   │   ├── home_screen.dart
│   │   ├── report_screen.dart
│   │   ├── qrcode_screen.dart
│   │   ├── reward_screen.dart
│   │   ├── menu_screen.dart
│   │   └── dna_result_screen.dart
│   ├── widgets/               # 共通ウィジェット
│   │   └── custom_tab_bar.dart
│   └── theme/                 # テーマ設定
│       └── app_theme.dart
├── ios/                       # iOSネイティブコード
├── android/                   # Androidネイティブコード
├── assets/                    # 画像・フォント等
└── pubspec.yaml              # 依存関係設定
```

---

## ステップ3: 依存関係とテーマの設定

### 3.1 pubspec.yaml の編集

```yaml
name: myfurdi_flutter_app
description: FURDI会員向けフィットネスサポートアプリ
publish_to: 'none'
version: 1.0.0+1

environment:
  sdk: '>=3.0.0 <4.0.0'

dependencies:
  flutter:
    sdk: flutter

  # UI関連
  cupertino_icons: ^1.0.6
  google_fonts: ^6.1.0

  # 状態管理
  flutter_riverpod: ^2.4.9

  # QRコード生成
  qr_flutter: ^4.1.0

  # グラフ・チャート
  fl_chart: ^0.65.0

  # ナビゲーション
  go_router: ^13.0.0

  # HTTP通信
  dio: ^5.4.0

  # ローカルストレージ
  shared_preferences: ^2.2.2

  # 日付処理
  intl: ^0.19.0

dev_dependencies:
  flutter_test:
    sdk: flutter
  flutter_lints: ^3.0.0

flutter:
  uses-material-design: true

  # アセットの追加（必要に応じて）
  # assets:
  #   - assets/images/
  #   - assets/icons/
```

### 3.2 依存関係のインストール

```bash
flutter pub get
```

---

## ステップ4: テーマの設定

### 4.1 lib/theme/app_theme.dart の作成

```dart
import 'package:flutter/material.dart';
import 'package:flutter/cupertino.dart';

class AppTheme {
  // カラーパレット（FURDI公式カラー）
  static const Color primaryPink = Color(0xFFFF69B4);
  static const Color primaryPinkLight = Color(0xFFFFE4E1);
  static const Color primaryPinkDark = Color(0xFFFF1493);

  static const Color neutralGray = Color(0xFFF5F5F5);
  static const Color textPrimary = Color(0xFF1C1C1E);
  static const Color textSecondary = Color(0xFF3A3A3C);

  static const Color successGreen = Color(0xFF4CAF50);
  static const Color infoBlue = Color(0xFF2196F3);
  static const Color warningOrange = Color(0xFFFF9800);

  static const Color separator = Color(0xFFE5E5E7);
  static const Color cardBackground = Colors.white;

  // Material Themeデータ（Android用）
  static ThemeData materialTheme() {
    return ThemeData(
      useMaterial3: true,
      colorScheme: ColorScheme.fromSeed(
        seedColor: primaryPink,
        primary: primaryPink,
        secondary: infoBlue,
        surface: neutralGray,
      ),
      scaffoldBackgroundColor: neutralGray,
      appBarTheme: const AppBarTheme(
        backgroundColor: Colors.white,
        foregroundColor: textPrimary,
        elevation: 0,
        centerTitle: true,
      ),
      cardTheme: CardTheme(
        color: cardBackground,
        elevation: 0,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(12),
          side: const BorderSide(color: separator, width: 1),
        ),
      ),
      textTheme: const TextTheme(
        headlineLarge: TextStyle(
          fontSize: 24,
          fontWeight: FontWeight.bold,
          color: textPrimary,
        ),
        headlineMedium: TextStyle(
          fontSize: 18,
          fontWeight: FontWeight.bold,
          color: textPrimary,
        ),
        bodyLarge: TextStyle(
          fontSize: 16,
          color: textPrimary,
        ),
        bodyMedium: TextStyle(
          fontSize: 14,
          color: textSecondary,
        ),
        bodySmall: TextStyle(
          fontSize: 12,
          color: textSecondary,
        ),
        labelSmall: TextStyle(
          fontSize: 11,
          color: textSecondary,
        ),
      ),
    );
  }

  // iOS Cupertinoテーマ
  static CupertinoThemeData cupertinoTheme() {
    return const CupertinoThemeData(
      primaryColor: primaryPink,
      scaffoldBackgroundColor: neutralGray,
      barBackgroundColor: Colors.white,
      textTheme: CupertinoTextThemeData(
        primaryColor: textPrimary,
        textStyle: TextStyle(
          fontSize: 16,
          color: textPrimary,
        ),
      ),
    );
  }
}
```

---

## ステップ5: メイン画面の実装

### 5.1 lib/main.dart の実装

```dart
import 'package:flutter/material.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/services.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'dart:io';

import 'theme/app_theme.dart';
import 'screens/home_screen.dart';
import 'screens/report_screen.dart';
import 'screens/qrcode_screen.dart';
import 'screens/reward_screen.dart';
import 'screens/menu_screen.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();

  // ステータスバーの設定
  SystemChrome.setSystemUIOverlayStyle(
    const SystemUiOverlayStyle(
      statusBarColor: Colors.transparent,
      statusBarIconBrightness: Brightness.dark,
    ),
  );

  runApp(
    const ProviderScope(
      child: MyFurdiApp(),
    ),
  );
}

class MyFurdiApp extends StatelessWidget {
  const MyFurdiApp({super.key});

  @override
  Widget build(BuildContext context) {
    // プラットフォーム判定でMaterialまたはCupertinoを使い分け
    if (Platform.isIOS) {
      return CupertinoApp(
        title: 'MyFurdi',
        theme: AppTheme.cupertinoTheme(),
        home: const MainTabScreen(),
        debugShowCheckedModeBanner: false,
      );
    } else {
      return MaterialApp(
        title: 'MyFurdi',
        theme: AppTheme.materialTheme(),
        home: const MainTabScreen(),
        debugShowCheckedModeBanner: false,
      );
    }
  }
}

// タブバー付きメイン画面
class MainTabScreen extends ConsumerStatefulWidget {
  const MainTabScreen({super.key});

  @override
  ConsumerState<MainTabScreen> createState() => _MainTabScreenState();
}

class _MainTabScreenState extends ConsumerState<MainTabScreen> {
  int _currentIndex = 0;

  final List<Widget> _screens = [
    const HomeScreen(),
    const ReportScreen(),
    const QRCodeScreen(),
    const RewardScreen(),
    const MenuScreen(),
  ];

  @override
  Widget build(BuildContext context) {
    if (Platform.isIOS) {
      // iOS: CupertinoTabScaffold
      return CupertinoTabScaffold(
        tabBar: CupertinoTabBar(
          backgroundColor: Colors.white,
          activeColor: AppTheme.primaryPink,
          inactiveColor: AppTheme.textSecondary,
          height: 60,
          items: const [
            BottomNavigationBarItem(
              icon: Icon(CupertinoIcons.home),
              label: 'ホーム',
            ),
            BottomNavigationBarItem(
              icon: Icon(CupertinoIcons.chart_bar),
              label: 'レポート',
            ),
            BottomNavigationBarItem(
              icon: Icon(CupertinoIcons.qrcode),
              label: '入館証',
            ),
            BottomNavigationBarItem(
              icon: Icon(CupertinoIcons.trophy),
              label: 'リワード',
            ),
            BottomNavigationBarItem(
              icon: Icon(CupertinoIcons.settings),
              label: 'メニュー',
            ),
          ],
        ),
        tabBuilder: (context, index) {
          return CupertinoTabView(
            builder: (context) => _screens[index],
          );
        },
      );
    } else {
      // Android: Scaffold + BottomNavigationBar
      return Scaffold(
        body: _screens[_currentIndex],
        bottomNavigationBar: BottomNavigationBar(
          currentIndex: _currentIndex,
          onTap: (index) {
            setState(() {
              _currentIndex = index;
            });
          },
          selectedItemColor: AppTheme.primaryPink,
          unselectedItemColor: AppTheme.textSecondary,
          type: BottomNavigationBarType.fixed,
          backgroundColor: Colors.white,
          selectedFontSize: 9,
          unselectedFontSize: 9,
          items: const [
            BottomNavigationBarItem(
              icon: Icon(Icons.home),
              label: 'ホーム',
            ),
            BottomNavigationBarItem(
              icon: Icon(Icons.bar_chart),
              label: 'レポート',
            ),
            BottomNavigationBarItem(
              icon: Icon(Icons.qr_code),
              label: '入館証',
            ),
            BottomNavigationBarItem(
              icon: Icon(Icons.emoji_events),
              label: 'リワード',
            ),
            BottomNavigationBarItem(
              icon: Icon(Icons.menu),
              label: 'メニュー',
            ),
          ],
        ),
      );
    }
  }
}
```

---

## ステップ6: 各画面の実装例

### 6.1 lib/screens/home_screen.dart

```dart
import 'package:flutter/material.dart';
import 'package:flutter/cupertino.dart';
import 'dart:io';
import '../theme/app_theme.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppTheme.neutralGray,
      appBar: AppBar(
        title: const Text('ホーム'),
        backgroundColor: Colors.white,
        elevation: 0,
      ),
      body: SafeArea(
        child: SingleChildScrollView(
          padding: const EdgeInsets.all(16),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              // ウェルカムカード
              _buildWelcomeCard(),
              const SizedBox(height: 16),

              // チャレンジセクション
              _buildSectionTitle('今日のチャレンジ'),
              const SizedBox(height: 12),
              _buildChallengeCard(
                title: 'FURDI トレーニング',
                subtitle: '今日のトレーニングを完了',
                progress: 0.0,
                icon: CupertinoIcons.sportscourt,
              ),
              const SizedBox(height: 12),
              _buildChallengeCard(
                title: '体組成測定',
                subtitle: '今週の測定を完了',
                progress: 0.5,
                icon: CupertinoIcons.chart_bar_alt_fill,
              ),
              const SizedBox(height: 16),

              // 混雑状況セクション
              _buildSectionTitle('店舗混雑状況'),
              const SizedBox(height: 12),
              _buildCongestionCard(),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildWelcomeCard() {
    return Container(
      padding: const EdgeInsets.all(20),
      decoration: BoxDecoration(
        gradient: LinearGradient(
          colors: [AppTheme.primaryPink, AppTheme.primaryPinkDark],
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
        ),
        borderRadius: BorderRadius.circular(16),
      ),
      child: const Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            'こんにちは！',
            style: TextStyle(
              color: Colors.white,
              fontSize: 24,
              fontWeight: FontWeight.bold,
            ),
          ),
          SizedBox(height: 8),
          Text(
            '今日も素敵な一日を！',
            style: TextStyle(
              color: Colors.white,
              fontSize: 16,
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildSectionTitle(String title) {
    return Text(
      title,
      style: const TextStyle(
        fontSize: 18,
        fontWeight: FontWeight.bold,
        color: AppTheme.textPrimary,
      ),
    );
  }

  Widget _buildChallengeCard({
    required String title,
    required String subtitle,
    required double progress,
    required IconData icon,
  }) {
    return Container(
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(12),
        border: Border.all(color: AppTheme.separator),
      ),
      child: Row(
        children: [
          Container(
            width: 48,
            height: 48,
            decoration: BoxDecoration(
              color: AppTheme.primaryPinkLight,
              borderRadius: BorderRadius.circular(24),
            ),
            child: Icon(
              icon,
              color: AppTheme.primaryPink,
              size: 24,
            ),
          ),
          const SizedBox(width: 16),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  title,
                  style: const TextStyle(
                    fontSize: 16,
                    fontWeight: FontWeight.bold,
                    color: AppTheme.textPrimary,
                  ),
                ),
                const SizedBox(height: 4),
                Text(
                  subtitle,
                  style: const TextStyle(
                    fontSize: 14,
                    color: AppTheme.textSecondary,
                  ),
                ),
                const SizedBox(height: 8),
                LinearProgressIndicator(
                  value: progress,
                  backgroundColor: AppTheme.neutralGray,
                  valueColor: const AlwaysStoppedAnimation<Color>(
                    AppTheme.primaryPink,
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildCongestionCard() {
    return Container(
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(12),
        border: Border.all(color: AppTheme.separator),
      ),
      child: Column(
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              const Text(
                '現在の混雑度',
                style: TextStyle(
                  fontSize: 16,
                  fontWeight: FontWeight.bold,
                  color: AppTheme.textPrimary,
                ),
              ),
              Container(
                padding: const EdgeInsets.symmetric(
                  horizontal: 12,
                  vertical: 6,
                ),
                decoration: BoxDecoration(
                  color: AppTheme.successGreen.withOpacity(0.1),
                  borderRadius: BorderRadius.circular(16),
                ),
                child: const Text(
                  '空いています',
                  style: TextStyle(
                    fontSize: 12,
                    fontWeight: FontWeight.bold,
                    color: AppTheme.successGreen,
                  ),
                ),
              ),
            ],
          ),
          const SizedBox(height: 16),
          Row(
            children: List.generate(5, (index) {
              return Expanded(
                child: Container(
                  margin: EdgeInsets.only(
                    right: index < 4 ? 4 : 0,
                  ),
                  height: 40 + (index * 8.0),
                  decoration: BoxDecoration(
                    color: index < 2
                        ? AppTheme.successGreen
                        : AppTheme.neutralGray,
                    borderRadius: BorderRadius.circular(4),
                  ),
                ),
              );
            }),
          ),
          const SizedBox(height: 12),
          const Text(
            '最終更新: 5分前',
            style: TextStyle(
              fontSize: 12,
              color: AppTheme.textSecondary,
            ),
          ),
        ],
      ),
    );
  }
}
```

### 6.2 他の画面のスケルトン実装

**lib/screens/report_screen.dart:**
```dart
import 'package:flutter/material.dart';
import '../theme/app_theme.dart';

class ReportScreen extends StatelessWidget {
  const ReportScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppTheme.neutralGray,
      appBar: AppBar(
        title: const Text('レポート'),
        backgroundColor: Colors.white,
      ),
      body: const Center(
        child: Text('レポート画面（実装予定）'),
      ),
    );
  }
}
```

**lib/screens/qrcode_screen.dart:**
```dart
import 'package:flutter/material.dart';
import 'package:qr_flutter/qr_flutter.dart';
import '../theme/app_theme.dart';

class QRCodeScreen extends StatelessWidget {
  const QRCodeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppTheme.neutralGray,
      appBar: AppBar(
        title: const Text('入館証'),
        backgroundColor: Colors.white,
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Container(
              padding: const EdgeInsets.all(24),
              decoration: BoxDecoration(
                color: Colors.white,
                borderRadius: BorderRadius.circular(16),
              ),
              child: QrImageView(
                data: 'FURDI-MEMBER-001',
                version: QrVersions.auto,
                size: 200.0,
              ),
            ),
            const SizedBox(height: 16),
            const Text(
              '会員番号: 001',
              style: TextStyle(
                fontSize: 16,
                fontWeight: FontWeight.bold,
              ),
            ),
          ],
        ),
      ),
    );
  }
}
```

**lib/screens/reward_screen.dart:**
```dart
import 'package:flutter/material.dart';
import '../theme/app_theme.dart';

class RewardScreen extends StatelessWidget {
  const RewardScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppTheme.neutralGray,
      appBar: AppBar(
        title: const Text('リワード'),
        backgroundColor: Colors.white,
      ),
      body: const Center(
        child: Text('リワード画面（実装予定）'),
      ),
    );
  }
}
```

**lib/screens/menu_screen.dart:**
```dart
import 'package:flutter/material.dart';
import '../theme/app_theme.dart';

class MenuScreen extends StatelessWidget {
  const MenuScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppTheme.neutralGray,
      appBar: AppBar(
        title: const Text('メニュー'),
        backgroundColor: Colors.white,
      ),
      body: const Center(
        child: Text('メニュー画面（実装予定）'),
      ),
    );
  }
}
```

---

## ステップ7: iPhoneでの実行

### 7.1 iOSシミュレータで実行

```bash
# 利用可能なデバイスを確認
flutter devices

# シミュレータで実行
flutter run -d ios

# または特定のシミュレータを指定
flutter run -d "iPhone 15 Pro"
```

### 7.2 実機（iPhone）で実行

#### a. Apple Developer登録

1. Apple Developer Program に登録（年間 ¥12,980）
   https://developer.apple.com/programs/

2. Xcodeで開発者アカウントを設定:
   - Xcode > Settings > Accounts
   - 「+」ボタンで Apple ID を追加

#### b. iOSプロジェクトの設定

```bash
# iOSフォルダを開く
open ios/Runner.xcworkspace
```

**Xcodeでの設定:**

1. **Signing & Capabilities**タブを選択
2. **Automatically manage signing** にチェック
3. **Team** で自分のApple Developer チームを選択
4. **Bundle Identifier** を一意の名前に変更（例: `jp.furdi.app.myfurdi`）

#### c. iPhoneをMacに接続

1. iPhoneをUSBケーブルでMacに接続
2. iPhone側で「このコンピュータを信頼」をタップ
3. **設定 > 一般 > VPNとデバイス管理** で開発者アプリを信頼

#### d. 実機で実行

```bash
# 接続されたデバイスを確認
flutter devices

# 実機で実行（デバイス名を指定）
flutter run -d "Your iPhone Name"

# またはデバイスIDを指定
flutter run -d 00008030-XXXXXXXXXXXX
```

### 7.3 リリースビルド

```bash
# iOSリリースビルド
flutter build ios --release

# App Storeへの提出用ビルド（Xcodeから実行）
# Xcode > Product > Archive
```

---

## ステップ8: 開発のヒント

### 8.1 ホットリロード

アプリ実行中にコードを変更したら:
```bash
# ホットリロード（状態を保持）
r

# ホットリスタート（状態をリセット）
R

# アプリ終了
q
```

### 8.2 デバッグ

```dart
// デバッグプリント
print('デバッグメッセージ');
debugPrint('詳細なデバッグ情報');

// Flutterインスペクタ（VS Code / Android Studio）
// ウィジェットツリーの確認、レイアウト問題の診断
```

### 8.3 パフォーマンス確認

```bash
# パフォーマンスモードで実行
flutter run --profile

# FPS、メモリ使用量を確認
# DevTools起動
flutter pub global activate devtools
flutter pub global run devtools
```

### 8.4 エラー対応

**CocoaPodsエラー:**
```bash
cd ios
pod install
pod update
cd ..
flutter clean
flutter pub get
```

**ビルドエラー:**
```bash
flutter clean
flutter pub get
cd ios && rm -rf Pods Podfile.lock && pod install && cd ..
flutter run
```

---

## ステップ9: 次のステップ

### 優先順位1: コア機能の実装
- [ ] QRコード生成（入館証）
- [ ] ログイン・認証機能
- [ ] API連携（PIXFORMANCE, TANITA, SECOM）

### 優先順位2: データ表示
- [ ] レポート画面（グラフ・チャート）
- [ ] リワード画面（バッジ、進捗）
- [ ] DNA検査結果画面（レーダーチャート）

### 優先順位3: 拡張機能
- [ ] プッシュ通知（Firebase Cloud Messaging）
- [ ] 混雑状況リアルタイム更新
- [ ] ダークモード対応

### 優先順位4: テストとCI/CD
- [ ] ユニットテスト
- [ ] Widgetテスト
- [ ] Integrationテスト
- [ ] GitHub Actions / Codemagic

---

## まとめ

このガイドに従って：

1. ✅ Flutter環境をセットアップ
2. ✅ プロジェクトを作成
3. ✅ FURDI公式カラー・デザインシステムを適用
4. ✅ iOS/Android両対応のUI実装
5. ✅ iPhoneシミュレータまたは実機で動作確認

現在のReactモックと同じUI・UXをFlutterで再現し、実際のiPhoneで動かすことができます。

**困ったときは:**
- Flutter公式ドキュメント: https://docs.flutter.dev/
- Flutter日本語コミュニティ: https://flutter-jp.connpass.com/
- Stack Overflow: https://stackoverflow.com/questions/tagged/flutter
