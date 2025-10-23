# Google Slides MCP セットアップ完了

## ✅ インストール完了

### インストール場所
```
~/.local/share/mcp-servers/google-slides-mcp/
```

### ビルド済みファイル
```
~/.local/share/mcp-servers/google-slides-mcp/build/index.js
```

## ✅ Claude Code 設定完了

**設定ファイル:** `~/.config/claude-code/mcp_settings.json`

```json
{
  "mcpServers": {
    "google-sheets": {
      "command": "uvx",
      "args": ["mcp-google-sheets@latest"],
      "env": {
        "GOOGLE_APPLICATION_CREDENTIALS": "/Users/masayahirano/.config/mcp-google-sheets/credentials.json"
      }
    },
    "google-docs": {
      "command": "uvx",
      "args": ["mcp-gsuite"],
      "env": {
        "GOOGLE_APPLICATION_CREDENTIALS": "/Users/masayahirano/.config/mcp-google-sheets/credentials.json"
      }
    },
    "google-slides": {
      "command": "node",
      "args": ["/Users/masayahirano/.local/share/mcp-servers/google-slides-mcp/build/index.js"],
      "env": {
        "GOOGLE_CLIENT_ID": "109341072757-l9b2620gt4okkll64qolreb45iurtcjl.apps.googleusercontent.com",
        "GOOGLE_CLIENT_SECRET": "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",
        "GOOGLE_REFRESH_TOKEN": "1//0etoie1pPjEPgCgYIARAAGA4SNgF-L9IrDzekpQWMlaoX46E1ga3TKbce6N6bufXxXGDAmgPt5Yu4P7YK_cGG2NddXJV83wob3Q"
      }
    }
  }
}
```

## 🎯 利用可能なMCPツール

### Google Slides
- `create_presentation` - 新しいプレゼンテーションを作成
- `get_presentation` - プレゼンテーション情報を取得
- `batch_update_presentation` - スライドを一括更新

### Google Sheets
- `create_spreadsheet` - スプレッドシート作成
- `add_rows` - 行を追加
- `update_cells` - セルを更新
- その他多数

### Google Docs
- ドキュメント操作ツール

## 📚 認証スコープ

以下のスコープで認証済み:
- `https://www.googleapis.com/auth/spreadsheets` - Google Sheets
- `https://www.googleapis.com/auth/drive.file` - Google Drive
- `https://www.googleapis.com/auth/presentations` - Google Slides

## 🔄 Claude Codeの再起動

設定を反映するには、**Claude Codeを再起動**してください。

## 🧪 動作確認方法

Claude Codeを再起動後、以下のコマンドで確認できます:

```
「Google Slidesで新しいプレゼンテーションを作成して」
```

## 📖 参考リンク

- **Google Slides MCP GitHub:** https://github.com/matteoantoci/google-slides-mcp
- **Google Sheets MCP GitHub:** https://github.com/xing5/mcp-google-sheets

## ⚠️ 注意事項

1. **Google Cloud Console設定**
   - Google Slides APIが有効になっている必要があります
   - テストユーザーに自分のメールアドレスを追加済み

2. **トークンの有効期限**
   - Refresh Tokenは期限切れになることがあります
   - その場合は `get_slides_token.py` を再実行

3. **セキュリティ**
   - Client SecretとRefresh Tokenは機密情報です
   - GitHubなどに公開しないでください

## 🎉 完了！

これで以下が使えるようになりました:
- ✅ Google Sheets - スプレッドシート作成・編集
- ✅ Google Slides - プレゼンテーション作成・編集
- ✅ Google Docs - ドキュメント操作

Claude Codeを再起動して、MCPツールを使ってみましょう！
