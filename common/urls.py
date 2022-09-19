from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
'''
위 오류는 registration 디렉터리에 login.html 파일이 없음을 의미한다. 
앞에서 사용한 LoginView는 registration이라는 템플릿 디렉터리에서 login.html 파일을 찾는다. 
그런데 이 파일을 찾지 못해 오류가 발생한 것이다. 
이 오류를 해결하려면 registration/login.html 템플릿 파일을 작성해야 한다.

  어느 경로로 타고 가서 login.html 을 찾으라고 강제로 값 입력해둠 
  강제로 입력을 하니깐 
  registration/login.html이 아닌 common/login.html이 없다는 오류로 변경되었다.
  

'''