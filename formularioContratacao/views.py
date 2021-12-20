<<<<<<< HEAD
from django.shortcuts import render
from .models import Contratacao

def index(request):
    return render(request,'index.html')

def sucesso(request):
    return render(request,'sucesso.html')

=======
from django.shortcuts import render,redirect
from .models import Contratacao

def index(request):
    data = {}
    data ['index'] = Contratacao()
    return render(request,'index.html', data)

def create(request):
    form = Contratacao(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('sucesso')

def sucesso(request):
    return render(request,'sucesso.html')
>>>>>>> 62b0197 (alteracao)
