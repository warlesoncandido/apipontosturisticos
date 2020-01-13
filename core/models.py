from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentarios
from avaliacao.models import Avaliacao
from localizacao.models import Localizacao

class PontosTuristicos(models.Model) :
    #nome do ponto turistico
    nome = models.CharField(max_length=150)
    # descricao do ponto turistico
    descricao = models.TextField()
    # aprovaçao do ponto turistico
    aprovado = models.BooleanField(default=False)
    # Lista M2M de atracoes
    atracoes = models.ManyToManyField(Atracao)
    # Lista M2M de comentarios
    comentarios = models.ManyToManyField(Comentarios)
    # Lista M2M de avaliacao
    avaliacao = models.ManyToManyField(Avaliacao)
    #localizacao do Ponto turistico
    localizacao = models.ForeignKey(Localizacao, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome