import urllib.request
import json
import re

# JR東海の在来線運行情報ページ
url = "https://traininfo.jr-central.co.jp/zairaisen/index.html?lang=ja"

def check_status():
    try:
        # ブラウザからのアクセスに見せかけるためのヘッダー
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        )
        with urllib.request.urlopen(req) as response:
            html_content = response.read().decode('utf-8')
            
        # 「平常運転」という文字がページ内に含まれているかチェック
        # ※JR東海のページで平常時以外の文言になっているかを判定
        if "平常運転" in html_content:
            status = "normal"
        else:
            status = "delay" # 平常運転の文字がない（＝何らかの遅延・見合わせの可能性）
            
    except Exception as e:
        # エラー時は安全のため normal 扱い、または別ステータスにする
        status = "normal"
        
    # status.json というファイルに書き出す
    data = {"zairaisen": status}
    with open("status.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)

if __name__ == "__main__":
    check_status()
