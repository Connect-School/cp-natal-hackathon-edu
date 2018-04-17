from django.db import models
from core.models import Organizacao, Gerente
from responsabilidade.models import DiredResponsavel, DiredDependente

# Create your models here.
class Dired(Organizacao):
    perfil_responsavel = models.OneToOneField(DiredResponsavel, related_name="dired", null=True, blank=True, on_delete=models.PROTECT)
    perfil_dependente = models.OneToOneField(DiredDependente, related_name="dired", null=True, blank=True,
                                             on_delete=models.PROTECT)
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)
    telefone = models.CharField(max_length=16)

    def get_name(self):
        return self.nome

    def get_tipo(self):
        return 'dired'

    def __str__(self):
        return self.get_name()


class GerenteDired(Gerente):
    dired = models.ForeignKey(Dired, related_name="gerentes", null=True, blank=True, on_delete=models.PROTECT)

    def get_organizacao(self):
        return self.dired