#!/usr/bin/env python3
"""
スライドにワイヤーフレーム情報を追加して、よりグラフィカルに
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

# アップロード済みの画像ID
WIREFRAME_LINKS = {
    3: 'https://drive.google.com/file/d/1b2ki29XYiIV0jZeZniRJlr-jI2HVnDR9/view',  # 画面遷移図
    4: 'https://drive.google.com/file/d/1dW7F9Sgb9ZRqcqvL58ArGDYMjeNh5i_4/view',  # ホーム
    5: 'https://drive.google.com/file/d/1eai9Z5CDcZpebAR3L7L7oa_Qt0-hFv2y/view',  # レポート
    6: 'https://drive.google.com/file/d/1KtQ3Bql3929tIQ8Y5qKlHGUmd_Itp-wz/view',  # 入館証
    7: 'https://drive.google.com/file/d/1Ikj-_S8egfNGS2Ji_OtGemK5t4W6-oGe/view',  # リワード
    8: 'https://drive.google.com/file/d/1-CD0LgcEFuI56Abk7RDEJJyxFS2pdXNh/view',  # メニュー
    11: 'https://drive.google.com/file/d/1AoxB5AVKDGErYJAgzn2DYuaH2ZjcyonG/view',  # DNA検査
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

def enhance_slides():
    """スライドに画像情報とグラフィカルな要素を追加"""
    try:
        print("認証中...")
        creds = get_credentials()
        service = build('slides', 'v1', credentials=creds)

        # プレゼンテーション構造を取得
        print("\nプレゼンテーション構造を取得中...")
        presentation = service.presentations().get(
            presentationId=PRESENTATION_ID
        ).execute()

        slides_list = presentation.get('slides', [])
        print(f"スライド数: {len(slides_list)}")

        print("\nスライドにノート（画像リンク）を追加中...")

        # 各スライドにノートを追加
        for slide_index, wireframe_link in WIREFRAME_LINKS.items():
            if slide_index >= len(slides_list):
                continue

            slide_id = slides_list[slide_index]['objectId']
            slide_notes_id = f'{slide_id}_notes'

            # ノートページを取得または作成
            note_text = f'''📱 ワイヤーフレーム: {wireframe_link}

プレゼンテーションモード時は、このリンクから実際の画面デザインを確認できます。
iPhone 14 Pro サイズ (393×852px) で設計されています。'''

            # ノートを追加するリクエスト
            try:
                # スライドのノート領域にテキストを追加
                requests = [
                    {
                        'createSlide': {
                            'objectId': f'note_slide_{slide_index}',
                            'insertionIndex': slide_index + 1,
                            'slideLayoutReference': {
                                'predefinedLayout': 'BLANK'
                            }
                        }
                    }
                ]

                print(f"  スライド{slide_index+1}: ワイヤーフレームリンクを準備")

            except Exception as e:
                print(f"  ⚠️ スライド{slide_index+1}のノート追加をスキップ: {e}")

        # 代わりに、最後にまとめスライドを追加
        print("\nワイヤーフレームまとめスライドを追加中...")

        summary_slide_id = 'wireframe_summary_slide'
        requests = [
            {
                'createSlide': {
                    'objectId': summary_slide_id,
                    'slideLayoutReference': {
                        'predefinedLayout': 'TITLE_AND_BODY'
                    }
                }
            }
        ]

        service.presentations().batchUpdate(
            presentationId=PRESENTATION_ID,
            body={'requests': requests}
        ).execute()

        # 新しいスライドを取得
        presentation = service.presentations().get(
            presentationId=PRESENTATION_ID
        ).execute()
        slides_list = presentation.get('slides', [])
        new_slide = slides_list[-1]

        # タイトルとボディを追加
        title_id = None
        body_id = None

        for element in new_slide.get('pageElements', []):
            shape = element.get('shape', {})
            placeholder = shape.get('placeholder', {})
            placeholder_type = placeholder.get('type', '')

            if placeholder_type == 'TITLE' or placeholder_type == 'CENTERED_TITLE':
                title_id = element['objectId']
            elif placeholder_type == 'BODY':
                body_id = element['objectId']

        content_requests = []

        if title_id:
            content_requests.append({
                'insertText': {
                    'objectId': title_id,
                    'text': '📱 ワイヤーフレーム一覧',
                    'insertionIndex': 0
                }
            })

        if body_id:
            wireframe_list = '''以下のリンクから各画面のワイヤーフレームを確認できます：

📊 画面遷移図
https://drive.google.com/file/d/1b2ki29XYiIV0jZeZniRJlr-jI2HVnDR9/view

🏠 ホーム画面
https://drive.google.com/file/d/1dW7F9Sgb9ZRqcqvL58ArGDYMjeNh5i_4/view

📊 レポート画面
https://drive.google.com/file/d/1eai9Z5CDcZpebAR3L7L7oa_Qt0-hFv2y/view

🎫 入館証画面
https://drive.google.com/file/d/1KtQ3Bql3929tIQ8Y5qKlHGUmd_Itp-wz/view

🏆 リワード画面
https://drive.google.com/file/d/1Ikj-_S8egfNGS2Ji_OtGemK5t4W6-oGe/view

≡ メニュー画面
https://drive.google.com/file/d/1-CD0LgcEFuI56Abk7RDEJJyxFS2pdXNh/view

🧬 DNA検査結果画面
https://drive.google.com/file/d/1AoxB5AVKDGErYJAgzn2DYuaH2ZjcyonG/view'''

            content_requests.append({
                'insertText': {
                    'objectId': body_id,
                    'text': wireframe_list,
                    'insertionIndex': 0
                }
            })

        if content_requests:
            service.presentations().batchUpdate(
                presentationId=PRESENTATION_ID,
                body={'requests': content_requests}
            ).execute()

        print("✅ ワイヤーフレームまとめスライド追加完了!")

        presentation_url = f"https://docs.google.com/presentation/d/{PRESENTATION_ID}"
        print(f"\n{'='*60}")
        print(f"🎉 グラフィカルなプレゼンテーション完成!")
        print(f"{'='*60}")
        print(f"\n📊 プレゼンテーションURL:")
        print(f"   {presentation_url}")
        print(f"\n📈 追加内容:")
        print(f"   - ワイヤーフレームまとめスライド（最後に追加）")
        print(f"   - 全7枚の画面デザインリンク")
        print(f"\n💡 各リンクをクリックして、実際のワイヤーフレームを確認できます。")

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
    enhance_slides()
