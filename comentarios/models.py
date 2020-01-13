from django.contrib.auth.models import User
from django.db import models

class Comentarios(models.Model):
    #nome nos comentarios
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    #descricao dos comentarios
    descricao = models.TextField()
    #data do comentario
    data = models.DateTimeField(auto_now_add=True)
    #aprovacao de comentarios
    aprovado = models.BooleanField(default=False)
    def __str__(self):
        return self.usuario.username
