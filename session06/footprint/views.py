# from django.shortcuts import render
# render는 template을 위한 것
# python은 함수-함수, class-class 사이 엔터 2번
from footprint.models import Footprint
from django.http import JsonResponse
import json



# request라는 매개변수를 무조건 받음
# orm을 이용해보자
def footprint_GET(request):
    # 필요한 데이터만 filter해서 Footprint에 담아줘!
    # 최신데이터 먼저 가져와줘! 내림차순(-sent_at)
    footprints = Footprint.objects.filter(receiver='정지원').order_by('-sent_at')
    messages = []
    # messages는 배열 형태로

    for i in range(len(footprints)):
        # i번째 footprints에서 message를 뽑아서 messages에 더해줘!
        messages.append(footprints[i].message)

    return JsonResponse({
        'status' : 200,
        'message':'Footprint 조회 성공',
        'data': {
            'messages' : messages
        }
    })

# request라는 매개변수를 무조건 받음
# GET으로 가져왔으면 써줘야지!
def footprint_POST(request):
    # utf-8로 디코딩해주고 json 형태로 받아온다
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    # message에는 body의 content가 들어갈거임
    # orm으로 데이터를 추가해온거임
    Footprint.objects.create(message=body['content'], receiver=body['receiverName'])

    # 성공하면 json으로 이 응답을 준다
    return JsonResponse({
        # 데이터가 성공적으로 받아졌다는 201번이 맞음
        # 200은 get에서 요청이 성공했다는게 맞음
        'status':200,
        'message':'메세지 전송 성공'
    })