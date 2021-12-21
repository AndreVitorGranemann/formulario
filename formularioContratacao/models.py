from django.db import models
from datetime import datetime

class Contratacao(models.Model):
    id = models.AutoField(primary_key=True)
    nomecompleto = models.CharField(max_length=200)
<<<<<<< HEAD
<<<<<<< HEAD
    dataNascimento = models.IntegerField()
=======
    dataNascimento = models.DateField()
>>>>>>> 62b0197 (alteracao)
    rg_cpf= models.TextField()
=======
    dataNascimento = models.TextField()
    rg_cpf = models.TextField()
>>>>>>> 721b641 (texte)
    contaNubank = models.TextField()
    estadoCivil = models.TextField()
    numeroCarteiraTrabalho = models.TextField()
    whatsappEmail =  models.TextField()
    linkdlen = models.TextField()
    load = models.DateTimeField(auto_now=True)