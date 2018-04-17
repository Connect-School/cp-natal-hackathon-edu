from rest_polymorphic.serializers import PolymorphicSerializer
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from django.contrib.auth.models import User
from .models import Organizacao, Usuario, Pai, Aluno
from dired.models import Dired, GerenteDired
from dired.serializers import DiredSerializer, GerenteDiredSerializer
from secretaria.models import Secretaria, GerenteSecretaria
from secretaria.serializers import SecretariaSerializer, GerenteSecretariaSerializer
from escola.models import Escola, GerenteEscola, Professor
from escola.serializers import EscolaSerializer, GerenteEscolaSerializer, ProfessorSerializer


class OrganizacaoSerializer(ModelSerializer):
    class Meta:
        model = Organizacao
        fields = '__all__'


class OrganizacaoPolySerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        Organizacao: OrganizacaoSerializer,
        Dired: DiredSerializer,
        Secretaria: SecretariaSerializer,
        Escola: EscolaSerializer
    }


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'is_staff')


class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('perfil_user')


class PaiSerializer(ModelSerializer):
    class Meta:
        model = Pai
        fields = ('perfil_user', 'perfil_responsavel', 'notificacoes', 'resolviveis')


class AlunoSerializer(ModelSerializer):
    class Meta:
        model = Aluno
        fields = ('perfil_user', 'perfil_dependente', 'notificacoes', 'resolviveis')


class UsuarioPolySerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        Usuario: UsuarioSerializer,
        Pai: PaiSerializer,
        Aluno: AlunoSerializer,
        Professor: ProfessorSerializer,
        GerenteEscola: GerenteEscolaSerializer,
        GerenteSecretaria: GerenteSecretariaSerializer,
        GerenteDired: GerenteDiredSerializer
    }
