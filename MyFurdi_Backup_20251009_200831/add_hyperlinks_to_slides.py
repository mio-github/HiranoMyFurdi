#!/usr/bin/env python3
"""
スライドのテキストにハイパーリンクを追加
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

def add_hyperlinks():
    """URLにハイパーリンクを追加"""
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

        # 最後のスライド（ワイヤーフレーム一覧）を取得
        last_slide = slides[-1]
        slide_id = last_slide['objectId']

        print("\nハイパーリンクを追加中...")

        # スライド内のテキストボックスを探す
        requests = []

        for element in last_slide.get('pageElements', []):
            if 'shape' not in element:
                continue

            shape = element['shape']
            element_id = element['objectId']
            text_elements = shape.get('text', {}).get('textElements', [])

            # テキスト全体を結合
            full_text = ''
            current_index = 0

            for text_element in text_elements:
                if 'textRun' in text_element:
                    content = text_element['textRun'].get('content', '')
                    full_text += content

            # URLを探してハイパーリンクを追加
            if 'https://drive.google.com' in full_text:
                # 各URLの位置を特定
                urls = [
                    ('https://drive.google.com/file/d/1b2ki29XYiIV0jZeZniRJlr-jI2HVnDR9/view', '画面遷移図'),
                    ('https://drive.google.com/file/d/1dW7F9Sgb9ZRqcqvL58ArGDYMjeNh5i_4/view', 'ホーム画面'),
                    ('https://drive.google.com/file/d/1eai9Z5CDcZpebAR3L7L7oa_Qt0-hFv2y/view', 'レポート画面'),
                    ('https://drive.google.com/file/d/1KtQ3Bql3929tIQ8Y5qKlHGUmd_Itp-wz/view', '入館証画面'),
                    ('https://drive.google.com/file/d/1Ikj-_S8egfNGS2Ji_OtGemK5t4W6-oGe/view', 'リワード画面'),
                    ('https://drive.google.com/file/d/1-CD0LgcEFuI56Abk7RDEJJyxFS2pdXNh/view', 'メニュー画面'),
                    ('https://drive.google.com/file/d/1AoxB5AVKDGErYJAgzn2DYuaH2ZjcyonG/view', 'DNA検査結果画面')
                ]

                for url, title in urls:
                    start_index = full_text.find(url)
                    if start_index != -1:
                        end_index = start_index + len(url)

                        # ハイパーリンクを追加
                        requests.append({
                            'updateTextStyle': {
                                'objectId': element_id,
                                'textRange': {
                                    'type': 'FIXED_RANGE',
                                    'startIndex': start_index,
                                    'endIndex': end_index
                                },
                                'style': {
                                    'link': {
                                        'url': url
                                    },
                                    'foregroundColor': {
                                        'opaqueColor': {
                                            'rgbColor': {
                                                'red': 0.26,
                                                'green': 0.52,
                                                'blue': 0.96
                                            }
                                        }
                                    },
                                    'underline': True
                                },
                                'fields': 'link,foregroundColor,underline'
                            }
                        })

                        print(f"  ✅ {title}のリンクを追加")

        # バッチ更新を実行
        if requests:
            print(f"\nハイパーリンクを適用中... ({len(requests)}個)")
            service.presentations().batchUpdate(
                presentationId=PRESENTATION_ID,
                body={'requests': requests}
            ).execute()
            print("✅ ハイパーリンク追加完了!")
        else:
            print("⚠️ ハイパーリンクを追加できませんでした")

        presentation_url = f"https://docs.google.com/presentation/d/{PRESENTATION_ID}"
        print(f"\n{'='*60}")
        print(f"🎉 ハイパーリンク設定完了!")
        print(f"{'='*60}")
        print(f"\n📊 プレゼンテーションURL:")
        print(f"   {presentation_url}")
        print(f"\n💡 最後のスライドで、各URLをクリックして")
        print(f"   ワイヤーフレームを確認できます！")

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
    add_hyperlinks()
