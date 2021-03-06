from re import template
from django.shortcuts import render
from django.views.generic import DetailView
from .forms import *
from .models import *

# Create your views here.


def ImageView(request):
    if request.method == 'POST':
        profile_form = ProfileForm(data=request.POST, files=request.FILES)
        
        if profile_form.is_valid():
            profile_form.save()
        
    else:
        profile_form = ProfileForm()
    
    return render(request, 'upload.html', {'profile_form': profile_form})

def Display(request):
    if request.method == 'GET':
        img = Profile.objects.all()
        return render(request, 'display.html', {'profile_img': img})