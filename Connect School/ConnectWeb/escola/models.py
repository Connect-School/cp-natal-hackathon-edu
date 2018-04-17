from django.db import models
from core.models import Usuario, Organizacao, Gerente
from responsabilidade.models import EscolaResponsavel, EscolaDependente, ProfessorDependente, GerenteEscolaDependente


class Escola(Organizacao):
    perfil_responsavel = models.OneToOneField(EscolaResponsavel, related_name="escola", null=True, blank=True, on_delete=models.PROTECT)
    perfil_dependente = models.OneToOneField(EscolaDependente, related_name="escola", null=True, blank=True, on_delete=models.PROTECT)
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)
    telefone = models.CharField(max_length=16)

    def get_name(self):
        return self.nome

    def get_tipo(self):
        return "escola"

    def __str__(self):
        return self.get_name()


class GerenteEscola(Gerente):
    perfil_dependente = models.OneToOneField(GerenteEscolaDependente, related_name="gerente_escola", null=True, blank=True,
                                             on_delete=models.PROTECT)
    escola = models.ForeignKey(Escola, related_name="gerentes", null=True, blank=True, on_delete=models.PROTECT)

    def get_organizacao(self):
        return self.escola


class Professor(Usuario):
    perfil_dependente = models.OneToOneField(ProfessorDependente, related_name="professor", null=True, blank=True, on_delete=models.PROTECT)
