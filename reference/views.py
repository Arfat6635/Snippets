from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"index.html")

    
def javascript(request):
    context={
        "Topic":"Javascript",
        "Topic_Message":"The Javascript cheat sheet is a one-page reference sheet for the javascript programming language.",
        "Topic_Start":"Getting Started",
    }
    return render(request,"javascript.html",context)
