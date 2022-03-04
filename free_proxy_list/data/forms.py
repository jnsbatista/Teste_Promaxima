from dataclasses import fields
from pyexpat import model
from django import forms

from .models import Data

class DataForm(forms.ModelForm):
  
  class Meta:
    model = Data
    fields = ('ip_address', 'port', 'protocol', 'anonymity', 'country', 'region', 'city', 'uptime', 'response', 'transfer')