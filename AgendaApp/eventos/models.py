from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

# Create your models here.
class Evento(models.Model):
    titulo_do_evento = models.CharField(max_length=500)
    data_e_hora = models.DateTimeField(auto_now=False, auto_now_add=False)
    descricao = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.titulo_do_evento
     