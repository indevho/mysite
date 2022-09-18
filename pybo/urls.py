from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('<int:question_id>/', views.detail),

]
'''
url pattern 중 
 string 으로 들어오면? 
 <string:search_keyword>/ 로 가야 하나? 

'''