#!/usr/bin/env python3
"""
ベトナム語列（H列）に画面ごとの背景色を適用
"""
import pickle
from pathlib import Path
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# 設定
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
CREDENTIALS_DIR = Path.home() / '.config' / 'mcp-google-sheets'
TOKEN_FILE = CREDENTIALS_DIR / 'token_with_slides.pickle'
SPREADSHEET_ID = '1kFiKmfiCv63hDxW0oR02U9CypiL-tOYgf_Hs7c_mxqg'

# 画面ごとの色設定（同じ色を使用）
SCREEN_COLORS = {
    'スプラッシュ画面': {'red': 1.0, 'green': 0.9, 'blue': 0.9},
    'ログイン画面': {'red': 1.0, 'green': 0.95, 'blue': 0.9},
    '初回チュートリアル': {'red': 1.0, 'green': 1.0, 'blue': 0.9},
    'ホーム画面': {'red': 0.9, 'green': 1.0, 'blue': 0.9},
    'レポート画面': {'red': 0.9, 'green': 0.95, 'blue': 1.0},
    '入館証画面': {'red': 0.95, 'green': 0.9, 'blue': 1.0},
    'リワード画面': {'red': 1.0, 'green': 0.9, 'blue': 0.95},
    'メニュー画面': {'red': 0.95, 'green': 1.0, 'blue': 0.95},
    '混雑状況確認画面': {'red': 1.0, 'green': 0.95, 'blue': 0.95},
    '動画トレーニング画面': {'red': 0.95, 'green': 0.95, 'blue': 1.0},
    '運動記録入力画面': {'red': 0.9, 'green': 1.0, 'blue': 1.0},
    'お知らせ一覧画面': {'red': 1.0, 'green': 1.0, 'blue': 0.95},
    'お知らせ詳細画面': {'red': 1.0, 'green': 0.98, 'blue': 0.9},
    'FAQ・コラム画面': {'red': 0.95, 'green': 0.95, 'blue': 0.95},
    'DNA検査結果画面': {'red': 0.9, 'green': 1.0, 'blue': 0.95},
    '通知設定画面': {'red': 1.0, 'green': 0.9, 'blue': 1.0},
    '設定画面': {'red': 0.98, 'green': 0.98, 'blue': 1.0},
    'PIXFORMANCE連携': {'red': 0.95, 'green': 1.0, 'blue': 0.9},
    'TANITA連携': {'red': 0.9, 'green': 0.95, 'blue': 1.0},
    'SECOM連携': {'red': 1.0, 'green': 0.95, 'blue': 1.0},
    'YouTube連携': {'red': 1.0, 'green': 0.9, 'blue': 0.9},
    'DNA検査サービス連携': {'red': 0.9, 'green': 1.0, 'blue': 0.9},
    'Apple Health連携': {'red': 0.95, 'green': 0.95, 'blue': 0.95},
    'Google Fit連携': {'red': 1.0, 'green': 1.0, 'blue': 0.9},
    'AIチャットボット': {'red': 0.9, 'green': 0.9, 'blue': 1.0},
    'ウェアラブル連携': {'red': 1.0, 'green': 0.95, 'blue': 0.9},
    'ポイントシステム': {'red': 1.0, 'green': 1.0, 'blue': 0.95},
    'コミュニティ機能': {'red': 0.95, 'green': 1.0, 'blue': 1.0},
    'データエクスポート': {'red': 0.95, 'green': 0.9, 'blue': 0.95},
}

def get_credentials():
    """認証情報を取得"""
    with open(TOKEN_FILE, 'rb') as token:
        creds = pickle.load(token)

    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
        with open(TOKEN_FILE, 'wb') as token:
            pickle.dump(creds, token)

    return creds

def colorize_vietnamese():
    """ベトナム語列に背景色を適用"""
    try:
        print("認証中...")
        creds = get_credentials()
        service = build('sheets', 'v4', credentials=creds)

        # シートIDを取得
        print("\nシート情報を取得中...")
        spreadsheet = service.spreadsheets().get(spreadsheetId=SPREADSHEET_ID).execute()
        sheets = spreadsheet.get('sheets', [])
        sheet_id = sheets[0]['properties']['sheetId']

        # データを取得して画面ごとにグループ化
        print("データを取得中...")
        result = service.spreadsheets().values().get(
            spreadsheetId=SPREADSHEET_ID,
            range='機能一覧!A:B'
        ).execute()
        values = result.get('values', [])

        # 画面ごとに行をグループ化
        screen_rows = {}
        current_screen = None

        for i, row in enumerate(values):
            if i == 0:  # ヘッダー行はスキップ
                continue

            if len(row) >= 2:
                screen_name = row[1]  # B列（画面名）
                if screen_name:
                    current_screen = screen_name
                    if screen_name not in screen_rows:
                        screen_rows[screen_name] = []
                    screen_rows[screen_name].append(i)
                elif current_screen:
                    screen_rows[current_screen].append(i)

        print(f"\n検出された画面数: {len(screen_rows)}")

        # H列（ベトナム語列）に色を適用
        requests = []

        for screen_name, row_indices in screen_rows.items():
            if screen_name in SCREEN_COLORS:
                color = SCREEN_COLORS[screen_name]

                if row_indices:
                    start_row = min(row_indices)
                    end_row = max(row_indices) + 1

                    requests.append({
                        'repeatCell': {
                            'range': {
                                'sheetId': sheet_id,
                                'startRowIndex': start_row,
                                'endRowIndex': end_row,
                                'startColumnIndex': 7,  # H列
                                'endColumnIndex': 8
                            },
                            'cell': {
                                'userEnteredFormat': {
                                    'backgroundColor': color
                                }
                            },
                            'fields': 'userEnteredFormat.backgroundColor'
                        }
                    })

                    print(f"  {screen_name}: 行 {start_row+1}-{end_row} ({len(row_indices)}項目)")

        # バッチ更新を実行
        if requests:
            print(f"\n色設定を適用中... ({len(requests)}画面)")
            service.spreadsheets().batchUpdate(
                spreadsheetId=SPREADSHEET_ID,
                body={'requests': requests}
            ).execute()

            print("✅ 色設定完了!")
        else:
            print("⚠️ 適用する色設定がありません")

        spreadsheet_url = f"https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}"
        print(f"\n{'='*60}")
        print(f"🎨 ベトナム語列の背景色設定完了!")
        print(f"{'='*60}")
        print(f"\n📊 スプレッドシートURL:")
        print(f"   {spreadsheet_url}")
        print(f"\n✅ {len(screen_rows)}個の画面にH列の色を適用しました")
        print(f"   （A-G列と同じ背景色）")

        return spreadsheet_url

    except HttpError as error:
        print(f"❌ Google API エラー: {error}")
        import traceback
        traceback.print_exc()
    except Exception as e:
        print(f"❌ エラー: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    colorize_vietnamese()
