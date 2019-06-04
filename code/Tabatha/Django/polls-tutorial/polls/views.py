from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

# from django.template import loader

from .models import Choice, Question

class IndexView(generic.ListView):
        template_name = "polls/index.html"
        
        def get_queryset(self):
                return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
        model = Question
        template_name = "polls/detail.html"

        def get_queryset(self):
                return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
        model = Question
        template_name = "polls/results.html"

# def index(request):
#         latest_question_list = Question.objects.order_by("-pub_date")[:5]
#         # template = loader.get_template("polls/index.html")
#         context = {
#                 "latest_question_list":latest_question_list
#         }
#         # return HttpResponse(template.render(context, request))
#         return render(request, "polls/index.html", context)

# def detail(request, question_id):
#         question = get_object_or_404(Question, pk=question_id)
#         return render(request, "polls/detail.html", {
#                 "question":question
#         })

# def results(request, question_id):
#         question = get_object_or_404(Question, pk=question_id)
#         return render(request, "polls/results.html", {
#                 "question": question
#         })
def vote(request, pk):
        question = get_object_or_404(Question, pk=pk)
        try:
                selected_choice = question.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
                return render(request, "polls/details.html", {
                        "question": question,
                       'error_message': "Please make a selection."
                })
        else:
                selected_choice.votes += 1
                selected_choice.save()
                return HttpResponseRedirect(reverse("polls:results", args=(question.id, )))

def add_question(request):
        if request.method == "GET":
                return render(request, "polls/add-q.html")
        elif request.method == "POST":
                question = Question.objects.create(question_text=request.POST['add-q'], pub_date=timezone.now())
                question.choice_set.create(question=question, choice_text=request.POST['add-c1'])
                question.choice_set.create(question=question, choice_text=request.POST['add-c2'])
                question.choice_set.create(question=question, choice_text=request.POST['add-c3'])
                return HttpResponseRedirect(reverse("polls:index"))



