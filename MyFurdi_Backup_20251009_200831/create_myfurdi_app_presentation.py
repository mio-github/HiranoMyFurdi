#!/usr/bin/env python3
"""
MyFurdiアプリ機能紹介プレゼンテーションを作成
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
            'title': 'MyFurdi アプリ機能紹介'
        }).execute()

        presentation_id = presentation['presentationId']
        print(f"✅ プレゼンテーション作成成功!")
        print(f"   ID: {presentation_id}")

        # スライド構成
        slide_titles = [
            'アプリ概要',
            'メイン機能：5つのタブ',
            'ホーム画面',
            'レポート画面',
            '入館証画面',
            'リワード画面',
            'メニュー画面',
            '混雑状況確認',
            '動画トレーニング',
            'DNA検査結果',
            '外部連携',
            '開発フェーズ'
        ]

        # スライドを追加
        print(f"\nスライドを追加中... ({len(slide_titles)}スライド)")
        requests = []

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

        if requests:
            service.presentations().batchUpdate(
                presentationId=presentation_id,
                body={'requests': requests}
            ).execute()
            print(f"✅ {len(requests)}スライドを追加しました")

        # コンテンツを追加
        add_content(service, presentation_id)

        presentation_url = f"https://docs.google.com/presentation/d/{presentation_id}"
        print(f"\n{'='*60}")
        print(f"🎉 MyFurdi アプリ機能紹介完成!")
        print(f"{'='*60}")
        print(f"\n📊 プレゼンテーションURL:")
        print(f"   {presentation_url}")
        print(f"\n📈 統計:")
        print(f"   - 総スライド数: {len(slide_titles)+1}スライド")
        print(f"   - カバー範囲: 全19画面・82機能")

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

    # プレゼンテーション構造を取得
    presentation = service.presentations().get(
        presentationId=presentation_id
    ).execute()

    slides = presentation.get('slides', [])

    # スライド内容の定義
    slide_contents = [
        {
            'title': 'MyFurdi\nフィットネスアプリ',
            'body': 'FURDI会員向け\nトータルフィットネスサポートアプリ\n\n全19画面 / 82機能'
        },
        {
            'title': 'アプリ概要',
            'body': '【対象ユーザー】\nFURDI会員（女性専用フィットネスジム）\n\n【主な目的】\n• 来店前の混雑状況確認\n• トレーニング記録・体組成管理\n• モチベーション維持（ゲーミフィケーション）\n• 自宅でのトレーニングサポート\n• DNA検査結果に基づく最適化'
        },
        {
            'title': 'メイン機能：5つのタブ',
            'body': '📱 ボトムナビゲーション\n\n🏠 ホーム - ダッシュボード\n📊 レポート - 運動・体組成記録\n🎫 入館証 - QRコード表示\n🏆 リワード - バッジ・チャレンジ\n≡ メニュー - 設定・各種情報'
        },
        {
            'title': 'ホーム画面',
            'body': '【主要機能】\n✓ 時間帯別挨拶（パーソナライズ）\n✓ 今日のチャレンジ（低ハードル）\n✓ 来店サマリ（連続日数・週間目標）\n✓ 混雑状況クイックビュー\n✓ 健康データサマリ（体重・体脂肪・歩数）\n✓ クイックアクション（6機能）\n✓ 週次サマリー（前週比較）'
        },
        {
            'title': 'レポート画面',
            'body': '【3つのタブ】\n\n📈 運動記録\n• トレーニング履歴・グラフ\n• 運動種目別内訳\n• PIXFORMANCE連携\n\n⚖️ 体組成\n• 体重・体脂肪率推移\n• BMI、筋肉量、内臓脂肪\n• TANITA自動連携\n\n📅 来館履歴\n• カレンダービュー\n• 入退館時刻・滞在時間\n• SECOM連携'
        },
        {
            'title': '入館証画面',
            'body': '【QRコード表示】\n✓ ユーザー固有QRコード\n✓ 30秒ごと自動更新\n✓ 画面明るさ自動調整\n✓ オフライン対応（キャッシュ）\n\n【その他】\n• 会員ID・氏名・有効期限\n• 店舗選択・変更\n• 利用案内（初心者向け）'
        },
        {
            'title': 'リワード画面',
            'body': '【ゲーミフィケーション】\n\n🎯 今日のチャレンジ（日次）\n• 3-5個の低ハードルタスク\n• 達成時アニメーション\n\n📅 週間・月間チャレンジ\n• 継続的な目標設定\n\n🏅 マイバッジ（50種類）\n• 来店系、トレーニング系、ヘルス系\n• レア度設定（★-★★★★★）\n\n📊 実績\n• ランクシステム（5段階）\n• 累計データ表示'
        },
        {
            'title': 'メニュー画面',
            'body': '【利用ガイド】\n🎓 はじめての方へ\n📖 アプリの使い方\n💡 AIマシン・測定機器の使い方\n\n【コンテンツ】\n🎬 動画トレーニング一覧\n📰 お知らせ\n❓ FAQ\n📝 コラム\n\n【設定】\n⚙️ アプリ設定\n🔔 通知設定\n🧬 DNA検査結果\n🔗 外部連携'
        },
        {
            'title': '混雑状況確認',
            'body': '【リアルタイム情報】\n✓ 現在の混雑度（色・アイコン表示）\n  🟢 空いています (0-30%)\n  🟡 やや混雑 (31-60%)\n  🟠 混雑 (61-80%)\n  🔴 かなり混雑 (81-100%)\n\n✓ 1日の混雑予測グラフ\n✓ 曜日別傾向分析\n✓ おすすめ時間帯表示\n✓ 複数店舗対応'
        },
        {
            'title': '動画トレーニング',
            'body': '【自宅トレーニングサポート】\n\n📹 カテゴリ別動画\n• 初心者向け\n• 有酸素運動\n• 筋トレ\n• ストレッチ\n• ヨガ\n\n✓ YouTube埋め込みプレーヤー\n✓ 視聴履歴管理\n✓ 完了後の運動記録自動反映\n✓ お気に入り登録\n✓ 難易度・再生時間フィルタ'
        },
        {
            'title': 'DNA検査結果',
            'body': '【5つのタブ】\n\n🎯 総合評価\n• レーダーチャート（6軸）\n• 体質タイプ判定\n\n💪 筋肉タイプ\n• ACTN3遺伝子（速筋/遅筋）\n• ACE遺伝子（持久力）\n\n🔥 代謝\n• 基礎代謝傾向\n• 栄養素代謝（糖質/脂質/タンパク質）\n\n⚠️ 怪我リスク\n• 関節・腱リスク評価\n• 予防策提案\n\n📄 詳細データ（21項目）'
        },
        {
            'title': '外部連携',
            'body': '【既存連携】\n✓ PIXFORMANCE - AIマシン\n✓ TANITA - 体組成計\n✓ SECOM - 入退館管理\n✓ YouTube - 動画コンテンツ\n\n【Phase 2】\n→ DNA検査サービス（GeneQuest/MYCODE/ジーンライフ）\n→ Apple Health（iOS）\n→ Google Fit（Android）\n\n【Phase 3】\n→ ウェアラブルデバイス\n→ AIチャットボット'
        },
        {
            'title': '開発フェーズ',
            'body': '【Phase 1（初期リリース）】\n✓ 基本機能（ホーム、レポート、入館証、リワード、メニュー）\n✓ 混雑状況確認\n✓ プッシュ通知\n✓ 動画トレーニング\n\n【Phase 2（拡張機能）】\n✓ DNA検査結果画面 ← 実装済み\n→ リワード詳細（ランクシステム）\n→ データエクスポート\n\n【Phase 3（将来構想）】\n→ AIチャットボット\n→ ウェアラブル連携\n→ コミュニティ機能'
        }
    ]

    # 各スライドにコンテンツを追加
    content_requests = []

    for i, slide in enumerate(slides):
        if i >= len(slide_contents):
            break

        content = slide_contents[i]

        # スライド内のプレースホルダーを探す
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
            presentationId=presentation_id,
            body={'requests': content_requests}
        ).execute()
        print("✅ コンテンツ追加完了!")

if __name__ == '__main__':
    create_presentation()
