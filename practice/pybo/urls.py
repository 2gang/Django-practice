from django.urls import path

from . import views

app_name = 'pybo'   #네임스페이스 - 각가의 앱이 관리하는 독립된 이름 공간/ 중복된 URL 별칭 사용이 가능하도록 함

urlpatterns=  [ 
    path('', views.index, name='index'),    #별칭 부여
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
]