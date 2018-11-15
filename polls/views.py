from django.http import HttpResponse
from django.shortcuts import render

from polls.models import Question


def index(request):

    # 1번 create를 이용하여 데이터 입력
    # Question.objects.create()

    # 2번 save를 이용하여 데이터 입력
    # Question(question_text='aaaa', pub_date=timezone.now()).save()


    q = Question.objects.all()[0]
    choices = q.choice_set.all()

    print(q.question_text)
    print(choices[0].choice_text)
    print(choices[1].choice_text)
    print(choices[2].choice_text)


    return HttpResponse('polls index')