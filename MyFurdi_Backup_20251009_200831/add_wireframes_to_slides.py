#!/usr/bin/env python3
"""
ワイヤーフレーム画像をスライドに追加
"""
import pickle
import os
import base64
from pathlib import Path
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

# 設定
SCOPES = [
    'https://www.googleapis.com/auth/presentations',
    'https://www.googleapis.com/auth/drive.file'
]
CREDENTIALS_DIR = Path.home() / '.config' / 'mcp-google-sheets'
TOKEN_FILE = CREDENTIALS_DIR / 'token_with_slides.pickle'
PRESENTATION_ID = '1_GTxgaSjq3Iy7plviWlvEtL0X5BsX101jVPWvrGF7g4'
WIREFRAMES_DIR = '/Volumes/KIOXIA/Developments/withAI/Vercel/Furdi/MyFURDI/HiranoMyFurdi/wireframes'

def get_credentials():
    """認証情報を取得"""
    with open(TOKEN_FILE, 'rb') as token:
        creds = pickle.load(token)

    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
        with open(TOKEN_FILE, 'wb') as token:
            pickle.dump(creds, token)

    return creds

def upload_image_to_drive(drive_service, image_path):
    """画像をGoogle Driveにアップロード"""
    file_name = os.path.basename(image_path)

    file_metadata = {
        'name': file_name,
        'mimeType': 'image/svg+xml'
    }

    media = MediaFileUpload(
        image_path,
        mimetype='image/svg+xml',
        resumable=True
    )

    file = drive_service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id, webContentLink'
    ).execute()

    # ファイルを公開設定に
    drive_service.permissions().create(
        fileId=file['id'],
        body={'type': 'anyone', 'role': 'reader'}
    ).execute()

    # 公開URLを取得
    file_info = drive_service.files().get(
        fileId=file['id'],
        fields='webContentLink, webViewLink'
    ).execute()

    return file['id'], file_info.get('webContentLink')

def add_wireframes():
    """ワイヤーフレーム画像をスライドに追加"""
    try:
        print("認証中...")
        creds = get_credentials()
        slides_service = build('slides', 'v1', credentials=creds)
        drive_service = build('drive', 'v3', credentials=creds)

        # プレゼンテーション構造を取得
        print("\nプレゼンテーション構造を取得中...")
        presentation = slides_service.presentations().get(
            presentationId=PRESENTATION_ID
        ).execute()

        slides = presentation.get('slides', [])
        print(f"スライド数: {len(slides)}")

        # 画像とスライドのマッピング
        image_mapping = {
            '01_home_screen.svg': 4,      # ホーム画面
            '02_report_screen.svg': 5,    # レポート画面
            '03_qrcode_screen.svg': 6,    # 入館証画面
            '04_reward_screen.svg': 7,    # リワード画面
            '05_menu_screen.svg': 8,      # メニュー画面
            '06_dna_result_screen.svg': 11,  # DNA検査結果
            'screen_transition_diagram.svg': 3  # メイン機能説明
        }

        requests = []

        print("\n画像をアップロード中...")
        for image_file, slide_index in image_mapping.items():
            image_path = os.path.join(WIREFRAMES_DIR, image_file)

            if not os.path.exists(image_path):
                print(f"  ⚠️ ファイルが見つかりません: {image_file}")
                continue

            if slide_index >= len(slides):
                print(f"  ⚠️ スライド{slide_index}が存在しません")
                continue

            # Google Driveにアップロード
            print(f"  📤 {image_file} をアップロード中...")
            file_id, web_link = upload_image_to_drive(drive_service, image_path)
            print(f"     ✅ アップロード完了 (ID: {file_id})")

            # 画像URL（公開URL）
            image_url = f"https://drive.google.com/uc?export=view&id={file_id}"

            # スライドに画像を追加
            slide_id = slides[slide_index]['objectId']
            image_id = f'image_{slide_index}_{image_file.replace(".svg", "")}'

            # 画面遷移図は大きく表示
            if 'transition' in image_file:
                width = 500
                height = 460
                x = 30
                y = 100
            else:
                # ワイヤーフレームはiPhoneサイズ（右側に配置）
                width = 197  # 393px の半分
                height = 426  # 852px の半分
                x = 450  # 右側に配置
                y = 120

            requests.append({
                'createImage': {
                    'objectId': image_id,
                    'url': image_url,
                    'elementProperties': {
                        'pageObjectId': slide_id,
                        'size': {
                            'width': {'magnitude': width, 'unit': 'PT'},
                            'height': {'magnitude': height, 'unit': 'PT'}
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
            })

        # バッチ更新を実行
        if requests:
            print(f"\nスライドに画像を挿入中... ({len(requests)}枚)")
            slides_service.presentations().batchUpdate(
                presentationId=PRESENTATION_ID,
                body={'requests': requests}
            ).execute()
            print("✅ 画像挿入完了!")

        presentation_url = f"https://docs.google.com/presentation/d/{PRESENTATION_ID}"
        print(f"\n{'='*60}")
        print(f"🎉 グラフィカルなプレゼンテーション完成!")
        print(f"{'='*60}")
        print(f"\n📊 プレゼンテーションURL:")
        print(f"   {presentation_url}")
        print(f"\n📈 追加した画像:")
        print(f"   - ワイヤーフレーム: 6枚")
        print(f"   - 画面遷移図: 1枚")

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
