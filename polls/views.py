from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from polls.models import Question

def vote(request, question_id):
    select = request.POST['select']

    print(select)

    return HttpResponse('ok')



def detail(request, question_id):
    q = Question.objects.get(id=question_id) # 조건에 맞는 데이터 1개 조회
    c = q.choice_set.all()
    # choice = ''
    # for a in c:
    #     choice += a.choice_text
    #             request  템플릿   컨텍스트(데이터/모델)
    return render(
        request,
        'polls/detail.html',
        {
            'question': q.question_text,
            'choice': c
        }
    )

    # return HttpResponse(q.question_text + '<br>' + choice)

def detail2(request, num1, num2):
    return HttpResponse(num1 + num2)

def add(request):
    q = request.GET['q']

    Question.objects.create(question_text=q, pub_date=timezone.now())

    return HttpResponse('')

def index(request):

    questions = Question.objects.all()
    #             request       템플릿            컨텍스트 (모델/데이터)
    return render(
        request, 'polls/index.html',
        {'question': questions})

    # 1번 create를 이용하여 데이터 입력
    # Question.objects.create()

    # 2번 save를 이용하여 데이터 입력
    # Question(question_text='aaaa', pub_date=timezone.now()).save()

    # return HttpResponse('polls index')