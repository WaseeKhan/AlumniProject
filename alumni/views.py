from django.shortcuts import render, redirect
from .form import *
from .models import AddAlumni, HomeSlider, NewsUpdate


# Create your views here.


def home(request):
    slider_items = HomeSlider.objects.all()
    news = NewsUpdate.objects.all()
    context = {'slider_items':slider_items, 'news': news}
    return render(request, 'alumni/index.html', context)


def profile(request, pk):
    alumni = AddAlumni.objects.filter(id=pk)
    context = {'alumni': alumni}
    return render(request, 'alumni/profile.html', context)


def alumnies(request):
    total = AddAlumni.objects.count()
    alumni = AddAlumni.objects.all()
    context = {'total':total, 'alumni':alumni}
    return render(request, 'alumni/alumnies.html', context)


def add_alumni_details(request):
    form = AddAlumniForm()
    if request.method == 'POST':
        form = AddAlumniForm(request.POST, request.FILES)
        print(request.POST)
        print(request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = AddAlumniForm()
    return render(request, 'alumni/add_alumni_details.html', {'form': form})


def updateProfile(request, pk):
    alumni = AddAlumni.objects.get(id=pk)
    form = AddAlumniForm(instance=alumni)
    if request.method == 'POST':
        form = AddAlumniForm(request.POST, instance=alumni)
        if form.is_valid():
            form.save()
            print("Profile updated!")
            return redirect('/')
        else:
            print("Profile not updated, pls try again!")

    context={'form':form}
    return render(request, 'alumni/update_profile.html', context)
