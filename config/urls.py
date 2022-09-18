"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
#from django.urls import path
#from pybo import views
from django.urls import path, include
# import 기준이 뭘까?? 여튼 pybo/views.py 땡겨오는걸 보면. 루트폴더(?) 인 mysite 를 기준으로 손쉽게 캐치해내는것같다.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')),  # 마지막에 / 를 왜 해대는 걸까요 . URL을 정규화하는 장고의 기능 때문이다
]
print("config/urls.urlpatterns====================")
print(urlpatterns)
