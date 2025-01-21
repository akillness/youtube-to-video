import json

path_json = f'./KoAlpaca_v1.LiarHeart.json'
print(path_json)
# JSON 문자열을 Python 리스트로 변환
with open(path_json, "r") as file:
    for line in file:
        try:
            data = json.loads(line.strip())
            print(data)  # 각 JSON 객체 출력
        except json.JSONDecodeError as e:
            print(f"JSON decode error: {e}")
  
