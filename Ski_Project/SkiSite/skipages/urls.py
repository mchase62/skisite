from django.urls import path 
from .views import indexPageView, finderPageView, aboutPageView, editSkiPageView, updateSkiPageView, deleteSkiPageView, addSkiPageView

urlpatterns = [
    path("", indexPageView, name = "index"),
    path("finder", finderPageView, name = "finder"),
    path("about", aboutPageView, name = "about"),
    path("edit/<int:ski_id>/", editSkiPageView, name = 'editSki'),
    path("updateSkis/", updateSkiPageView, name = "updateSki"),
    path("deleteSki/<int:ski_id>/", deleteSkiPageView, name = 'deleteSki'),
    path("addSki", addSkiPageView, name="addSki")
]