# - 프레임워크는 언어가 아님
# - 장고-외국 스타트업 / 노드-한국 스타트업

# ### **API**

# - 해당 정보를 주세요 → 요청
# - 서버에 데이터들을 만들어놓는 것 → 백엔드

# pip3 install requests

# → requests라는 파이썬 모듈을 install


# # 리스트 - 순서대로 차곡차곡
from traceback import print_list


item_list = ["지원", "민서", "동길", "해윤", "교현"]

# new_data = []

# for x in item_list:
#     if x == "명준":
#         new_data.append(x)

num_list = [1,2,3,4,5,6,7,8,9,10]

new_data = []
for n in num_list:
    if n%2 == 0:
        new_data.append(n)
print(new_data)

str = '지원 해윤 동길 교현 민서'

if "지원" in str:
    print("지원이가 있대")
else:
    print("없다는데?")

# print(item_list[0])

# # 리스트 접근
# a = item_list[3]

# # 리스트 값 지정
# item_list[0] = "지원"

# # 리스트 메서드
# item_list.append("명준")
# print(item_list)


# # 딕셔너리 
# item_dic = {"key1" : 111, "key2" : 222}
# print(item_dic)

# # 딕셔너리 접근
# print(item_dic["key1"])

# # 딕셔너리 변경
# item_dic["key1"] = 222
# print(item_dic)

# # 딕셔너리 추가
# item_dic["key3"] = 333
# print(item_dic)

# # 딕셔너리 메서드
# # 딕셔너리는 키값이나 value값만 받아서 리스트를 만들어서 for문 돌림
# dic_val = item_dic.values()
# print(dic_val)

# dic_keys = item_dic.keys()
# print(dic_keys)

# dic_items = item_dic.items()
# print(dic_items)
