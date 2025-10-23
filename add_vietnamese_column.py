#!/usr/bin/env python3
"""
スプレッドシートにベトナム語列を追加
"""
import pickle
from pathlib import Path
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# 設定
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
CREDENTIALS_DIR = Path.home() / '.config' / 'mcp-google-sheets'
TOKEN_FILE = CREDENTIALS_DIR / 'token_with_slides.pickle'
SPREADSHEET_ID = '1kFiKmfiCv63hDxW0oR02U9CypiL-tOYgf_Hs7c_mxqg'

# 主要な用語のベトナム語翻訳
TRANSLATIONS = {
    # カテゴリ
    '認証・オンボーディング': 'Xác thực & Hướng dẫn',
    'メイン機能': 'Chức năng chính',
    'サブ機能': 'Chức năng phụ',
    '外部連携': 'Liên kết ngoài',
    '将来構想': 'Kế hoạch tương lai',

    # 画面名
    'スプラッシュ画面': 'Màn hình khởi động',
    'ログイン画面': 'Màn hình đăng nhập',
    '初回チュートリアル': 'Hướng dẫn lần đầu',
    'ホーム画面': 'Màn hình chính',
    'レポート画面': 'Màn hình báo cáo',
    '入館証画面': 'Màn hình thẻ vào',
    'リワード画面': 'Màn hình phần thưởng',
    'メニュー画面': 'Màn hình menu',
    '混雑状況確認画面': 'Màn hình kiểm tra mật độ',
    '動画トレーニング画面': 'Màn hình video tập luyện',
    '運動記録入力画面': 'Màn hình nhập bản ghi',
    'お知らせ一覧画面': 'Màn hình thông báo',
    'お知らせ詳細画面': 'Màn hình chi tiết thông báo',
    'FAQ・コラム画面': 'Màn hình FAQ/Bài viết',
    'DNA検査結果画面': 'Màn hình kết quả DNA',
    '通知設定画面': 'Màn hình cài đặt thông báo',
    '設定画面': 'Màn hình cài đặt',
    'PIXFORMANCE連携': 'Liên kết PIXFORMANCE',
    'TANITA連携': 'Liên kết TANITA',
    'SECOM連携': 'Liên kết SECOM',
    'YouTube連携': 'Liên kết YouTube',
    'DNA検査サービス連携': 'Liên kết dịch vụ DNA',
    'Apple Health連携': 'Liên kết Apple Health',
    'Google Fit連携': 'Liên kết Google Fit',
    'AIチャットボット': 'Chatbot AI',
    'ウェアラブル連携': 'Liên kết thiết bị đeo',
    'ポイントシステム': 'Hệ thống điểm',
    'コミュニティ機能': 'Chức năng cộng đồng',
    'データエクスポート': 'Xuất dữ liệu',

    # 機能名
    'アプリ起動': 'Khởi động ứng dụng',
    'メール・パスワード認証': 'Xác thực Email/Mật khẩu',
    'ソーシャルログイン': 'Đăng nhập mạng xã hội',
    '使い方ガイド': 'Hướng dẫn sử dụng',
    '時間帯別挨拶': 'Lời chào theo thời gian',
    '今日のチャレンジ': 'Thử thách hôm nay',
    '来店サマリ': 'Tóm tắt lượt đến',
    '混雑状況クイックビュー': 'Xem nhanh tình trạng đông',
    '健康データサマリ': 'Tóm tắt dữ liệu sức khỏe',
    'クイックアクション': 'Thao tác nhanh',
    '週次サマリー': 'Tóm tắt tuần',
    '運動記録タブ': 'Tab ghi chép tập luyện',
    '体組成タブ': 'Tab thành phần cơ thể',
    '来館履歴タブ': 'Tab lịch sử đến',
    'CSVエクスポート': 'Xuất CSV',
    'QRコード表示': 'Hiển thị mã QR',
    '会員情報表示': 'Hiển thị thông tin thành viên',
    '店舗選択': 'Chọn cửa hàng',
    'オフライン対応': 'Hỗ trợ offline',
    '週間・月間チャレンジ': 'Thử thách tuần/tháng',
    'マイバッジ': 'Huy hiệu của tôi',
    '実績': 'Thành tích',
    'バッジ獲得アニメーション': 'Hiệu ứng nhận huy hiệu',
    'プロフィール管理': 'Quản lý hồ sơ',
    '利用ガイド': 'Hướng dẫn sử dụng',
    '設定メニュー': 'Menu cài đặt',
    'ログアウト': 'Đăng xuất',
    'リアルタイム混雑度': 'Mật độ thời gian thực',
    '1日の混雑予測': 'Dự đoán mật độ trong ngày',
    '曜日別傾向': 'Xu hướng theo ngày',
    '空き通知': 'Thông báo còn chỗ',
    'カテゴリ別表示': 'Hiển thị theo danh mục',
    '動画再生': 'Phát video',
    '視聴履歴管理': 'Quản lý lịch sử xem',
    '運動記録自動反映': 'Tự động ghi nhận tập luyện',
    'お気に入り登録': 'Đăng ký yêu thích',
    '手動記録追加': 'Thêm ghi chép thủ công',
    '運動種目選択': 'Chọn loại bài tập',
    '強度設定': 'Cài đặt cường độ',
    '消費カロリー計算': 'Tính calorie tiêu hao',
    '未読・既読管理': 'Quản lý đã đọc/chưa đọc',
    '検索機能': 'Chức năng tìm kiếm',
    '詳細表示': 'Hiển thị chi tiết',
    '画像・リンク埋め込み': 'Nhúng hình ảnh/liên kết',
    'シェア機能': 'Chức năng chia sẻ',
    'FAQ検索': 'Tìm kiếm FAQ',
    'アコーディオン表示': 'Hiển thị accordion',
    'コラム記事': 'Bài viết cột',
    '総合評価タブ': 'Tab đánh giá tổng hợp',
    '筋肉タイプタブ': 'Tab loại cơ bắp',
    '代謝タブ': 'Tab trao đổi chất',
    '怪我リスクタブ': 'Tab nguy cơ chấn thương',
    '詳細データタブ': 'Tab dữ liệu chi tiết',
    '外部サービス連携': 'Liên kết dịch vụ ngoài',
    '通知ON/OFF': 'Bật/Tắt thông báo',
    'カテゴリ別設定': 'Cài đặt theo danh mục',
    '通知時間帯設定': 'Cài đặt giờ thông báo',
    'プレビュー送信': 'Gửi xem trước',
    'ホーム画面カスタマイズ': 'Tùy chỉnh màn hình chính',
    '目標設定': 'Cài đặt mục tiêu',
    '単位設定': 'Cài đặt đơn vị',
    'テーマ設定': 'Cài đặt giao diện',
    'データ連携管理': 'Quản lý liên kết dữ liệu',
    'ヘルスケア連携': 'Liên kết chăm sóc sức khỏe',
    'AIマシンデータ取得': 'Lấy dữ liệu máy AI',
    '体組成データ取得': 'Lấy dữ liệu thành phần cơ thể',
    '入退館データ取得': 'Lấy dữ liệu vào/ra',
    '動画コンテンツ配信': 'Phân phối nội dung video',
    '遺伝子データ取得': 'Lấy dữ liệu gen',
    'ヘルスデータ同期': 'Đồng bộ dữ liệu sức khỏe',
    'フィットネスデータ同期': 'Đồng bộ dữ liệu thể dục',
    '自動応答': 'Trả lời tự động',
    'デバイス連携': 'Liên kết thiết bị',
    'ポイント付与・利用': 'Tích/Sử dụng điểm',
    'ユーザー間交流': 'Giao lưu người dùng',
    '全データ出力': 'Xuất toàn bộ dữ liệu',

    # 優先度
    'Phase 1': 'Giai đoạn 1',
    'Phase 2': 'Giai đoạn 2',
    'Phase 3': 'Giai đoạn 3',

    # 実装状況
    '未実装': 'Chưa thực hiện',
    '実装済み': 'Đã hoàn thành'
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

def add_vietnamese_column():
    """ベトナム語列を追加"""
    try:
        print("認証中...")
        creds = get_credentials()
        service = build('sheets', 'v4', credentials=creds)

        # 既存データを取得
        print("\n既存データを取得中...")
        result = service.spreadsheets().values().get(
            spreadsheetId=SPREADSHEET_ID,
            range='機能一覧!A:G'
        ).execute()
        values = result.get('values', [])

        print(f"データ行数: {len(values)}")

        # ベトナム語列のデータを準備
        vietnamese_data = []

        for i, row in enumerate(values):
            if i == 0:
                # ヘッダー行
                vietnamese_data.append(['Vietnamese / Tiếng Việt'])
            else:
                # データ行 - 各列の内容をベトナム語に翻訳
                if len(row) >= 3:
                    # カテゴリ、画面名、機能名を組み合わせて翻訳
                    category = row[0] if len(row) > 0 else ''
                    screen = row[1] if len(row) > 1 else ''
                    function = row[2] if len(row) > 2 else ''

                    # 翻訳を作成
                    parts = []
                    if function:
                        parts.append(TRANSLATIONS.get(function, function))

                    vietnamese_text = ' - '.join(parts) if parts else ''
                    vietnamese_data.append([vietnamese_text])
                else:
                    vietnamese_data.append([''])

        # H列にベトナム語データを追加
        print(f"\nベトナム語列を追加中... ({len(vietnamese_data)}行)")
        service.spreadsheets().values().update(
            spreadsheetId=SPREADSHEET_ID,
            range='機能一覧!H1',
            valueInputOption='RAW',
            body={'values': vietnamese_data}
        ).execute()

        print("✅ ベトナム語列追加完了!")

        # ヘッダー行のフォーマットを更新
        print("\nヘッダーのフォーマットを更新中...")

        # シートIDを取得
        spreadsheet = service.spreadsheets().get(spreadsheetId=SPREADSHEET_ID).execute()
        sheets = spreadsheet.get('sheets', [])
        sheet_id = sheets[0]['properties']['sheetId']

        requests = [
            # H列のヘッダーにフォーマットを適用
            {
                'repeatCell': {
                    'range': {
                        'sheetId': sheet_id,
                        'startRowIndex': 0,
                        'endRowIndex': 1,
                        'startColumnIndex': 7,
                        'endColumnIndex': 8
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
                                'bold': True,
                                'fontSize': 11
                            },
                            'horizontalAlignment': 'CENTER'
                        }
                    },
                    'fields': 'userEnteredFormat(backgroundColor,textFormat,horizontalAlignment)'
                }
            },
            # H列の幅を自動調整
            {
                'autoResizeDimensions': {
                    'dimensions': {
                        'sheetId': sheet_id,
                        'dimension': 'COLUMNS',
                        'startIndex': 7,
                        'endIndex': 8
                    }
                }
            }
        ]

        service.spreadsheets().batchUpdate(
            spreadsheetId=SPREADSHEET_ID,
            body={'requests': requests}
        ).execute()

        print("✅ フォーマット更新完了!")

        spreadsheet_url = f"https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}"
        print(f"\n{'='*60}")
        print(f"🎉 ベトナム語列追加完了!")
        print(f"{'='*60}")
        print(f"\n📊 スプレッドシートURL:")
        print(f"   {spreadsheet_url}")
        print(f"\n🇻🇳 追加内容:")
        print(f"   - H列: Vietnamese / Tiếng Việt")
        print(f"   - 翻訳済み機能: {len([k for k in TRANSLATIONS if k not in ['Phase 1', 'Phase 2', 'Phase 3', '未実装', '実装済み']])}項目")

        return spreadsheet_url

    except HttpError as error:
        print(f"❌ Google API エラー: {error}")
        import traceback
        traceback.print_exc()
    except Exception as e:
        print(f"❌ エラー: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    add_vietnamese_column()
