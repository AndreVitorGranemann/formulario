from django.shortcuts import render,redirect
from formularioContratacao.forms import ContratacaoForm
from formularioContratacao.models import Contratacao

def index(request):
    data = {}
    data['db'] = Contratacao.objects.all()
    return render(request,'index.html', data)

def form(request):
    data = {}
    data['form'] =  ContratacaoForm()
    return render(request,'form.html', data)
    
def create(request):
    form = ContratacaoForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('index')


def view(request, pk):
    data = {}
    data['db'] = Contratacao.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Contratacao.objects.get(pk=pk)
    data['form'] = ContratacaoForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Contratacao.objects.get(pk=pk)
    form = ContratacaoForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('index')
def delete(request, pk):
    db = Contratacao.objects.get(pk=pk)
    db.delete()
    return redirect('index')
