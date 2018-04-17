from django.db import models
from polymorphic.models import PolymorphicModel
from core.models import Usuario, Organizacao
from responsabilidade.models import Responsavel
from model_utils import Choices


class Mensagem(PolymorphicModel):
    texto = models.CharField(max_length=255)
    data = models.DateTimeField()

    def __str__(self):
        return "Mensagem ({})".format(self.pk)


class MensagemIdentificada(Mensagem):
    criador = models.ForeignKey(Usuario, related_name="mensagens_identificadas", on_delete=models.CASCADE)

    def __str__(self):
        return "Mensagem ({}) de {}".format(self.pk, self.criador.get_name())


class Informavel(PolymorphicModel):

    def __str__(self):
        return "Informavel ({})".format(self.pk,)


class Aviso(Informavel):
    mensagem = models.OneToOneField(MensagemIdentificada, related_name="aviso", null=True, blank=True,
                                    on_delete=models.PROTECT)

    def __str__(self):
        return "Aviso ({}) de {}".format(self.pk, self.mensagem.criador.get_name())


class Notificacao(models.Model):
    usuario = models.ForeignKey(Usuario, related_name="notificacoes", on_delete=models.CASCADE)
    aviso = models.ForeignKey(Aviso, related_name="notificacoes", null=True, blank=True, on_delete=models.PROTECT)
    read = models.BooleanField(default=False)

    def __str__(self):
        return "Notificacao: {}\n".format(self.aviso)


class InformavelResolvivel(Informavel):
    encarregado = models.ForeignKey(Usuario, related_name="resolviveis", null=True, blank=True,
                                    on_delete=models.CASCADE)
    read = models.BooleanField(default=False)

    @property
    def is_bullying(self):
        if isinstance(self, Bullying):
            return True
        return False

    def __str__(self):
        return "Informavel resolvivel ({})".format(self.pk)


class Bullying(InformavelResolvivel):

    mensagem = models.OneToOneField(Mensagem, related_name="bullying", null=True, blank=True, on_delete=models.PROTECT)
    # TODO AssuntoUsuario (?)


    def __str__(self):
        return "Mensagem anônima ({}) para {}".format(self.pk, self.encarregado.get_name())


class InformavelForum(InformavelResolvivel):
    responsavel = models.ForeignKey(Responsavel, related_name="foruns", null=True, blank=True,
                                    on_delete=models.CASCADE)
    criador = models.ForeignKey(Usuario, related_name="foruns_criados", on_delete=models.CASCADE)
    TIPO = Choices(('reclamacao', ('Reclamação')), ('sugestao', ('Sugestão')), ('solicitacao', ('Solicitação')))
    tipo = models.CharField(choices=TIPO, default=TIPO.reclamacao, max_length=11)

    def usuario_has_access(self, usuario):
        return None

    def __str__(self):
        return "Forum ({})".format(self.pk)


class MensagemForum(MensagemIdentificada):
    forum = models.ForeignKey(InformavelForum, related_name="mensagens", on_delete=models.CASCADE)

    def __str__(self):
        return "Mensagem ({}) de {} para forum ({})".format(self.pk, self.criador.get_name(), self.forum.pk)


class InformavelForumOrganizacao(InformavelForum):
    assunto = models.ForeignKey(Organizacao, related_name="foruns_organizacao", on_delete=models.CASCADE)

    def usuario_has_access(self, usuario):
        if usuario.get_organizacao() == self.assunto:
            return True
        return False

    def __str__(self):
        return "Forum ({}) de {} sobre {}".format(self.pk, self.tipo, self.assunto)

class InformavelForumUsuario(InformavelForum):
    assunto = models.ForeignKey(Usuario, related_name="foruns_usuario", on_delete=models.CASCADE)

    def usuario_has_access(self, usuario):
        if self.tipo == 'reclamacao':
            if usuario == self.assunto:
                return False
        return True

    def __str__(self):
        return "Forum ({}) de {} sobre {}".format(self.pk, self.tipo, self.assunto)