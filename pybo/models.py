from django.db import models
'''
. 파이보는 질문과 답변을 할 수 있는 파이썬 게시판 서비스이다.

자. 질문(Question) 모델에는 최소한
subject  /  content  /  create_date 

답변(Answer) 모델
question  / content / create_date
'''

class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    '''
      CASCADE 로 질문삭제되면 따라서 삭제 
      정확하게 Question 을 찝어 주기는 해야 한다.
      
    '''
    content = models.TextField()
    create_date = models.DateTimeField()