from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, UsuarioViewSet, OrganizacaoViewSet


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
router.register('usuarios', UsuarioViewSet)
router.register('organizacoes', OrganizacaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
]
