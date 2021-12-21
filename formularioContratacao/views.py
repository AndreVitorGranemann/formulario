
from django.shortcuts import render,redirect
from formularioContratacao.forms import ContratacaoForm

def index(request):
    return render(request,'index.html')

def form(request):
    data = {}
    data['form'] =  ContratacaoForm()
    return render(request,'form.html', data)
    
def create(request):
    form = ContratacaoForm(request.POST or None)
    form.save()
    return redirect('index')




