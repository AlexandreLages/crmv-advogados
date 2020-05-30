from django.db import models
from django.contrib.auth.models import User


class Advogado(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=True, default='')
    celular = models.CharField(max_length=255, null=True, default='')
    cpf = models.CharField(max_length=255, null=True, default='')
    rg = models.CharField(max_length=255, null=True, default='')
    oab = models.CharField(max_length=255, null=True, default='')
    curriculo = models.TextField(null=True, default='')

    class Meta:
        db_table = 'tbAdvogado'

    def __str__(self):
        return 'Advogado:' + self.nome