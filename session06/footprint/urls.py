from . import views
from django.urls import path

urlpatterns = [
    path("", views.footprint_GET),
    # send까지 붙으면 views.py에 footprint_POST 함수 실행
    path("send", views.footprint_POST),
]
