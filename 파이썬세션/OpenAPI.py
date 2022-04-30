import requests

url = 'http://openapi.seoul.go.kr:8088/737a4b646e696d6a38364e5157726e/json/GetParkInfo/1/1000/'

response = requests.get(url)

# json으로 바꿔오기
response_json = response.json()

## 100글자까지 뽑아오기
# print(response.content[:1000])

# # GetParkInfo의 키값을 불러와줘
# json_keys = response_json["GetParkInfo"].keys()

# print(json_keys)

data_row = response_json["GetParkInfo"]["row"]

new_data = []
# for x in data_row:
#     print(x["PARKING_NAME"], x["ADDR"])

# string으로 gu를 받으면 list로 반환한다는 명시를 해주는 거임
# 트렌드임
def get_data(gu : str) -> list:
    new_data = []
    for x in data_row : 
        if gu in x["ADDR"]:
            new_data.append(x["PARKING_CODE"])

    return new_data



