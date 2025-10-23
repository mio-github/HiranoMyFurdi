#!/usr/bin/env python3
"""
Google Slides API用のrefresh tokenを取得
"""
import pickle
from pathlib import Path
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# 設定
SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/presentations'  # Google Slides用スコープを追加
]
CREDENTIALS_DIR = Path.home() / '.config' / 'mcp-google-sheets'
CLIENT_SECRET_FILE = CREDENTIALS_DIR / 'client_secret_109341072757-l9b2620gt4okkll64qolreb45iurtcjl.apps.googleusercontent.com.json'
TOKEN_FILE = CREDENTIALS_DIR / 'token_with_slides.pickle'

def get_credentials():
    """新しいスコープで認証情報を取得"""
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
            print("Google Slides APIのスコープを含めて認証します")
            flow = InstalledAppFlow.from_client_secrets_file(
                str(CLIENT_SECRET_FILE), SCOPES)
            creds = flow.run_local_server(port=0)

        # トークンを保存
        with open(TOKEN_FILE, 'wb') as token:
            pickle.dump(creds, token)
        print(f"認証トークンを保存: {TOKEN_FILE}")

    print("\n" + "="*60)
    print("認証情報:")
    print("="*60)
    print(f"Client ID: {creds.client_id}")
    print(f"Client Secret: {creds.client_secret}")
    print(f"Refresh Token: {creds.refresh_token}")
    print(f"Scopes: {creds.scopes}")
    print("="*60)

    return creds

if __name__ == '__main__':
    get_credentials()
    print("\n✅ Google Slides用の認証情報を取得しました")
    print("この情報をClaude Code設定に使用できます")
