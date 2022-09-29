from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.

class ListaCompras(models.Model):
    proprietario = models.ForeignKey(User, on_delete= models.CASCADE)
    nome = models.CharField(max_length = 100)
    concluido = models.BooleanField(default = False)
    
    def __str__(self):
        return self.nome

class Itens(models.Model):
    nome = models.CharField(max_length=200)
    lista = models.ForeignKey(ListaCompras, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome
