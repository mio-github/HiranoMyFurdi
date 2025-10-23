# Google OAuth 2.0 設定ガイド

## 問題
`Error 403: access_denied` - アプリがテストモードで、承認されたテストユーザーのみアクセス可能

## 解決方法

### オプション1: テストユーザーを追加（推奨・即座に実行可能）

1. **Google Cloud Console** にアクセス
   https://console.cloud.google.com/

2. プロジェクトを選択

3. **APIs & Services** → **OAuth consent screen**

4. **Test users** セクションで **+ ADD USERS** をクリック

5. あなたのGoogleアカウントのメールアドレスを追加
   - 例: masayahirano@gmail.com (実際のアカウント)

6. **SAVE**

7. スクリプトを再実行:
   ```bash
   cd /Volumes/KIOXIA/Developments/withAI/Vercel/Furdi/MyFURDI/HiranoMyFurdi
   uvx --with google-auth-oauthlib --with google-api-python-client python3 create_sheet_direct.py
   ```

### オプション2: アプリを公開（本番環境用）

1. **Google Cloud Console** にアクセス

2. **APIs & Services** → **OAuth consent screen**

3. **PUBLISH APP** をクリック

4. 審査プロセスを完了（数日〜数週間かかる場合があります）

### オプション3: サービスアカウント認証を使用

より簡単な方法として、サービスアカウントを作成:

1. **Google Cloud Console** → **APIs & Services** → **Credentials**

2. **+ CREATE CREDENTIALS** → **Service account**

3. サービスアカウント名を入力（例: "myfurdi-sheets-creator"）

4. **CREATE AND CONTINUE**

5. ロールを選択: **Editor** または **Owner**

6. **DONE**

7. 作成したサービスアカウントをクリック

8. **KEYS** タブ → **ADD KEY** → **Create new key**

9. **JSON** を選択 → **CREATE**

10. JSONファイルがダウンロードされます

11. ファイルを以下のように配置:
    ```bash
    mv ~/Downloads/your-project-xxxxx.json ~/.config/mcp-google-sheets/service-account.json
    ```

12. スクリプトを修正してサービスアカウント認証を使用

## 次のステップ

上記のいずれかの方法を実行後、再度スクリプトを実行してください。

推奨順序:
1. **オプション1** (最速) → テストユーザーを追加
2. スクリプト再実行
3. 成功！
