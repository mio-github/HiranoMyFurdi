#!/usr/bin/env python3
"""
既存のスプレッドシートにフォーマットを適用
"""
import pickle
from pathlib import Path
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# 設定
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
CREDENTIALS_DIR = Path.home() / '.config' / 'mcp-google-sheets'
TOKEN_FILE = CREDENTIALS_DIR / 'token.pickle'
SPREADSHEET_ID = '1kFiKmfiCv63hDxW0oR02U9CypiL-tOYgf_Hs7c_mxqg'

def get_credentials():
    """認証情報を取得"""
    with open(TOKEN_FILE, 'rb') as token:
        creds = pickle.load(token)

    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
        with open(TOKEN_FILE, 'wb') as token:
            pickle.dump(creds, token)

    return creds

def format_spreadsheet():
    """スプレッドシートにフォーマットを適用"""
    try:
        print("認証中...")
        creds = get_credentials()
        service = build('sheets', 'v4', credentials=creds)

        # シート情報を取得
        print("\nシート情報を取得中...")
        spreadsheet = service.spreadsheets().get(spreadsheetId=SPREADSHEET_ID).execute()
        sheets = spreadsheet.get('sheets', [])

        if not sheets:
            print("シートが見つかりません")
            return

        sheet_id = sheets[0]['properties']['sheetId']
        sheet_title = sheets[0]['properties']['title']
        print(f"シート名: {sheet_title}")
        print(f"シートID: {sheet_id}")

        # フォーマット設定
        print("\nフォーマット設定中...")
        requests = [
            # ヘッダー行の背景色とテキスト色（FURDIピンク）
            {
                'repeatCell': {
                    'range': {
                        'sheetId': sheet_id,
                        'startRowIndex': 0,
                        'endRowIndex': 1
                    },
                    'cell': {
                        'userEnteredFormat': {
                            'backgroundColor': {
                                'red': 1.0,
                                'green': 0.41,
                                'blue': 0.71
                            },
                            'textFormat': {
                                'foregroundColor': {
                                    'red': 1.0,
                                    'green': 1.0,
                                    'blue': 1.0
                                },
                                'bold': True,
                                'fontSize': 11
                            },
                            'horizontalAlignment': 'CENTER'
                        }
                    },
                    'fields': 'userEnteredFormat(backgroundColor,textFormat,horizontalAlignment)'
                }
            },
            # ヘッダー行を固定
            {
                'updateSheetProperties': {
                    'properties': {
                        'sheetId': sheet_id,
                        'gridProperties': {
                            'frozenRowCount': 1
                        }
                    },
                    'fields': 'gridProperties.frozenRowCount'
                }
            },
            # 列幅を自動調整
            {
                'autoResizeDimensions': {
                    'dimensions': {
                        'sheetId': sheet_id,
                        'dimension': 'COLUMNS',
                        'startIndex': 0,
                        'endIndex': 7
                    }
                }
            },
            # フィルタービューを追加
            {
                'setBasicFilter': {
                    'filter': {
                        'range': {
                            'sheetId': sheet_id,
                            'startRowIndex': 0,
                            'endRowIndex': 100  # データ行数に応じて調整
                        }
                    }
                }
            }
        ]

        service.spreadsheets().batchUpdate(
            spreadsheetId=SPREADSHEET_ID,
            body={'requests': requests}
        ).execute()

        print("✅ フォーマット設定完了!")
        print(f"\n{'='*60}")
        print(f"🎉 MyFurdi 機能一覧表のフォーマット完了!")
        print(f"{'='*60}")
        print(f"\n📊 スプレッドシートURL:")
        print(f"   https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}")
        print(f"\n✅ 適用されたフォーマット:")
        print(f"   - ヘッダー行固定")
        print(f"   - FURDIブランドカラー (#FF69B4)")
        print(f"   - 列幅自動調整")
        print(f"   - フィルター機能")

    except HttpError as error:
        print(f"❌ Google API エラー: {error}")
    except Exception as e:
        print(f"❌ エラー: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    format_spreadsheet()
