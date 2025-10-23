#!/usr/bin/env python3
"""
Google Sheetsにスプレッドシートを作成し、CSVデータをインポートするスクリプト
"""
import csv
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# 認証情報のパス（ディレクトリ内のJSONファイルを探す）
CREDENTIALS_DIR = os.path.expanduser('~/.config/mcp-google-sheets/')
CSV_PATH = '/Volumes/KIOXIA/Developments/withAI/Vercel/Furdi/MyFURDI/HiranoMyFurdi/MyFurdi_機能一覧表.csv'

# Google Sheets APIのスコープ
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def create_spreadsheet_with_data():
    """スプレッドシートを作成してデータを挿入"""

    # 認証情報ファイルを探す
    json_files = [f for f in os.listdir(CREDENTIALS_DIR) if f.endswith('.json')]
    if not json_files:
        print("認証ファイルが見つかりません")
        return None

    credentials_path = os.path.join(CREDENTIALS_DIR, json_files[0])
    print(f"認証ファイル: {credentials_path}")

    # 認証（OAuth2クライアントシークレットの場合は別の方法を使用）
    # サービスアカウントではなく、OAuth2の場合
    from google_auth_oauthlib.flow import InstalledAppFlow
    from google.auth.transport.requests import Request
    import pickle

    creds = None
    token_path = os.path.join(CREDENTIALS_DIR, 'token.pickle')

    if os.path.exists(token_path):
        with open(token_path, 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
            creds = flow.run_local_server(port=0)

        with open(token_path, 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # CSVファイルを読み込み
    with open(CSV_PATH, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        data = list(reader)

    # スプレッドシート作成
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

    try:
        # スプレッドシート作成
        result = service.spreadsheets().create(body=spreadsheet).execute()
        spreadsheet_id = result['spreadsheetId']
        spreadsheet_url = f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}"

        print(f"スプレッドシート作成成功!")
        print(f"ID: {spreadsheet_id}")
        print(f"URL: {spreadsheet_url}")

        # データを挿入
        body = {
            'values': data
        }

        service.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id,
            range='機能一覧!A1',
            valueInputOption='RAW',
            body=body
        ).execute()

        print(f"\nデータ挿入完了: {len(data)}行")

        # ヘッダー行のフォーマット設定
        requests = [
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
                                'bold': True
                            }
                        }
                    },
                    'fields': 'userEnteredFormat(backgroundColor,textFormat)'
                }
            },
            {
                'autoResizeDimensions': {
                    'dimensions': {
                        'sheetId': 0,
                        'dimension': 'COLUMNS',
                        'startIndex': 0,
                        'endIndex': 7
                    }
                }
            }
        ]

        service.spreadsheets().batchUpdate(
            spreadsheetId=spreadsheet_id,
            body={'requests': requests}
        ).execute()

        print("フォーマット設定完了")
        print(f"\n✅ スプレッドシートURL: {spreadsheet_url}")

        return spreadsheet_url

    except HttpError as error:
        print(f"エラーが発生しました: {error}")
        return None

if __name__ == '__main__':
    create_spreadsheet_with_data()
