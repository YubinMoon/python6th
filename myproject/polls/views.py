from django.shortcuts import render
from polls.models import Question


def index(request):
    lastest_question_list = Question.objects.order_by("-pub_date")[:5]
    content = {"lastest_question_list": lastest_question_list}
    return render(request, "polls/index.html", content)


def detail(request):
    pass


def vote(request):
    pass


def results(request):
    pass
