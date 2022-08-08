from socket import fromshare
from django import forms

from pybo.models import Question, Answer

class QuestionForm(forms.ModelForm):    #이와 같은 클래스를 장고 폼이라 한다. forms.Form을 상속받으면 폼, forms.ModelForm을 상속받으면 모델 폼
    class Meta:
        model = Question    #장고 모델 폼은 Meta 클래스를 반드시 가져야 하며, 모델폼이 사용할 모델과 필드들을 적어야 한다.
        fields = ['subject', 'content']
        labels = {      #화면에 영어 대신 한글로 표시
            'subject' : '제목', 
            'content' : '내용',
        }
        
class AnswerForm(forms.ModelForm):   
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content' : '답변 내용',
        }
        