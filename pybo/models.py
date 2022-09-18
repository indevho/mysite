from django.db import models


class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject + '/' + self.content
'''
get으로 조회할 경우 QuerySet이 아닌 Question 모델 객체가 리턴되었다. 
filter는 다건을 리턴하지만 get은 한건만 리턴하기 때문이다.

Question.objects.filter(id=3).count() 
는 결과가 그래서 0  이 반환이 됨. 
Question.objects.get(id=3).count()
이거는 오류가 남.

2번째 자료에 장고라는단어를 의도적으로 심은 뒤에 count 측정
Question.objects.filter(subject__contains='장고').count()
기대하는 값은 2 였는데, 1이 나온다. 이유가 무엇일까.
아하... commit 이 필요했었다. 문제 해결!


'''

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

    '''
    정말 신통방통한 장고의 기능이 아닐수 없다. 연결모델명_set 방법은 자주 사용!
    '''
    def __str__(self):
        return self.content + '/'