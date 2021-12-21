from django.forms import ModelForm, fields
from formularioContratacao.models import Contratacao

class ContratacaoForm(ModelForm):
    class Meta:
        model = Contratacao
        fields = ['nomecompleto', 'dataNascimento', 'rg_cpf', 'contaNubank', 'estadoCivil', 'numeroCarteiraTrabalho', 'whatsappEmail', 'linkdlen']