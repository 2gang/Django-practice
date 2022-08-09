from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from django.utils import timezone

from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator


#페이지 요청에 대한 응답을 할 때 사용하는 장고 클래스


def index(request):
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지

    # 조회
    question_list = Question.objects.order_by('-create_date')   #앞에 -가 붙으면 역순을 의미한다. 즉 작성일시의 역순

    # 페이징처리
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj}
    return render(request, 'pybo/question_list.html', context)      #render 함수는 context에 있는 question_list를 템플릿에 적용하여 html 코드로 변환한다.
 
def detail(request, question_id):   #Question 상세 내용을 확인하는 클래스, question_id 매개변수로 확인
    question = get_object_or_404(Question, pk=question_id)  #존재하지 않는 페이지에 접속하면 404오류가 뜨도록 함
    context = {'question' : question}   #question 모델 데이터 저장
    return render(request, 'pybo/question_detail.html', context)

# def answer_create(request, question_id):    #답변 클래스, request에는 detail.html의 textarea 부분이 넘어온다.
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now()) #넘어온 값을 추출하는 코드가 request.POST.get('content') 이다.
    # Question 모델을 통해 Answer 모델 데이터를 생성하기 위해 answer_set.create를 사용했다.
    return redirect('pybo:detail', question_id=question.id) #답변 등록 후 페이지 이동

def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form}    #{'form': form}은 폼 엘리먼트를 작성할 때 사용
    return render(request, 'pybo/question_form.html', context)  

def answer_create(request, question_id):
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
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)