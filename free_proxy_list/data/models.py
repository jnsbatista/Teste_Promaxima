from django.db import models


class Data(models.Model):
    ip_address = models.CharField(max_length=25, blank=True)
    port = models.PositiveIntegerField( blank=True)
    protocol = models.CharField(max_length=6, blank=True)
    anonymity = models.CharField(max_length=15, blank=True)
    country = models.CharField(max_length=20, blank=True)
    region = models.CharField(max_length=15, blank=True)
    city = models.CharField(max_length=25, blank=True)
    uptime = models.CharField(max_length=15, blank=True)
    response = models.CharField(max_length=15, blank=True)
    transfer = models.CharField(max_length=15, blank=True)
    
    def __str__(self):
      return self.ip_address
