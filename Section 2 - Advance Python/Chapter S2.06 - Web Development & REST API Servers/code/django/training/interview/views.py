"""."""

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Topics, Question, Choice
# Create your views here.


def index(request):
    """."""
    topics = 1
    # template = loader.get_template('interview_questions.html')
    questions = Question.objects.filter(topics=topics)
    # creating the values to pass
    # questions = Question()
    # questions.get_questions(topics)
    # context = {
    #     'name': 'Belal Khan',
    #     'fname': 'Azad Khan',
    #     'course': 'Python Django Framework',
    #     'address': 'Kanke, Ranchi, India',
    # }
    # questions = Question.

    # rendering the template in HttpResponse
    # but this time passing the context and request
    # return HttpResponse(template.render(questions=quests, request=request))
    return render(request,
                  'interview_questions.html',
                  {'questions': questions})
