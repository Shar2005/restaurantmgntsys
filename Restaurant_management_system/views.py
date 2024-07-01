# I have created this file - sharmistha
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
