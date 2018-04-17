from rest_framework.serializers import ModelSerializer
from .models import Secretaria, GerenteSecretaria


class SecretariaSerializer(ModelSerializer):
    class Meta:
        model = Secretaria
        fields = '__all__'


class GerenteSecretariaSerializer(ModelSerializer):
    class Meta:
        model = GerenteSecretaria
        fields = ('perfil_user', 'secretaria', 'notificacoes', 'resolviveis')
