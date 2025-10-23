#!/usr/bin/env python3
"""
Google Sheets APIを直接使用してスプレッドシートを作成
OAuth 2.0 認証を使用
"""
import os
import csv
import pickle
from pathlib import Path
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# 設定
SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive.file']
CREDENTIALS_DIR = Path.home() / '.config' / 'mcp-google-sheets'
CLIENT_SECRET_FILE = CREDENTIALS_DIR / 'client_secret_109341072757-l9b2620gt4okkll64qolreb45iurtcjl.apps.googleusercontent.com.json'
TOKEN_FILE = CREDENTIALS_DIR / 'token.pickle'
CSV_PATH = '/Volumes/KIOXIA/Developments/withAI/Vercel/Furdi/MyFURDI/HiranoMyFurdi/MyFurdi_機能一覧表.csv'

def get_credentials():
    """OAuth 2.0認証を取得"""
    creds = None

    # トークンファイルが存在する場合は読み込み
    if TOKEN_FILE.exists():
        with open(TOKEN_FILE, 'rb') as token:
            creds = pickle.load(token)

    # 認証情報が無効または存在しない場合
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            print("トークンをリフレッシュ中...")
            creds.refresh(Request())
        else:
            print("新規認証を開始...")
            flow = InstalledAppFlow.from_client_secrets_file(
                str(CLIENT_SECRET_FILE), SCOPES)
            creds = flow.run_local_server(port=0)

        # トークンを保存
        with open(TOKEN_FILE, 'wb') as token:
            pickle.dump(creds, token)
        print("認証トークンを保存しました")

    return creds

def create_spreadsheet_with_data():
    """スプレッドシートを作成してデータを挿入"""
    try:
        # 認証
        print("認証中...")
        creds = get_credentials()

        # Sheets API サービスを構築
        service = build('sheets', 'v4', credentials=creds)

        # CSVファイルを読み込み
        print(f"\nCSVファイルを読み込み中: {CSV_PATH}")
        with open(CSV_PATH, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            data = list(reader)

        print(f"データ行数: {len(data)}")

        # スプレッドシートを作成
        print("\nスプレッドシートを作成中...")
        spreadsheet = {
            'properties': {
                'title': 'MyFurdi 機能一覧表'
            },
            'sheets': [{
                'properties': {
                    'title': '機能一覧',
                    'gridProperties': {
                        'frozenRowCount': 1  # ヘッダー行を固定
                    }
                }
            }]
        }

        result = service.spreadsheets().create(body=spreadsheet).execute()
        spreadsheet_id = result['spreadsheetId']
        spreadsheet_url = f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}"

        print(f"✅ スプレッドシート作成成功!")
        print(f"   ID: {spreadsheet_id}")
        print(f"   URL: {spreadsheet_url}")

        # データを挿入
        print(f"\nデータを挿入中... ({len(data)}行)")
        body = {
            'values': data
        }

        service.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id,
            range='機能一覧!A1',
            valueInputOption='RAW',
            body=body
        ).execute()

        print("✅ データ挿入完了!")

        # ヘッダー行のフォーマット設定（FURDIピンク背景）
        print("\nフォーマット設定中...")
        requests = [
            # ヘッダー行の背景色とテキスト色
            {
                'repeatCell': {
                    'range': {
                        'sheetId': 0,
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
            # 列幅を自動調整
            {
                'autoResizeDimensions': {
                    'dimensions': {
                        'sheetId': 0,
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
                            'sheetId': 0,
                            'startRowIndex': 0,
                            'endRowIndex': len(data)
                        }
                    }
                }
            }
        ]

        service.spreadsheets().batchUpdate(
            spreadsheetId=spreadsheet_id,
            body={'requests': requests}
        ).execute()

        print("✅ フォーマット設定完了!")
        print(f"\n{'='*60}")
        print(f"🎉 MyFurdi 機能一覧表が作成されました!")
        print(f"{'='*60}")
        print(f"\n📊 スプレッドシートURL:")
        print(f"   {spreadsheet_url}")
        print(f"\n📈 統計:")
        print(f"   - 総機能数: {len(data)-1}項目")
        print(f"   - カラム数: {len(data[0])}列")
        print(f"   - ヘッダー行固定: ✅")
        print(f"   - フィルター機能: ✅")
        print(f"   - FURDI ブランドカラー: ✅")

        return spreadsheet_url

    except HttpError as error:
        print(f"❌ Google API エラー: {error}")
        return None
    except Exception as e:
        print(f"❌ エラー: {e}")
        import traceback
        traceback.print_exc()
        return None

if __name__ == '__main__':
    create_spreadsheet_with_data()
