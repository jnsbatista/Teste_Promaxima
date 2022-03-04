from django.db import models


class Data(models.Model):
    tipo = models.CharField(max_length=55, blank=True)
    litro = models.CharField(max_length=15, blank=True)
    ultima_venda = models.CharField(max_length=25, blank=True)
    tempo_ultima_venda = models.CharField(max_length=25, blank=True)
    nome_empresa = models.CharField(max_length=55, blank=True)
    endereco = models.CharField(max_length=55, blank=True)
    cidade = models.CharField(max_length=55, blank=True)
    
    def __str__(self):
      return self.tipo
