#!/usr/bin/env python3
"""
MyFurdiモックアップ画面のPDF生成スクリプト
"""

from PIL import Image
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.lib.utils import ImageReader
from pathlib import Path
import os
import json
import cairosvg
import tempfile

def load_config():
    """設定ファイルを読み込む"""
    config_path = Path("mockup-config.json")
    if config_path.exists():
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return None

def draw_wrapped_text(c, text, x, y, max_width, font_name, font_size, line_height=None):
    """テキストを折り返して描画"""
    if line_height is None:
        line_height = font_size * 1.5

    c.setFont(font_name, font_size)
    words = text.split(' ')
    lines = []
    current_line = []

    for word in words:
        test_line = ' '.join(current_line + [word])
        if c.stringWidth(test_line, font_name, font_size) <= max_width:
            current_line.append(word)
        else:
            if current_line:
                lines.append(' '.join(current_line))
            current_line = [word]

    if current_line:
        lines.append(' '.join(current_line))

    current_y = y
    for line in lines:
        c.drawString(x, current_y, line)
        current_y -= line_height

    return current_y

def generate_pdf():
    """スクリーンショットからPDFを生成"""

    # 設定ファイルを読み込む
    config = load_config()

    # 日本語フォントを登録（CIDフォントを使用）
    try:
        pdfmetrics.registerFont(UnicodeCIDFont('HeiseiMin-W3'))
        font_name = 'HeiseiMin-W3'
        print(f"使用フォント: {font_name} (CIDフォント)")
    except Exception as e:
        print(f"警告: CIDフォントの登録に失敗しました: {e}")
        try:
            pdfmetrics.registerFont(UnicodeCIDFont('HeiseiKakuGo-W5'))
            font_name = 'HeiseiKakuGo-W5'
            print(f"使用フォント: {font_name} (CIDフォント)")
        except Exception as e2:
            print(f"警告: 日本語フォントの登録に失敗しました: {e2}")
            font_name = 'Helvetica'
            print("Helveticaフォントを使用します（日本語が正しく表示されない可能性があります）")

    # パス設定
    screenshots_dir = Path("mockup-output/screenshots")
    output_dir = Path("mockup-output")
    output_dir.mkdir(exist_ok=True)

    output_pdf = output_dir / "MyFurdi_Mockup_Screens.pdf"

    # スクリーンショット一覧
    screenshots = [
        ("01_home.png", "ホーム画面", "Home Screen"),
        ("02_report.png", "レポート画面", "Report Screen"),
        ("03_qrcode.png", "入館証画面", "Entry Pass Screen"),
        ("04_reward.png", "リワード画面", "Reward Screen"),
        ("05_menu.png", "メニュー画面", "Menu Screen"),
    ]

    # PDFの作成
    c = canvas.Canvas(str(output_pdf), pagesize=A4)
    page_width, page_height = A4

    # タイトルページ
    c.setFont(font_name, 24)
    c.drawCentredString(page_width / 2, page_height - 100, "MyFurdi")

    c.setFont(font_name, 16)
    c.drawCentredString(page_width / 2, page_height - 140, "モックアップ画面集")
    c.setFont('Helvetica', 14)
    c.drawCentredString(page_width / 2, page_height - 165, "Screen Mockup Collection")

    c.setFont(font_name, 12)
    c.drawCentredString(page_width / 2, page_height - 200, "女性専用AIパーソナルトレーニングジム FURDI 会員向けアプリ")
    c.setFont('Helvetica', 10)
    c.drawCentredString(page_width / 2, page_height - 220, "FURDI Women's AI Personal Training Gym Member App")
    c.showPage()

    # 画面遷移図を追加（SVGがある場合）
    flow_diagram_path = Path("wireframes/screen_transition_diagram.svg")
    if flow_diagram_path.exists():
        print("画面遷移図を追加中...")

        try:
            # タイトルを先に描画
            c.setFont(font_name, 18)
            c.drawCentredString(page_width / 2, page_height - 60, "画面遷移図")
            c.setFont('Helvetica', 14)
            c.drawCentredString(page_width / 2, page_height - 85, "Screen Transition Diagram")

            # SVGをPNGに変換（一時ファイル）
            with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp_file:
                tmp_png_path = tmp_file.name

            # CairoSVGでSVGをPNGに変換（日本語フォントが正しく描画される）
            cairosvg.svg2png(
                url=str(flow_diagram_path),
                write_to=tmp_png_path,
                output_width=1400,  # SVGの元の幅
                output_height=1200  # SVGの元の高さ
            )

            # PNGを読み込んでPDFに追加
            img = Image.open(tmp_png_path)
            img_width, img_height = img.size

            # A4ページに収まるようにスケーリング
            max_diagram_width = page_width - 100
            max_diagram_height = page_height - 200

            scale = min(max_diagram_width / img_width, max_diagram_height / img_height)
            scaled_width = img_width * scale
            scaled_height = img_height * scale

            # 中央に配置
            x = (page_width - scaled_width) / 2
            y = (page_height - scaled_height) / 2 - 50

            # 画像を描画
            c.drawImage(tmp_png_path, x, y, width=scaled_width, height=scaled_height)

            # 一時ファイルを削除
            os.unlink(tmp_png_path)

            print(f"  画面遷移図を追加しました (サイズ: {scaled_width:.0f}x{scaled_height:.0f})")

        except Exception as e:
            print(f"  警告: 画面遷移図の追加に失敗しました: {e}")
            c.setFont(font_name, 10)
            c.drawCentredString(page_width / 2, page_height / 2,
                              "※画面遷移図の読み込みエラー")

        c.showPage()

    # 各画面を追加
    for idx, (img_file, title_ja, title_en) in enumerate(screenshots):
        img_path = screenshots_dir / img_file

        if not img_path.exists():
            print(f"警告: {img_path} が見つかりません")
            continue

        print(f"追加中: {title_ja} / {title_en} ({img_file})")

        # タイトル（日英併記）
        c.setFont(font_name, 16)
        c.drawString(50, page_height - 50, title_ja)
        c.setFont('Helvetica', 12)
        c.drawString(50, page_height - 70, title_en)

        # 画像を読み込んでサイズを取得
        img = Image.open(img_path)
        img_width, img_height = img.size

        # A4ページに収まるようにスケーリング（機能説明スペースを確保）
        max_width = page_width - 100
        max_height = page_height - 450  # 機能説明用のスペースを確保

        # アスペクト比を維持してスケーリング
        scale = min(max_width / img_width, max_height / img_height)
        scaled_width = img_width * scale
        scaled_height = img_height * scale

        # 画像を中央に配置
        x = (page_width - scaled_width) / 2
        y = page_height - 120 - scaled_height

        # 画像を描画
        c.drawImage(str(img_path), x, y, width=scaled_width, height=scaled_height)

        # 次のページへ（機能詳細を別ページに）
        c.showPage()

        # 機能詳細ページを追加
        if config and 'pages' in config:
            page_config = config['pages'][idx] if idx < len(config['pages']) else None
            if page_config and 'features' in page_config:
                features = page_config['features']

                # 機能詳細ページのタイトル
                c.setFont(font_name, 16)
                c.drawString(50, page_height - 50, f"{title_ja} - 機能詳細")
                c.setFont('Helvetica', 12)
                c.drawString(50, page_height - 70, f"{title_en} - Feature Details")

                feature_y = page_height - 110

                # 各機能の詳細を表示
                for feature in features:
                    if feature_y < 100:  # ページ下部に達したら次ページへ
                        c.showPage()
                        feature_y = page_height - 50

                    # 機能タイトル（日本語）
                    c.setFont(font_name, 11)
                    c.drawString(50, feature_y, f"● {feature['title_ja']}")
                    feature_y -= 18

                    # 機能タイトル（英語）
                    c.setFont('Helvetica-Bold', 10)
                    c.drawString(60, feature_y, feature['title_en'])
                    feature_y -= 20

                    # 機能詳細（日本語）
                    c.setFont(font_name, 9)
                    detail_ja = feature['detail_ja']
                    # テキストを折り返し
                    max_width = page_width - 120
                    words_ja = detail_ja
                    lines_ja = []
                    current_line = ""

                    for char in words_ja:
                        test_line = current_line + char
                        if c.stringWidth(test_line, font_name, 9) <= max_width:
                            current_line += char
                        else:
                            if current_line:
                                lines_ja.append(current_line)
                            current_line = char

                    if current_line:
                        lines_ja.append(current_line)

                    for line in lines_ja:
                        c.drawString(60, feature_y, line)
                        feature_y -= 14

                    feature_y -= 6

                    # 機能詳細（英語）
                    c.setFont('Helvetica', 8)
                    detail_en = feature['detail_en']
                    words_en = detail_en.split(' ')
                    lines_en = []
                    current_line = []

                    for word in words_en:
                        test_line = ' '.join(current_line + [word])
                        if c.stringWidth(test_line, 'Helvetica', 8) <= max_width:
                            current_line.append(word)
                        else:
                            if current_line:
                                lines_en.append(' '.join(current_line))
                            current_line = [word]

                    if current_line:
                        lines_en.append(' '.join(current_line))

                    for line in lines_en:
                        c.drawString(60, feature_y, line)
                        feature_y -= 12

                    feature_y -= 15  # 機能間のスペース

                # 機能詳細ページの終了
                c.showPage()

    # PDFを保存
    c.save()
    print(f"\n✓ PDF生成完了: {output_pdf}")
    print(f"  ファイルサイズ: {output_pdf.stat().st_size / 1024:.1f} KB")

if __name__ == "__main__":
    generate_pdf()
