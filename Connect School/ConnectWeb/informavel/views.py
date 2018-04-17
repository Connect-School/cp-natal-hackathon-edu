from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from core.models import Gerente
from .models import Notificacao, Bullying, InformavelForum
from .forms import InformavelForumUsuarioForm, InformavelForumOrganizacaoForm, AvisoForm, MensagemIdentificadaForm, NotificacaoForm
from django.utils import timezone


@login_required
def detalhar_forum(request, id_informavel):
    context = {}
    context['usuario_autenticado'] = request.user.is_authenticated
    usuario = get_object_or_404(Gerente, perfil_user=request.user)
    isinstance(usuario, Gerente)
    context['organizacao'] = usuario.get_organizacao()
    context['tipo_organizacao'] = usuario.get_organizacao().get_tipo()

    forum = get_object_or_404(InformavelForum, pk=id_informavel)

    context['forum'] = forum
    context['variar'] = True

    return render(request, 'informavel/detalhar_forum.html', context)


@login_required
def detalhar_aviso(request, id_notificacao):
    context = {}
    context['usuario_autenticado'] = request.user.is_authenticated
    usuario = get_object_or_404(Gerente, perfil_user=request.user)
    isinstance(usuario, Gerente)
    context['organizacao'] = usuario.get_organizacao()
    context['tipo_organizacao'] = usuario.get_organizacao().get_tipo()

    notificacao = get_object_or_404(Notificacao, pk=id_notificacao)
    notificacao.read = True
    notificacao.save()

    context['aviso'] = notificacao.aviso

    return render(request, 'informavel/detalhar_aviso.html', context)


@login_required
def detalhar_bullying(request, id_informavel):
    context = {}
    context['usuario_autenticado'] = request.user.is_authenticated
    usuario = get_object_or_404(Gerente, perfil_user=request.user)
    isinstance(usuario, Gerente)
    context['organizacao'] = usuario.get_organizacao()
    context['tipo_organizacao'] = usuario.get_organizacao().get_tipo()

    bullying = get_object_or_404(Bullying, pk=id_informavel)
    bullying.read = True
    bullying.save()

    context['bullying'] = bullying

    return render(request, 'informavel/detalhar_bullying.html', context)

@login_required
def cadastrar_forum_usuario(request):
    context = {}
    context['usuario_autenticado'] = request.user.is_authenticated
    usuario = get_object_or_404(Gerente, perfil_user=request.user)
    isinstance(usuario, Gerente)
    context['organizacao'] = usuario.get_organizacao()
    context['tipo_organizacao'] = usuario.get_organizacao().get_tipo()

    context['tipo'] = 'Forum Usuario'

    if request.method == "POST":
        form = InformavelForumUsuarioForm(request.POST)
        context['form'] = form
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('/{}'.format(context['tipo_organizacao']))

    else:
        form = InformavelForumUsuarioForm()
        context['form'] = form
        return render(request, "informavel/cadastrar_forum.html", context)

@login_required
def cadastrar_forum_organizacao(request):
    context = {}
    context['usuario_autenticado'] = request.user.is_authenticated
    usuario = get_object_or_404(Gerente, perfil_user=request.user)
    isinstance(usuario, Gerente)
    context['organizacao'] = usuario.get_organizacao()
    context['tipo_organizacao'] = usuario.get_organizacao().get_tipo()

    context['tipo'] = 'Forum Organização'

    if request.method == "POST":
        form = InformavelForumOrganizacaoForm(request.POST)
        context['form'] = form
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('/{}'.format(context['tipo_organizacao']))

    else:
        form = InformavelForumOrganizacaoForm()
        context['form'] = form
        return render(request, "informavel/cadastrar_forum.html", context)

@login_required
def cadastrar_aviso(request):
    context = {}
    context['usuario_autenticado'] = request.user.is_authenticated
    usuario = get_object_or_404(Gerente, perfil_user=request.user)
    isinstance(usuario, Gerente)
    context['organizacao'] = usuario.get_organizacao()
    context['tipo_organizacao'] = usuario.get_organizacao().get_tipo()

    context['tipo'] = 'Aviso'

    form_aviso = AvisoForm(prefix='aviso')
    form_mensagem = MensagemIdentificadaForm(prefix='mensagem')
    form_notificacao = NotificacaoForm(prefix='notificacao')

    if request.method == "POST":
        form_aviso = AvisoForm(request.POST, prefix='aviso')
        form_mensagem = MensagemIdentificadaForm(request.POST, prefix='mensagem')
        form_notificacao = NotificacaoForm(request.POST, prefix='notificacao')


        context['form_aviso'] = form_aviso
        context['form_mensagem'] = form_mensagem
        context['form_notificacao'] = form_notificacao

        if form_aviso.is_valid() and form_notificacao.is_valid() and form_notificacao.is_valid():
            # Prepare the school model, but don't commit it to the database
            # just yet.
            # school = form.save(commit=False)

            # Add the location ForeignKey by saving the secondary form we
            # setup
            # school.location = sub_form.save()

            # Save the main object and continue on our merry way.
            # school.save()
            # return _goto_school(school)

            # model_instance = form.save(commit=False)
            # model_instance.timestamp = timezone.now()
            # model_instance.save()
            return redirect('/{}'.format(context['tipo_organizacao']))

    else:
        form_aviso = AvisoForm(prefix='aviso')
        form_mensagem = MensagemIdentificadaForm(prefix='mensagem')
        form_notificacao = NotificacaoForm(prefix='notificacao')

        context['form_aviso'] = form_aviso
        context['form_mensagem'] = form_mensagem
        context['form_notificacao'] = form_notificacao

        return render(request, "informavel/cadastrar_aviso.html", context)
