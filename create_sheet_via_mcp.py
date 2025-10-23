#!/usr/bin/env python3
"""
MCP Google Sheetsサーバーを使ってスプレッドシートを作成
"""
import asyncio
import json
import csv
import sys
import os
from pathlib import Path

# MCPクライアント用の設定
MCP_SERVER_COMMAND = "uvx"
MCP_SERVER_ARGS = ["mcp-google-sheets@latest"]
MCP_SERVER_ENV = {
    "GOOGLE_APPLICATION_CREDENTIALS": os.path.expanduser("~/.config/mcp-google-sheets/client_secret_109341072757-l9b2620gt4okkll64qolreb45iurtcjl.apps.googleusercontent.com.json"),
    **os.environ
}

CSV_PATH = '/Volumes/KIOXIA/Developments/withAI/Vercel/Furdi/MyFURDI/HiranoMyFurdi/MyFurdi_機能一覧表.csv'

async def call_mcp_tool(process, method, params):
    """MCPツールを呼び出す"""
    request = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": method,
        "params": params
    }

    # リクエストを送信
    request_json = json.dumps(request) + "\n"
    process.stdin.write(request_json.encode())
    await process.stdin.drain()

    # レスポンスを読み取り
    response_line = await process.stdout.readline()
    response = json.loads(response_line.decode())

    if "error" in response:
        raise Exception(f"MCP Error: {response['error']}")

    return response.get("result")

async def main():
    """メイン処理"""
    print("MCPサーバーを起動中...")

    # MCPサーバーを起動
    process = await asyncio.create_subprocess_exec(
        MCP_SERVER_COMMAND,
        *MCP_SERVER_ARGS,
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
        env=MCP_SERVER_ENV
    )

    try:
        # 初期化メッセージを送信
        init_request = {
            "jsonrpc": "2.0",
            "id": 0,
            "method": "initialize",
            "params": {
                "protocolVersion": "2024-11-05",
                "capabilities": {},
                "clientInfo": {
                    "name": "MyFurdi Google Sheets Creator",
                    "version": "1.0.0"
                }
            }
        }

        process.stdin.write((json.dumps(init_request) + "\n").encode())
        await process.stdin.drain()

        # 初期化レスポンスを読み取り
        init_response = await process.stdout.readline()
        print(f"初期化レスポンス: {init_response.decode().strip()}")

        # CSVファイルを読み込み
        print(f"\nCSVファイルを読み込み中: {CSV_PATH}")
        with open(CSV_PATH, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            data = list(reader)

        print(f"データ行数: {len(data)}")

        # スプレッドシートを作成
        print("\nスプレッドシートを作成中...")
        create_result = await call_mcp_tool(
            process,
            "tools/call",
            {
                "name": "create_spreadsheet",
                "arguments": {
                    "title": "MyFurdi 機能一覧表"
                }
            }
        )

        spreadsheet_id = create_result.get("spreadsheetId")
        print(f"スプレッドシート作成成功!")
        print(f"ID: {spreadsheet_id}")
        print(f"URL: https://docs.google.com/spreadsheets/d/{spreadsheet_id}")

        # データを追加
        print("\nデータを追加中...")
        add_result = await call_mcp_tool(
            process,
            "tools/call",
            {
                "name": "add_rows",
                "arguments": {
                    "spreadsheet_id": spreadsheet_id,
                    "sheet_name": "Sheet1",
                    "data": data
                }
            }
        )

        print("データ追加完了!")
        print(f"\n✅ 完成: https://docs.google.com/spreadsheets/d/{spreadsheet_id}")

    except Exception as e:
        print(f"エラー: {e}", file=sys.stderr)
        stderr = await process.stderr.read()
        if stderr:
            print(f"サーバーエラー: {stderr.decode()}", file=sys.stderr)
    finally:
        # プロセスを終了
        process.terminate()
        await process.wait()

if __name__ == '__main__':
    asyncio.run(main())
