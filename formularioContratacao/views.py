from django.shortcuts import render
from .models import Contratacao

def index(request):
    return render(request,'index.html')

def sucesso(request):
    return render(request,'sucesso.html')

