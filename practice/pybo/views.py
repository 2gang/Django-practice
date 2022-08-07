from django.shortcuts import render, get_object_or_404
from .models import Question


#페이지 요청에 대한 응답을 할 때 사용하는 장고 클래스

def index(request): 
    question_list = Question.objects.order_by('-create_date')    #앞에 -가 붙으면 역순을 의미한다. 즉 작성일시의 역순
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)  #render 함수는 context에 있는 question_list를 템플릿에 적용하여 html 코드로 변환한다.
 
def detail(request, question_id):   #Question 상세 내용을 확인하는 클래스, question_id 매개변수로 확인
    question = get_object_or_404(Question, pk=question_id)  #존재하지 않는 페이지에 접속하면 404오류가 뜨도록 함
    context = {'question' : question}   #question 모델 데이터 저장
    return render(request, 'pybo/question_detail.html', context)