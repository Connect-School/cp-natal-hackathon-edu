from django.urls import path

from . import views

urlpatterns = [
    path('detalhar/forum/<id_informavel>', views.detalhar_forum, name='detalhar_forum'),
    path('cadastrar/forum/usuario', views.cadastrar_forum_usuario, name='cadastrar_forum_usuario'),
    path('cadastrar/forum/organizacao', views.cadastrar_forum_organizacao, name='cadastrar_forum_organizacao'),
    path('cadastrar/aviso', views.cadastrar_aviso, name='cadastrar_aviso'),
    path('detalhar/aviso/<id_notificacao>', views.detalhar_aviso, name='detalhar_aviso'),
    path('detalhar/bullying/<id_informavel>', views.detalhar_bullying, name='detalhar_bullying'),
]