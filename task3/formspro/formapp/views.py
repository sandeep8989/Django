from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def resume(request):
    return render(request, "resume.html")

def projects(request):
    return render(request, "projects.html")

def contacts(request):
    return render(request, "contacts.html")

