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
    funcao = models.CharField(max_length=50, null=True, default='')

    usa_twitter = models.BooleanField(default=False)
    usa_facebook = models.BooleanField(default=False)
    usa_instagram = models.BooleanField(default=False)
    usa_whatsapp = models.BooleanField(default=False)
    usa_linkdin = models.BooleanField(default=False)

    url_twitter = models.CharField(max_length=255, null=True, default='')
    url_facebook = models.CharField(max_length=255, null=True, default='')
    url_instagram = models.CharField(max_length=255, null=True, default='')
    url_whatsapp = models.CharField(max_length=255, null=True, default='')
    url_linkdin = models.CharField(max_length=255, null=True, default='')

    foto = models.ImageField(upload_to='imagens/', blank = True, null = True)

    class Meta:
        db_table = 'tbAdvogado'

    def __str__(self):
        return 'Advogado:' + self.nome


class PaginaInicial(models.Model):
    email_principal = models.CharField(max_length=255, null=True, default='')
    telefone_principal = models.CharField(max_length=255, null=True, default='')

    usa_twitter = models.BooleanField(default=False)
    url_twitter = models.CharField(max_length=255, null=True, default='')
    usa_facebook = models.BooleanField(default=False)
    url_facebook = models.CharField(max_length=255, null=True, default='')
    usa_instagram = models.BooleanField(default=False)
    url_instagram = models.CharField(max_length=255, null=True, default='')
    usa_whatsapp = models.BooleanField(default=False)
    url_whatsapp = models.CharField(max_length=255, null=True, default='')
    usa_linkdin = models.BooleanField(default=False)
    url_linkdin = models.CharField(max_length=255, null=True, default='')

    titulo = models.CharField(max_length=50, null=False)
    titulo_sobre = models.CharField(max_length=255, null=False)
    mensagem_sobre = models.CharField(max_length=3000, null=False)
    imagem_sobre = models.ImageField(upload_to='imagens/', blank = True, null = True)

    class Meta:
        db_table = 'tbPaginaInicial'


class Carrocel(models.Model):
    titulo = models.CharField(max_length = 50, null = False)
    mensagem = models.CharField(max_length = 1000, null = True, default='')
    imagem = models.ImageField(upload_to='imagens/', blank = True, null = True)
    pagina_inicial = models.ForeignKey(PaginaInicial, on_delete=models.DO_NOTHING, related_name = 'carroceis')

    class Meta:
        db_table = 'tbCarrocel'