from django.urls import path

from . import views



app_name = 'pybo'
'''
 pybo 이외의 앱이 추가되는 경우도 상정하라! 

'''

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>', views.answer_create, name='answer_create'),
]
'''
url pattern 중 
 string 으로 들어오면? 
 <string:search_keyword>/ 로 가야 하나? 

'''
'''
   URL 하드코딩 을 극복하는 URL 별칭 사용을 위하여, 
    path의 파라미터로  name 이 추가된다!
    
    
    redirect 함수와 URL 별칭
URL별칭은 템플릿 외에 redirect 함수에서도 사용된다. 
redirect는 특정 페이지로 이동시키는 함수이다. 
redirect 함수의 사용은 뒤에서 자세히 공부한다.
redirect('pybo:detail', question_id=question.id)

'''