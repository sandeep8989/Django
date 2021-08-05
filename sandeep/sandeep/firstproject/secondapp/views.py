from django.shortcuts import render
from django.http import HttpResponse

def info(request):
    return render(request, 'second.html')

def one(request):
    return render(request, 'one.html')

def two(request):
    return render(request, 'two.html')

def three(request):
    return render(request,'three.html')