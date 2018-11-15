from django.http import HttpResponse
from django.shortcuts import render

from polls.models import Question


def index(request):
    q = Question.objects.all()[0]
    choices = q.choice_set.all()

    print(q.question_text)
    print(choices[0].choice_text)
    print(choices[1].choice_text)
    print(choices[2].choice_text)


    return HttpResponse('polls index')