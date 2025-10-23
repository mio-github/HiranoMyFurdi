# Google Slides API 有効化ガイド

## ⚠️ エラー内容

```
Google Slides API has not been used in project 109341072757 before or it is disabled.
```

## 📝 解決方法

### ステップ1: Google Cloud Consoleにアクセス

以下のURLを**ブラウザで開いてください**:

```
https://console.developers.google.com/apis/api/slides.googleapis.com/overview?project=109341072757
```

または、以下の手順で手動で有効化:

1. **Google Cloud Console** にアクセス
   https://console.cloud.google.com/

2. プロジェクト `109341072757` を選択

3. **左側メニュー** → **「APIとサービス」** → **「ライブラリ」**

4. **検索ボックス**で「Google Slides API」を検索

5. **「Google Slides API」**をクリック

6. **「有効にする」**ボタンをクリック

### ステップ2: 有効化を確認

APIを有効化したら、**数分待ってから**スクリプトを再実行してください。

```bash
cd /Volumes/KIOXIA/Developments/withAI/Vercel/Furdi/MyFURDI/HiranoMyFurdi
uvx --with google-auth-oauthlib --with google-api-python-client python3 create_myfurdi_presentation.py
```

## ✅ 有効化済みのAPI

現在、以下のAPIが有効になっています:
- ✅ Google Sheets API
- ✅ Google Drive API
- ⏳ Google Slides API（これから有効化）

## 📚 参考

**直接有効化URL:**
https://console.developers.google.com/apis/api/slides.googleapis.com/overview?project=109341072757

**Google Slides API ドキュメント:**
https://developers.google.com/slides/api

## 🔄 次のステップ

1. 上記URLでGoogle Slides APIを有効化
2. 2-3分待つ
3. `create_myfurdi_presentation.py` を再実行
4. プレゼンテーション作成成功！
