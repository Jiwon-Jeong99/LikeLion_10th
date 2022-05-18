from django.db import models
# from django.dispatch import receiver
# from django.forms import DateTimeField


# autofield : (데이터 식별자) 값이 하나씩 들어올때마다 값이 하나씩 늘어남 (데이터 식별위해)
class Footprint(models.Model):
    footprint_id = models.AutoField(primary_key=True)
    # text를 받고, null이면 거짓으로 판명
    receiver = models.TextField(null=False)
    message = models.TextField(null=False)
    # 메세지를 정렬해야 하기 때문에 sent_at
    # create, update 가지고 있음 (분석을 할 때 사용)
    # auto_now_add (db야 너가 알아서 시간 넣어줘)
    # blank=False 빈칸일 수 없다
    sent_at = models.DateTimeField(auto_now_add=True, blank=False)
