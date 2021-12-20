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
from formularioContratacao.forms import ContratacaoForm

def index(request):
    return render(request,'index.html')

def form(request):
    data = {}
    data ['form'] = ContratacaoForm()
    return render (request, 'form.html', data)

def create(request):
    form = ContratacaoForm(request.POST or None)
    print(form)
    if form.is_valid():
        form.save()
        return redirect('sucesso')

def sucesso(request):
    return render(request,'sucesso.html')
>>>>>>> 62b0197 (alteracao)
