#!/usr/bin/env python3
"""
プレゼンテーションからMCP関連の記述を削除
"""
import pickle
from pathlib import Path
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# 設定
SCOPES = ['https://www.googleapis.com/auth/presentations']
CREDENTIALS_DIR = Path.home() / '.config' / 'mcp-google-sheets'
TOKEN_FILE = CREDENTIALS_DIR / 'token_with_slides.pickle'
PRESENTATION_ID = '1_GTxgaSjq3Iy7plviWlvEtL0X5BsX101jVPWvrGF7g4'

def get_credentials():
    """認証情報を取得"""
    with open(TOKEN_FILE, 'rb') as token:
        creds = pickle.load(token)

    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
        with open(TOKEN_FILE, 'wb') as token:
            pickle.dump(creds, token)

    return creds

def remove_mcp_content():
    """MCP関連の記述を削除"""
    try:
        print("認証中...")
        creds = get_credentials()
        service = build('slides', 'v1', credentials=creds)

        # プレゼンテーション構造を取得
        print("\nプレゼンテーション構造を取得中...")
        presentation = service.presentations().get(
            presentationId=PRESENTATION_ID
        ).execute()

        slides = presentation.get('slides', [])
        print(f"スライド数: {len(slides)}")

        # 各スライドのテキストを確認・更新
        delete_requests = []
        update_requests = []

        for slide in slides:
            slide_id = slide['objectId']

            for element in slide.get('pageElements', []):
                if 'shape' in element:
                    shape = element['shape']
                    text_elements = shape.get('text', {}).get('textElements', [])

                    # テキストを結合して確認
                    full_text = ''
                    for text_element in text_elements:
                        if 'textRun' in text_element:
                            full_text += text_element['textRun'].get('content', '')

                    # MCP関連のテキストが含まれているか確認
                    if 'MCP' in full_text or 'Model Context Protocol' in full_text:
                        element_id = element['objectId']

                        # テキストをクリアして新しいテキストに置き換え
                        delete_requests.append({
                            'deleteText': {
                                'objectId': element_id,
                                'textRange': {
                                    'type': 'ALL'
                                }
                            }
                        })

                        # タイトルの場合は修正
                        if 'MyFurdi × MCP' in full_text:
                            update_requests.append({
                                'insertText': {
                                    'objectId': element_id,
                                    'text': 'MyFurdi\nフィットネスアプリ',
                                    'insertionIndex': 0
                                }
                            })
                        elif 'Model Context Protocol' in full_text:
                            update_requests.append({
                                'insertText': {
                                    'objectId': element_id,
                                    'text': 'FURDI会員向け\nトータルフィットネスサポートアプリ\n\n全19画面 / 82機能',
                                    'insertionIndex': 0
                                }
                            })

        # バッチ更新を実行
        all_requests = delete_requests + update_requests

        if all_requests:
            print(f"\nMCP関連の記述を削除中... ({len(delete_requests)}箇所)")
            service.presentations().batchUpdate(
                presentationId=PRESENTATION_ID,
                body={'requests': all_requests}
            ).execute()
            print("✅ 削除・更新完了!")
        else:
            print("⚠️ MCP関連の記述が見つかりませんでした")

        presentation_url = f"https://docs.google.com/presentation/d/{PRESENTATION_ID}"
        print(f"\n{'='*60}")
        print(f"🎉 プレゼンテーション更新完了!")
        print(f"{'='*60}")
        print(f"\n📊 プレゼンテーションURL:")
        print(f"   {presentation_url}")

        return presentation_url

    except HttpError as error:
        print(f"❌ Google API エラー: {error}")
        import traceback
        traceback.print_exc()
    except Exception as e:
        print(f"❌ エラー: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    remove_mcp_content()
