from dataclasses import fields
from pyexpat import model
from django import forms

from .models import Data

class DataForm(forms.ModelForm):
  
  class Meta:
    model = Data
    fields = ('tipo', 'litro', 'ultima_venda', 'tempo_ultima_venda', 'nome_empresa', 'endereco', 'cidade')
    ordering = ["tipo"]
