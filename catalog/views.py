from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def get_books(request):
    return HttpResponse("Welcome to the NouveauLib page.")


def greet(request, name):
    return render(request, "index.html", {'name': name})
