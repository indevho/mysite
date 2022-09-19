from django import forms
from pybo.models import Question, Answer
#Question 질문 등록시에 쓰일 FORM
'''
QuestionForm은 모델 폼(forms.ModelForm)을 상속했다. 
장고의 폼은 일반 폼(forms.Form)과 모델 폼(forms.ModelForm)이 있는데 
모델 폼은 모델(Model)과 연결된 폼으로 폼을 저장하면 
연결된 모델의 데이터를 저장할수 있는 폼이다.
 모델 폼은 이너 클래스인 Meta 클래스가 반드시 필요하다. 
 
 Meta 클래스에는 사용할 모델과 모델의 속성을 적어야 한다.

'''
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question  # 사용할 모델
        fields = ['subject', 'content']  # QuestionForm에서 사용할 Question 모델의 속성
        # widgets = {
        #     'subject': forms.TextInput(attrs={'class': 'form-control'}),
        #     'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        # }
        labels = {
            'subject': '제목한글',
            'content': '내용한글',
        }
#주의!!
#   forms.py와 같은 신규 파일 작성시에는 로컬 서버 재시작이 필요하다.

# labels ?
# 질문 등록 화면에 표시되는 'Subject', 'Content'를
# 영문이 아니라 한글로 표시하고 싶다면 다음처럼 labels 속성을 지정하면 된다.

'''
문제의식 : { form.as_p }를 사용하면 빠르게 템플릿을 만들 수 있지만 HTML 코드가 자동으로 생성되므로 
디자인 측면에서 많은 제한이 생긴다

 폼을 이용하여 자동으로 HTML 코드를
  생성하지 말고 직접 HTML 코드를 작성하는 방법을 사용해 보자. 
  우선 수작업시 필요없는 widget 속성을 제거하자.

그리고 질문 등록 템플릿을 다음과 같이 수정하자.

[파일명: projects\mysite templates\pybo\question_form.html]


장고의 템플릿 필터는 |default_if_none:'' 처럼 | 기호와 함께 사용된다.
'''


#이번에는 질문 등록에 장고 폼을 적용한 것처럼 답변 등록에도 장고 폼을 적용해 보자.
# 답변을 등록할 때 사용할 AnswerForm 정의!
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }