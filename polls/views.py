from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from .models import Question
# Create your views here.

def index(request):
    last_question_list=Question.objects.order_by("-pub_date")[:5]
    context={'latest_question_list':last_question_list}
    return render(request, 'polls/index.html',context)
#   template=loader.get_template('polls/index.html')
#    return HttpResponse(template.render(context,request))
#    output=", ".join([q.question_text for q in last_question_list])
#    return HttpResponse(output)

def detail(request, question_id):
#    try:
#        question=Question.objects.get(pk=question_id)
#    except Question.DoesNotExist:
#        raise Http404("Question does not exist")
#    #return HttpResponse("You're looking at question %s." % question_id)
    question=get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question":question})

def results(request, question_id):
    response = ("You're looking at results of question %s." % question_id)
    return HttpResponse(response%question_id)

def vote(request, question_id):
    return HttpResponse("You're voting at question %s." % question_id)
