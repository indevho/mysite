from django.urls import path

# 본 동 폴더에서 끌고오는 법은 JUST DOT >   .  써주기
from . import views

'''
 만약에 path('/', views.index),
 를 쓰면 . 알아서  /는 이미 붙어있도록 해두었기 떄문에..
 어디서??? config/urls.py 에서
  http://127.0.0.1:8000/pybo//  
 로 접근해야지 된다..... 
 그러니까 엥간하면 urlpattern에서  / 를 맨뒤에쓰지말라.
 아니 써선안된다
 니가 config.urls.py 를 확실히 읽어서 검증하기전까지는..... 

'''
urlpatterns = [
    path('', views.index),
]