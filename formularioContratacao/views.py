
from django.shortcuts import render,redirect
from formularioContratacao.forms import ContratacaoForm

def index(request):
    data = {}
    data ['index'] = ContratacaoForm()
    return render(request,'index.html', data)

def create(request):
    form = ContratacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('sucesso')



