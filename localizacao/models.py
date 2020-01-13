from django.db import models


class Localizacao(models.Model):
    #Endereco 1
    linha1 = models.CharField(max_length=150)
    # Endereco 1
    linha2 = models.CharField(max_length=150 ,null=True ,blank=True)
    #cidade
    cidade = models.CharField(max_length=150)
    #estado
    estado = models.CharField(max_length=150)
    #pais
    pais = models.CharField(max_length=150)
    #latitude
    latitude = models.IntegerField(null=True, blank=True)
    #longitude
    longitude = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.linha1