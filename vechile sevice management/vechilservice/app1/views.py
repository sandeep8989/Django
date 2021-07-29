from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from .forms import Fun
from .models import show


# Create your views here.
def home(request):
    if request.method == 'POST':
        fm = Fun(request.POST)
        if fm.is_valid():
            custname = fm.cleaned_data['custname']
            vechtype = fm.cleaned_data['vechtype']
            vechnum = fm.cleaned_data['vechnum']
            servicetype = fm.cleaned_data['servicetype']
            reg_data = show(custname=custname, vechtype=vechtype, vechnum=vechnum, servicetype=servicetype)
            reg_data.save()
            messages.success(request, 'You have register successfully')
            fm=Fun()

    else:
        fm = Fun()
    return render(request, 'home.html', {'form': fm, 'shows': show.objects.all()})


def delete(request, id):
    fm = show.objects.get(id=id)
    fm.delete()
    return HttpResponseRedirect('/')


def update_data(request, id):
    if request.method == "POST":
        pi = show.objects.get(pk=id)
        fm = Fun(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'You have update successfully')
    else:
        pi = show.objects.get(pk=id)
        fm = Fun(instance=pi)
    return render(request, 'updateonline.html', {'form': fm})
