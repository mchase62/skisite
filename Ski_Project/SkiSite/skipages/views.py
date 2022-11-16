from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def indexPageView(request):
    return render(request, 'index.html')

def aboutPageView(request):
    return render(request, 'about.html')

def finderPageView(request):
    return render(request, 'deezskis.html')