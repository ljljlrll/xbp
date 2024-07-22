import requests

# NAVITIME APIのエンドポイントとAPIキー
endpoint = "https://api.navitime.co.jp/v3/transport"
api_key = "69591e8177msh24cda3e51e37130p169aa0jsn7df2c19bbd61"

# パラメータ（例: 出発地と目的地）
params = {
    "start": "保土ヶ谷駅",
    "goal": "横浜駅",
    "appkey": api_key
}

try:
    # APIにGETリクエストを送信
    response = requests.get(endpoint, params=params)
    
    # レスポンスのJSONデータを取得
    data = response.json()
    
    # データの解析や利用
    # ここに必要な処理を記述する
    
    # 例: レスポンスからルート情報を取得
    route = data["route"]
    for step in route:
        print(step["instruction"])

except requests.exceptions.RequestException as e:
    print("Request error:", e)
