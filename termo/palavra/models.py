from django.db import models

# Create your models here.
class Resposta(models.Model):
    palavra = models.CharField(max_length=12)

class User(models.Model):
    username = models.CharField(max_length = 30)
    qntdRespondidas = models.IntegerField()
    level = models.IntegerField()

class Respondidas(models.Model):
    usuario = models.ForeignKey(User, on_delete = models.CASCADE)
    solved = models.ForeignKey(Resposta, on_delete = models.CASCADE)