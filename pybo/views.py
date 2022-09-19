from django.shortcuts import render

# Create your views here.
# version1  from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question
from .models import Answer
from .forms import QuestionForm, AnswerForm
from django.http import HttpResponseNotAllowed
#version1  def index(request):
#version1    return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")
#PAGING을 도입해보자!!
from django.core.paginator import Paginator


def index(request):
    page = request.GET.get('page', '1')  # 페이지 initial 값
    # currentPage값 가져오고, 없는경우 1 디폴트로 떙겨오라는 의미
    question_list = Question.objects.order_by('-create_date')
    '''
     question_lit 를  정렬하여 끌고오기- 정렬순이 강제된 상태..   order by 뒤를 변수화 하면 어떨까? 
     
     - 를 눈여겨 볼 것.  DESC와 같다, 즉 최신 값부터 끌고오도록 한다는 의미
     
    '''
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}
    #context = {'question_list': question_list}
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

###TEST 데이터 300개 생성하기 
>>> for i in range(300):
...     q = Question(subject='테스트 데이터입니다:[%03d]' % i, content='내용무', create_date=timezone.now())
...     q.save()
...   
   
   
   
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

#def answer_create(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    #answer버전!
    #answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now())
    #answer.save()

#    return redirect('pybo:detail', question_id=question.id)

def answer_create(request, question_id):
    """
    pybo 답변등록 ( 바로 위에 구버전 answer_create 있음! )
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)




# def question_create(request):
#     form = QuestionForm()
#     return render(request, 'pybo/question_form.html', {'form': form})
def question_create(request):
    '''
    form method="post" 로 지정 했으므로.
    pOST 만 받는 조건을 툭 걸어준다
    '''
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            #timezone.now() 라는 함수가 datetime 형식에 맞나보다
            #>> DateTimeField
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)