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
      
    return render(request,'index.html',context)


def all_rozdil(request,is_main):
    stats = Stats.objects.all().filter(main_is_id=is_main)
    rozdil = Rozdil.objects.all()
    title_rozdil = Rozdil.objects.get(pk=is_main)
    context = {'stats':stats,'rozdil': rozdil,'title_rozdil':title_rozdil }

    return render(request,'stats.html',context)

def detali(request,id_ekz):
    details = Stats.objects.get(pk=id_ekz)
    rozdil = Rozdil.objects.all()
    context = {'details':details,'rozdil': rozdil}

    return render(request,'details.html',context)