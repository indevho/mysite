from django.shortcuts import render

# Create your views here.
# version1  from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question
from .models import Answer
#version1  def index(request):
#version1    return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")

def index(request):
    question_list = Question.objects.order_by('-create_date')
    '''
     question_lit 를  정렬하여 끌고오기- 정렬순이 강제된 상태..   order by 뒤를 변수화 하면 어떨까? 
     
     - 를 눈여겨 볼 것.  DESC와 같다, 즉 최신 값부터 끌고오도록 한다는 의미
     
    '''
    context = {'question_list': question_list}
    '''
       querySet 을  context 라는 곳에 담아버리기. ,  body에  뭉쳐담아서 response 하기 
    '''
    return render(request, 'pybo/question_list.html', context)
    '''
        index  >>  기본적으로  /pybo/ 로 들어온 경우 꺼내올 VIEW 지정..
       
     question_lit 를  정렬하여 끌고오기- 정렬순이 강제된 상태..   order by 뒤를 변수화 하면 어떨까? 
    '''


'''
 새로운 PAGE 추가 ..   요청으로 int 값 오는 경우 이 detail  view 를 챙겨오게 됨.
   urls.py에서 언급한 question_id 가 그대로  detail 호출시에 찍힌다. 
   이 question_id 가 int 인지 이상한 문자로 오는지는 , urls.py에서 이미 걸러진다 ( '<int:question_id>' ) 
'''
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    '''
     무리해서 30호출 시 :Page not found (404) ___  No Question matches the given query. 
     이번에는 500 대신 404 오류 페이지가 출력되는 것을 확인할 수 있다.
    '''
    #question = Question.objects.get(id=question_id)
    '''
    
     무리해서 30호출 시 :  DoesNotExist at /pybo/30/ ___  Question matching query does not exist.
    '''

    print('detail 수행 한다 :  '+str(question_id))

    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    #answer버전!
    #answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now())
    #answer.save()

    return redirect('pybo:detail', question_id=question.id)