from django.urls import path 
from .views import indexPageView, finderPageView, aboutPageView

urlpatterns = [
    path("", indexPageView, name = "index"),
    path("finder", finderPageView, name = "finder"),
    path("about", aboutPageView, name = "about")
]