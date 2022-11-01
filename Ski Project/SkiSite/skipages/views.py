from django.http import HttpResponse

# Create your views here.

def indexPageView(request):
    return HttpResponse('This is the home page for the ski site')

def aboutPageView(request):
    return HttpResponse('This is the about page for the ski site')

def finderPageView(request):
    return HttpResponse('This is where you look for skis')