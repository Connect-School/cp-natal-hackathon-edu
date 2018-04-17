from rest_framework.serializers import ModelSerializer
from .models import Dired, GerenteDired


class DiredSerializer(ModelSerializer):
    class Meta:
        model = Dired
        fields = '__all__'


class GerenteDiredSerializer(ModelSerializer):
    class Meta:
        model = GerenteDired
        fields = ('perfil_user', 'dired', 'notificacoes', 'resolviveis')
