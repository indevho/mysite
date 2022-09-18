from django.shortcuts import render

# Create your views here.
# version1  from django.http import HttpResponse
from django.shortcuts import render
from .models import Question

#version1  def index(request):
#version1    return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")

def index(request):
    question_list = Question.objects.order_by('-create_date')
    '''
     question_lit 를  정렬하여 끌고오기- 정렬순이 강제된 상태..   order by 뒤를 변수화 하면 어떨까? 
    '''
    context = {'question_list': question_list}
    '''
       querySet 을  context 라는 곳에 담아버리기. ,  body에  뭉쳐담아서 response 하기 
    '''
    return render(request, 'pybo/question_list.html', context)
    '''
     question_lit 를  정렬하여 끌고오기- 정렬순이 강제된 상태..   order by 뒤를 변수화 하면 어떨까? 
    '''