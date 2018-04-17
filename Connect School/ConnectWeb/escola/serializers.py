from rest_framework.serializers import ModelSerializer
from .models import Escola, GerenteEscola, Professor


class EscolaSerializer(ModelSerializer):
    class Meta:
        model = Escola
        fields = '__all__'


class GerenteEscolaSerializer(ModelSerializer):
    class Meta:
        model = GerenteEscola
        fields = ('perfil_user', 'escola', 'notificacoes', 'resolviveis')


class ProfessorSerializer(ModelSerializer):
    class Meta:
        model = Professor
        fields = ('perfil_user', 'perfil_dependente', 'notificacoes', 'resolviveis')
