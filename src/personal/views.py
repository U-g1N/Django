from django.shortcuts import render
from personal.models import Question

# Create your views here.

def home_screen_view(request):
    
    context = {}
    #Method 1
    #context[some_string] = "This is some string"

    #Method 2
    # context {
    #     'some_string': "This is some string"
    # }

    # list_of_values = []
    # list_of_values.append("First Entry")
    # list_of_values.append("Second Entry")
    # list_of_values.append("Third Entry")
    # context['list_of_values']=list_of_values

    questions = Question.objects.all()
    context['questions'] = questions

    return render(request, "personal/home.html", context)