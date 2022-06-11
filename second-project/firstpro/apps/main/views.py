from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    sections = Section.objects.all()
    context = {
        'welcome': 'به وب سایت من خوش امدید ',
        'sections': sections
    }
    return render(request, 'main/index.html', context)
