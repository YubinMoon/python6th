from django.shortcuts import get_object_or_404, render
from polls.models import Question


def index(request):
    lastest_question_list = Question.objects.order_by("-pub_date")[:5]
    content = {"lastest_question_list": lastest_question_list}
    return render(request, "polls/index.html", content)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def vote(request):
    pass


def results(request):
    pass
