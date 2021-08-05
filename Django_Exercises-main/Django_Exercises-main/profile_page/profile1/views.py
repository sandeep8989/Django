from django.shortcuts import render

# Create your views here.
def profile1(request):
    return render(request,'homepage.html')


def service(request):
    return render(request,'services.html')


def project(request):
    return render(request,'projects.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request,'contact.html')