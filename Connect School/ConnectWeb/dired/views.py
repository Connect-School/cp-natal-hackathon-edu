from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from core.models import Gerente


@login_required
def index(request):
    context = {}
    context['usuario_autenticado'] = request.user.is_authenticated

    usuario = get_object_or_404(Gerente, perfil_user=request.user)

    isinstance(usuario, Gerente)

    context['organizacao'] = usuario.get_organizacao()
    context['tipo_organizacao'] = usuario.get_organizacao().get_tipo()

    context['notificacoes'] = []
    context['foruns'] = []

    return render(request, 'dired/index.html', context)
