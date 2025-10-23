#!/usr/bin/env python3
"""
MyFurdi × MCP システム紹介プレゼンテーションを作成
"""
import pickle
from pathlib import Path
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# 設定
SCOPES = ['https://www.googleapis.com/auth/presentations', 'https://www.googleapis.com/auth/drive.file']
CREDENTIALS_DIR = Path.home() / '.config' / 'mcp-google-sheets'
TOKEN_FILE = CREDENTIALS_DIR / 'token_with_slides.pickle'

# FURDIブランドカラー
FURDI_PINK = {'red': 1.0, 'green': 0.41, 'blue': 0.71}
FURDI_PINK_LIGHT = {'red': 1.0, 'green': 0.894, 'blue': 0.882}
WHITE = {'red': 1.0, 'green': 1.0, 'blue': 1.0}
DARK_GRAY = {'red': 0.11, 'green': 0.11, 'blue': 0.118}

def get_credentials():
    """認証情報を取得"""
    with open(TOKEN_FILE, 'rb') as token:
        creds = pickle.load(token)

    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
        with open(TOKEN_FILE, 'wb') as token:
            pickle.dump(creds, token)

    return creds

def create_presentation():
    """プレゼンテーションを作成"""
    try:
        print("認証中...")
        creds = get_credentials()
        service = build('slides', 'v1', credentials=creds)

        # プレゼンテーション作成
        print("\nプレゼンテーションを作成中...")
        presentation = service.presentations().create(body={
            'title': 'MyFurdi × MCP 自動化システム紹介'
        }).execute()

        presentation_id = presentation['presentationId']
        print(f"✅ プレゼンテーション作成成功!")
        print(f"   ID: {presentation_id}")

        # スライドを追加していく
        requests = []

        # デフォルトのスライドを取得
        slides = service.presentations().get(presentationId=presentation_id).execute()
        slide_ids = [slide['objectId'] for slide in slides.get('slides', [])]

        print(f"\nスライドを作成中... (10スライド)")

        # スライド1: タイトルスライド（既存のスライドを更新）
        if slide_ids:
            title_slide_id = slide_ids[0]
            requests.extend([
                # タイトルテキスト
                {
                    'insertText': {
                        'objectId': title_slide_id,
                        'text': 'MyFurdi × MCP\n自動化システム',
                        'insertionIndex': 0
                    }
                },
                # サブタイトル
                {
                    'createShape': {
                        'objectId': f'{title_slide_id}_subtitle',
                        'shapeType': 'TEXT_BOX',
                        'elementProperties': {
                            'pageObjectId': title_slide_id,
                            'size': {
                                'width': {'magnitude': 600, 'unit': 'PT'},
                                'height': {'magnitude': 80, 'unit': 'PT'}
                            },
                            'transform': {
                                'scaleX': 1,
                                'scaleY': 1,
                                'translateX': 60,
                                'translateY': 350,
                                'unit': 'PT'
                            }
                        }
                    }
                },
                {
                    'insertText': {
                        'objectId': f'{title_slide_id}_subtitle',
                        'text': 'Model Context Protocolを活用した\nフィットネスアプリ開発の自動化',
                        'insertionIndex': 0
                    }
                }
            ])

        # 追加スライドを作成
        slide_titles = [
            'プロジェクト概要',
            '開発成果',
            'MCP統合',
            'Google Sheets連携',
            'Google Slides連携',
            '技術スタック',
            '開発フロー',
            '今後の展開'
        ]

        for i, title in enumerate(slide_titles):
            slide_id = f'slide_{i+2}'
            requests.append({
                'createSlide': {
                    'objectId': slide_id,
                    'slideLayoutReference': {
                        'predefinedLayout': 'TITLE_AND_BODY'
                    },
                    'placeholderIdMappings': [
                        {
                            'layoutPlaceholder': {
                                'type': 'TITLE',
                                'index': 0
                            },
                            'objectId': f'{slide_id}_title'
                        },
                        {
                            'layoutPlaceholder': {
                                'type': 'BODY',
                                'index': 0
                            },
                            'objectId': f'{slide_id}_body'
                        }
                    ]
                }
            })

        # バッチ更新を実行
        print("\nスライドを生成中...")
        if requests:
            service.presentations().batchUpdate(
                presentationId=presentation_id,
                body={'requests': requests}
            ).execute()

        print("✅ スライド生成完了!")

        # コンテンツを追加
        add_content(service, presentation_id)

        presentation_url = f"https://docs.google.com/presentation/d/{presentation_id}"
        print(f"\n{'='*60}")
        print(f"🎉 MyFurdi システム紹介プレゼンテーション完成!")
        print(f"{'='*60}")
        print(f"\n📊 プレゼンテーションURL:")
        print(f"   {presentation_url}")
        print(f"\n📈 統計:")
        print(f"   - 総スライド数: 10スライド")
        print(f"   - カラー: FURDIブランドカラー (#FF69B4)")

        return presentation_url

    except HttpError as error:
        print(f"❌ Google API エラー: {error}")
        import traceback
        traceback.print_exc()
    except Exception as e:
        print(f"❌ エラー: {e}")
        import traceback
        traceback.print_exc()

def add_content(service, presentation_id):
    """各スライドにコンテンツを追加"""
    print("\nコンテンツを追加中...")

    # スライド2: プロジェクト概要
    content_requests = [
        {
            'insertText': {
                'objectId': 'slide_2_title',
                'text': 'プロジェクト概要',
                'insertionIndex': 0
            }
        },
        {
            'insertText': {
                'objectId': 'slide_2_body',
                'text': '''MyFurdi - FURDI会員向けフィットネスアプリ

✓ 全19画面の詳細設計
✓ 6画面のワイヤーフレーム作成
✓ インタラクティブなモックアプリ
✓ 全82機能の一覧化
✓ DNA検査結果画面の実装''',
                'insertionIndex': 0
            }
        },
        # スライド3: 開発成果
        {
            'insertText': {
                'objectId': 'slide_3_title',
                'text': '開発成果',
                'insertionIndex': 0
            }
        },
        {
            'insertText': {
                'objectId': 'slide_3_body',
                'text': '''📦 成果物パッケージ

• 設計ドキュメント（5ファイル）
• ワイヤーフレーム（6画面 + 遷移図）
• Reactモックアプリ（完全動作）
• Figmaインポート用ファイル
• Flutter実装例''',
                'insertionIndex': 0
            }
        },
        # スライド4: MCP統合
        {
            'insertText': {
                'objectId': 'slide_4_title',
                'text': 'MCP統合',
                'insertionIndex': 0
            }
        },
        {
            'insertText': {
                'objectId': 'slide_4_body',
                'text': '''Model Context Protocol活用

🔧 統合済みMCPサーバー
• Google Sheets MCP
• Google Docs MCP
• Google Slides MCP

⚡ 自動化機能
• スプレッドシート自動生成
• プレゼンテーション作成
• ドキュメント編集''',
                'insertionIndex': 0
            }
        },
        # スライド5: Google Sheets連携
        {
            'insertText': {
                'objectId': 'slide_5_title',
                'text': 'Google Sheets連携',
                'insertionIndex': 0
            }
        },
        {
            'insertText': {
                'objectId': 'slide_5_body',
                'text': '''📊 機能一覧表の自動生成

✓ 全82機能を自動でスプレッドシート化
✓ 29画面ごとに異なる背景色
✓ FURDIブランドカラーのヘッダー
✓ フィルター・ソート機能付き
✓ CSV → Sheets 完全自動化''',
                'insertionIndex': 0
            }
        },
        # スライド6: Google Slides連携
        {
            'insertText': {
                'objectId': 'slide_6_title',
                'text': 'Google Slides連携',
                'insertionIndex': 0
            }
        },
        {
            'insertText': {
                'objectId': 'slide_6_body',
                'text': '''🎨 プレゼンテーション自動作成

• Google Slides API活用
• 動的なコンテンツ生成
• ブランドカラー適用
• バッチ更新で高速処理
• このプレゼンも自動生成！''',
                'insertionIndex': 0
            }
        },
        # スライド7: 技術スタック
        {
            'insertText': {
                'objectId': 'slide_7_title',
                'text': '技術スタック',
                'insertionIndex': 0
            }
        },
        {
            'insertText': {
                'objectId': 'slide_7_body',
                'text': '''💻 使用技術

【フロントエンド】
React 18, TypeScript, Vite, Tailwind CSS

【バックエンド・自動化】
Python 3.13, Google APIs, MCP Servers

【認証】
OAuth 2.0, Service Account

【ツール】
uvx, Node.js, Git''',
                'insertionIndex': 0
            }
        },
        # スライド8: 開発フロー
        {
            'insertText': {
                'objectId': 'slide_8_title',
                'text': '開発フロー',
                'insertionIndex': 0
            }
        },
        {
            'insertText': {
                'objectId': 'slide_8_body',
                'text': '''🔄 自動化されたワークフロー

1. 要件定義 → Markdown設計書
2. 設計書 → CSV機能一覧
3. CSV → Google Sheets (自動)
4. 機能一覧 → 色分け (自動)
5. システム情報 → Slides (自動)

⏱️ 従来: 数時間 → 現在: 数分''',
                'insertionIndex': 0
            }
        },
        # スライド9: 今後の展開
        {
            'insertText': {
                'objectId': 'slide_9_title',
                'text': '今後の展開',
                'insertionIndex': 0
            }
        },
        {
            'insertText': {
                'objectId': 'slide_9_body',
                'text': '''🚀 Next Steps

Phase 1（現在）
✓ 基本設計完了
✓ MCP統合完了

Phase 2（進行中）
→ Flutter実装開始
→ API連携実装

Phase 3（将来）
→ AI機能統合
→ 完全自動化''',
                'insertionIndex': 0
            }
        }
    ]

    # バッチ更新
    if content_requests:
        service.presentations().batchUpdate(
            presentationId=presentation_id,
            body={'requests': content_requests}
        ).execute()

    print("✅ コンテンツ追加完了!")

if __name__ == '__main__':
    create_presentation()
