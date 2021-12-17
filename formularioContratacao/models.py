from django.db import models

class Contratacao(models.Model):
    id = models.AutoField(primary_key=True)
    nomecompleto = models.CharField(max_length=200)
    dataNascimento = models.IntegerField()
    rg_cpf= models.TextField()
    contaNubank = models.TextField()
    estadoCivil = models.TextField()
    numeroCarteiraTrabalho = models.TextField()
    whatsappEmail =  models.TextField()
    linkdlen = models.TextField()
    load = models.DateTimeField(auto_now=True)