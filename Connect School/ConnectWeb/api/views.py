from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response
from django.contrib.auth.models import User
from core.serializers import UserSerializer, UsuarioPolySerializer, OrganizacaoPolySerializer
from core.models import Usuario, Organizacao


class UserViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioPolySerializer


class OrganizacaoViewSet(ModelViewSet):
    queryset = Organizacao.objects.all()
    serializer_class = OrganizacaoPolySerializer

    def update(self, request, pk=None, project_pk=None):
        print(request.data['result'])

    def partial_update(self, request, *args, **kwargs):
        instance = self.queryset.get(pk=kwargs.get('pk'))
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)