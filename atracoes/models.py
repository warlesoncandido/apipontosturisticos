from django.db import models

class Atracao(models.Model):
    #nome da atracao
    nome = models.CharField(max_length=150)
    #descricao da atracao
    descricao = models.TextField()
    # horario de funcionamento atracao
    horario = models.TextField()
    #idade minima da atracao
    idade_minima = models.IntegerField()
    def __str__(self):
        return self.nome
