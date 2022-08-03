from django.db import models

class Question(models.Model):   #질문 모델
    subject = models.CharField(max_length= 200) #제목, 글자수 제한 200
    content = models.TextField()    #질문 내용, 글자수 제한 없는 데이터
    create_date = models.DateTimeField() #질문 날짜
    
    def __str__(self):
        return self.subject #데이터 조회시 id가 아닌 제목을 표시
    
    
class Answer(models.Model):   #답변 모델
    question = models.ForeignKey(Question, on_delete=models.CASCADE) 
    #질문(어떤 질문의 답변인지), ForeignKey - Question모델과 연결 
    # on_delete=models.CASCADE - 질문이 삭제되면 답변도 삭제됨
    content = models.TextField()    #답변 내용
    create_date = models.DateTimeField() #답변 날짜
