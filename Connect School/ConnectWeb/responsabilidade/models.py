from django.db import models
from polymorphic.models import PolymorphicModel


class Responsavel(PolymorphicModel):
    pass


class PaiResponsavel(Responsavel):

    def __str__(self):
        if hasattr(self, 'pai'):
            return self.pai.get_name()
        return ""


class EscolaResponsavel(Responsavel):

    def __str__(self):
        if hasattr(self, 'escola'):
            return self.escola.get_name()
        return ""


class DiredResponsavel(Responsavel):

    def __str__(self):
        if hasattr(self, 'dired'):
            return self.dired.get_name()
        return ""


class SecretariaResponsavel(Responsavel):

    def __str__(self):
        if hasattr(self, 'secretaria'):
            return self.secretaria.get_name()
        return ""


class Dependente(PolymorphicModel):
    responsavel = models.ForeignKey(Responsavel, related_name="dependentes",
                                    null=True, blank=True, on_delete=models.PROTECT)


class AlunoDependente(Dependente):

    def __str__(self):
        if hasattr(self, 'aluno'):
            return self.aluno.get_name()
        return ""


class ProfessorDependente(Dependente):

    def __str__(self):
        if hasattr(self, 'professor'):
            return self.professor.get_name()
        return ""


class GerenteEscolaDependente(Dependente):

    def __str__(self):
        if hasattr(self, 'gerente_escola'):
            return self.gerente_escola.get_name()
        return ""


class EscolaDependente(Dependente):

    def __str__(self):
        if hasattr(self, 'escola'):
            return self.escola.get_name()
        return ""


class DiredDependente(Dependente):

    def __str__(self):
        if hasattr(self, 'dired'):
            return self.dired.get_name()
        return ""


