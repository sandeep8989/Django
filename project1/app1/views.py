from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"Home.html")

def dogs(request):
    return render(request,"dogs.html")

def cats(request):
    return render(request,"cats.html")

def birds(request):
    return render(request,"birds.html")

def contact(request):
    return render(request,"contact.html")