from django.urls import path
from . import views

urlpatterns = [
    path("home",views.home,name="home"),
    path("dogs",views.dogs,name="dogs"),
    path("cats",views.cats,name="cats"),
    path("birds",views.birds,name="birds"),
    path("contact",views.contact,name="contact")
]
