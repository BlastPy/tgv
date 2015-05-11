from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def all_parts(request):
    return render(request, 'index.html', {})

def test_view(request):
    return render(request, 'second.html', {})