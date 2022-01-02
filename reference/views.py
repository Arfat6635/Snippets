from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"index.html")

    
def javascript(request):
    javascript_context={
        "Topic":"Javascript",
        "Topic_Message":"The Javascript cheat sheet is a one-page reference sheet for the javascript programming language.",
        "Topic_Start":"Getting Started",
    }
    return render(request,"javascript.html",javascript_context)


def python(request):
    python_context = {
        "Topic": "Python",
        "Topic_Message": "The Python cheat sheet is a one-page reference sheet for the Python programming language..",
        "Topic_Start": "Getting Started",
    }
    return render(request,"python.html",python_context)

def github(request):
    github_context={
        "Topic":"Github",
        "Topic_Message":"This cheat sheet summarizes commonly used Git command line instructions for quick reference.",
        "Topic_Start":"Getting Started"
    }
    return render(request, "github.html",github_context)

