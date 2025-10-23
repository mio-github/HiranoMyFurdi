#!/usr/bin/env python3
"""
既存のプレゼンテーションにコンテンツを追加
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
PRESENTATION_ID = '1fAorvAQAb1wPQlwMKRa-hSxxWHS3fKAegeGSiWfsars'

def get_credentials():
    """認証情報を取得"""
    with open(TOKEN_FILE, 'rb') as token:
        creds = pickle.load(token)

    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
        with open(TOKEN_FILE, 'wb') as token:
            pickle.dump(creds, token)

    return creds

def add_content():
    """プレゼンテーションにコンテンツを追加"""
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
        print(f"既存スライド数: {len(slides)}")

        # 追加スライドを作成
        print("\nスライドを追加中...")
        slide_titles = [
            'プロジェクト概要',
            '開発成果',
            'MCP統合',
            'Google Sheets連携',
            'Google Slides連携',
            '技術スタック',
            '開発フロー',
            '今後の展開',
            'まとめ'
        ]

        requests = []

        # 新しいスライドを作成
        for i, title in enumerate(slide_titles):
            slide_id = f'slide_{i+2}'
            requests.append({
                'createSlide': {
                    'objectId': slide_id,
                    'slideLayoutReference': {
                        'predefinedLayout': 'TITLE_AND_BODY'
                    }
                }
            })

        # スライドを追加
        if requests:
            service.presentations().batchUpdate(
                presentationId=PRESENTATION_ID,
                body={'requests': requests}
            ).execute()
            print(f"✅ {len(requests)}スライドを追加しました")

        # 再度プレゼンテーション構造を取得
        presentation = service.presentations().get(
            presentationId=PRESENTATION_ID
        ).execute()

        slides = presentation.get('slides', [])
        print(f"現在のスライド数: {len(slides)}")

        # 各スライドのテキストボックスを探してコンテンツを追加
        content_requests = []

        # スライド内容の定義
        slide_contents = [
            {
                'title': 'MyFurdi × MCP\n自動化システム',
                'body': 'Model Context Protocolを活用した\nフィットネスアプリ開発の自動化'
            },
            {
                'title': 'プロジェクト概要',
                'body': 'MyFurdi - FURDI会員向けフィットネスアプリ\n\n✓ 全19画面の詳細設計\n✓ 6画面のワイヤーフレーム作成\n✓ インタラクティブなモックアプリ\n✓ 全82機能の一覧化\n✓ DNA検査結果画面の実装'
            },
            {
                'title': '開発成果',
                'body': '📦 成果物パッケージ\n\n• 設計ドキュメント（5ファイル）\n• ワイヤーフレーム（6画面 + 遷移図）\n• Reactモックアプリ（完全動作）\n• Figmaインポート用ファイル\n• Flutter実装例'
            },
            {
                'title': 'MCP統合',
                'body': 'Model Context Protocol活用\n\n🔧 統合済みMCPサーバー\n• Google Sheets MCP\n• Google Docs MCP\n• Google Slides MCP\n\n⚡ 自動化機能\n• スプレッドシート自動生成\n• プレゼンテーション作成\n• ドキュメント編集'
            },
            {
                'title': 'Google Sheets連携',
                'body': '📊 機能一覧表の自動生成\n\n✓ 全82機能を自動でスプレッドシート化\n✓ 29画面ごとに異なる背景色\n✓ FURDIブランドカラーのヘッダー\n✓ フィルター・ソート機能付き\n✓ CSV → Sheets 完全自動化'
            },
            {
                'title': 'Google Slides連携',
                'body': '🎨 プレゼンテーション自動作成\n\n• Google Slides API活用\n• 動的なコンテンツ生成\n• ブランドカラー適用\n• バッチ更新で高速処理\n• このプレゼンも自動生成！'
            },
            {
                'title': '技術スタック',
                'body': '💻 使用技術\n\n【フロントエンド】\nReact 18, TypeScript, Vite, Tailwind CSS\n\n【バックエンド・自動化】\nPython 3.13, Google APIs, MCP Servers\n\n【認証】\nOAuth 2.0, Service Account\n\n【ツール】\nuvx, Node.js, Git'
            },
            {
                'title': '開発フロー',
                'body': '🔄 自動化されたワークフロー\n\n1. 要件定義 → Markdown設計書\n2. 設計書 → CSV機能一覧\n3. CSV → Google Sheets (自動)\n4. 機能一覧 → 色分け (自動)\n5. システム情報 → Slides (自動)\n\n⏱️ 従来: 数時間 → 現在: 数分'
            },
            {
                'title': '今後の展開',
                'body': '🚀 Next Steps\n\nPhase 1（現在）\n✓ 基本設計完了\n✓ MCP統合完了\n\nPhase 2（進行中）\n→ Flutter実装開始\n→ API連携実装\n\nPhase 3（将来）\n→ AI機能統合\n→ 完全自動化'
            },
            {
                'title': 'まとめ',
                'body': '🎯 達成したこと\n\n• MCPによる開発自動化の実現\n• Google APIs完全統合\n• 82機能の体系的な管理\n• ドキュメント自動生成\n\n💡 得られた知見\n\n• AIとの協働開発の可能性\n• 自動化による生産性向上\n• モダンな開発フローの確立'
            }
        ]

        # 各スライドにコンテンツを追加
        print("\nコンテンツを追加中...")
        for i, slide in enumerate(slides):
            if i >= len(slide_contents):
                break

            slide_id = slide['objectId']
            content = slide_contents[i]

            # スライド内のテキストボックスを探す
            for element in slide.get('pageElements', []):
                shape = element.get('shape', {})
                placeholder = shape.get('placeholder', {})
                placeholder_type = placeholder.get('type', '')

                # タイトルプレースホルダー
                if placeholder_type == 'TITLE' or placeholder_type == 'CENTERED_TITLE':
                    element_id = element['objectId']
                    content_requests.append({
                        'insertText': {
                            'objectId': element_id,
                            'text': content['title'],
                            'insertionIndex': 0
                        }
                    })

                # ボディプレースホルダー
                elif placeholder_type == 'BODY' or placeholder_type == 'SUBTITLE':
                    element_id = element['objectId']
                    content_requests.append({
                        'insertText': {
                            'objectId': element_id,
                            'text': content['body'],
                            'insertionIndex': 0
                        }
                    })

        # バッチ更新
        if content_requests:
            print(f"テキストを挿入中... ({len(content_requests)}箇所)")
            service.presentations().batchUpdate(
                presentationId=PRESENTATION_ID,
                body={'requests': content_requests}
            ).execute()
            print("✅ コンテンツ追加完了!")

        presentation_url = f"https://docs.google.com/presentation/d/{PRESENTATION_ID}"
        print(f"\n{'='*60}")
        print(f"🎉 MyFurdi システム紹介プレゼンテーション完成!")
        print(f"{'='*60}")
        print(f"\n📊 プレゼンテーションURL:")
        print(f"   {presentation_url}")
        print(f"\n📈 統計:")
        print(f"   - 総スライド数: {len(slides)}スライド")
        print(f"   - コンテンツ: 完全自動生成")

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
    add_content()
