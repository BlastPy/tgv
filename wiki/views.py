from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from django.db import models
from wiki.models import NamePart
from wiki.models import Rozdil
from wiki.models import Stats


def index(request):
    rozdil = Rozdil.objects.all()
    context = {'rozdil': rozdil } 
      
    return render(request,'rozdils.html',context)

def test_view(request):
    return render(request, 'second.html', {})

def stats(request,is_main):
    stats = Stats.objects.filter(main_is=is_main)
    context = {'stats':stats}

    return render(request,'stats.html',{})