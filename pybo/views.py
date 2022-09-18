from django.http import HttpResponse

'''
분명히  views.index 로 땡겨오기 때문에.. 
'''
def index(request):
   return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다. \n "+
                       "나는 index 함수의 RETURN값입니다 지금은 단순 문자열로된 \n"+
" HTTPRESPONSE")
'''
  개행문자가 안먹힌다 이건 HTTP쪽에서   개행문자를 다 씹어버려서 ??

'''






'''
 만일 index 를 단일 HttpResponse 로 해버리면..
 응~ 안통한다.  return 형태이길 원하는 것 같다. 이건 아마도 파이썬문법RULE?? 
'''
#index =  HttpResponse("안녕하세요 pybo에 오신것을 환영합니다. 나는 index 함수의 RETURN값입니다 지금은 단순 문자열로된
# HTTPRESPONSE")