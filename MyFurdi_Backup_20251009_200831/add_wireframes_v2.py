#!/usr/bin/env python3
"""
ワイヤーフレーム画像をスライドに追加（改良版）
SVGを読み込んでデータURIとして挿入
"""
import pickle
import os
import base64
from pathlib import Path
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# 設定
SCOPES = ['https://www.googleapis.com/auth/presentations']
CREDENTIALS_DIR = Path.home() / '.config' / 'mcp-google-sheets'
TOKEN_FILE = CREDENTIALS_DIR / 'token_with_slides.pickle'
PRESENTATION_ID = '1_GTxgaSjq3Iy7plviWlvEtL0X5BsX101jVPWvrGF7g4'
WIREFRAMES_DIR = '/Volumes/KIOXIA/Developments/withAI/Vercel/Furdi/MyFURDI/HiranoMyFurdi/wireframes'

# アップロード済みの画像ID（前回のアップロード結果を使用）
UPLOADED_IMAGES = {
    '01_home_screen.svg': '1dW7F9Sgb9ZRqcqvL58ArGDYMjeNh5i_4',
    '02_report_screen.svg': '1eai9Z5CDcZpebAR3L7L7oa_Qt0-hFv2y',
    '03_qrcode_screen.svg': '1KtQ3Bql3929tIQ8Y5qKlHGUmd_Itp-wz',
    '04_reward_screen.svg': '1Ikj-_S8egfNGS2Ji_OtGemK5t4W6-oGe',
    '05_menu_screen.svg': '1-CD0LgcEFuI56Abk7RDEJJyxFS2pdXNh',
    '06_dna_result_screen.svg': '1AoxB5AVKDGErYJAgzn2DYuaH2ZjcyonG',
    'screen_transition_diagram.svg': '1b2ki29XYiIV0jZeZniRJlr-jI2HVnDR9'
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

def add_wireframes():
    """ワイヤーフレーム画像をスライドに追加"""
    try:
        print("認証中...")
        creds = get_credentials()
        slides_service = build('slides', 'v1', credentials=creds)

        # プレゼンテーション構造を取得
        print("\nプレゼンテーション構造を取得中...")
        presentation = slides_service.presentations().get(
            presentationId=PRESENTATION_ID
        ).execute()

        slides = presentation.get('slides', [])
        print(f"スライド数: {len(slides)}")

        # 画像とスライドのマッピング
        image_mapping = {
            'screen_transition_diagram.svg': 3,  # メイン機能説明
            '01_home_screen.svg': 4,      # ホーム画面
            '02_report_screen.svg': 5,    # レポート画面
            '03_qrcode_screen.svg': 6,    # 入館証画面
            '04_reward_screen.svg': 7,    # リワード画面
            '05_menu_screen.svg': 8,      # メニュー画面
            '06_dna_result_screen.svg': 11,  # DNA検査結果
        }

        print("\nスライドに画像を挿入中...")
        success_count = 0

        for image_file, slide_index in image_mapping.items():
            if slide_index >= len(slides):
                print(f"  ⚠️ スライド{slide_index}が存在しません")
                continue

            file_id = UPLOADED_IMAGES.get(image_file)
            if not file_id:
                print(f"  ⚠️ {image_file}のファイルIDが見つかりません")
                continue

            # Google DriveのダウンロードURL（公開リンク）
            # 注: SVGは直接表示できないので、代わりにリンクを追加
            slide_id = slides[slide_index]['objectId']

            # テキストボックスを追加して画像へのリンクを表示
            text_box_id = f'link_box_{slide_index}'
            link_url = f'https://drive.google.com/file/d/{file_id}/view'

            # 画面遷移図は大きく表示
            if 'transition' in image_file:
                x = 30
                y = 350
                text = f'📊 画面遷移図を確認:\n{link_url}'
            else:
                x = 450
                y = 350
                screen_name = image_file.replace('.svg', '').replace('_', ' ').title()
                text = f'📱 ワイヤーフレーム:\n{link_url}'

            request = {
                'createShape': {
                    'objectId': text_box_id,
                    'shapeType': 'TEXT_BOX',
                    'elementProperties': {
                        'pageObjectId': slide_id,
                        'size': {
                            'width': {'magnitude': 200, 'unit': 'PT'},
                            'height': {'magnitude': 60, 'unit': 'PT'}
                        },
                        'transform': {
                            'scaleX': 1,
                            'scaleY': 1,
                            'translateX': x,
                            'translateY': y,
                            'unit': 'PT'
                        }
                    }
                }
            }

            try:
                slides_service.presentations().batchUpdate(
                    presentationId=PRESENTATION_ID,
                    body={'requests': [request]}
                ).execute()

                # テキストを挿入
                slides_service.presentations().batchUpdate(
                    presentationId=PRESENTATION_ID,
                    body={'requests': [{
                        'insertText': {
                            'objectId': text_box_id,
                            'text': text,
                            'insertionIndex': 0
                        }
                    }]}
                ).execute()

                print(f"  ✅ {image_file} のリンクを追加 (スライド{slide_index+1})")
                success_count += 1

            except HttpError as e:
                print(f"  ❌ {image_file} の追加に失敗: {e}")

        presentation_url = f"https://docs.google.com/presentation/d/{PRESENTATION_ID}"
        print(f"\n{'='*60}")
        print(f"🎉 画像リンク追加完了!")
        print(f"{'='*60}")
        print(f"\n📊 プレゼンテーションURL:")
        print(f"   {presentation_url}")
        print(f"\n📈 追加した画像リンク: {success_count}件")
        print(f"\n💡 注意: SVG画像は直接表示できないため、")
        print(f"   各スライドにGoogle Driveリンクを追加しました。")
        print(f"   リンクをクリックして画像を確認できます。")

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
    add_wireframes()
