from django.db import models
from datetime import datetime

class Contratacao(models.Model):
    id = models.AutoField(primary_key=True)
    nomecompleto = models.CharField(max_length=200)
    dataNascimento = models.CharField(max_length=200)
    rg_cpf = models.CharField(max_length=200)
    contaNubank = models.CharField(max_length=200)
    estadoCivil = models.CharField(max_length=200)
    numeroCarteiraTrabalho = models.CharField(max_length=200)
    whatsappEmail =  models.CharField(max_length=200)
    linkdlen = models.CharField(max_length=200)
    load = models.DateTimeField(auto_now=True)