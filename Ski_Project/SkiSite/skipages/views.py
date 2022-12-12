from django.http import HttpResponse
from django.shortcuts import render
from skipages.models import Skis

# Create your views here.

def indexPageView(request):
    return render(request, 'index.html')

def aboutPageView(request):
    return render(request, 'about.html')

def finderPageView(request):
    data = Skis.objects.all()

    context = {
        'skis' : data,
    }
    return render(request, 'deezskis.html', context)
    
def editSkiPageView(request, ski_id):
    data = Skis.objects.get(id=ski_id)

    context ={
        'skis' : data,
    }

    return render(request, 'editski.html', context)

def updateSkiPageView(request):
    if request.method=='POST':
        ski_id=request.POST['ski_id']

        ski = Skis.objects.get(id=ski_id)

        ski.brand = request.POST["brand"]
        ski.model = request.POST["model"]
        ski.waistwidth = request.POST["waistwidth"]
        ski.length = request.POST.get("length")
        ski.type = request.POST.get("type")

        ski.save()

    return finderPageView(request)

def deleteSkiPageView(request, ski_id):
    data = Skis.objects.get(id=ski_id)

    data.delete()

    return finderPageView(request)

def addSkiPageView(request):
    if request.method=='POST':
        ski = Skis()

        ski.brand = request.POST["brand"]
        ski.model = request.POST["model"]
        ski.waistwidth = request.POST["waistwidth"]
        ski.length = request.POST.get("length")
        ski.type = request.POST.get("type")

        ski.save()

        return finderPageView(request)
    else:
        return render(request, 'addSki.html')