from django.shortcuts import render

from django.http import HttpResponse
#페이지 요청에 대한 응답을 할 때 사용하는 장고 클래스

def index(request):
    return HttpResponse("안녕하세요 pybo에 오신걸 환영합니다")
 
