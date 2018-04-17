from django.forms import ModelForm
from .models import InformavelForumUsuario, InformavelForumOrganizacao, Aviso, MensagemIdentificada, Notificacao

class InformavelForumUsuarioForm(ModelForm):
    class Meta:
        model = InformavelForumUsuario
        fields = '__all__'

class InformavelForumOrganizacaoForm(ModelForm):
    class Meta:
        model = InformavelForumOrganizacao
        fields = '__all__'

class AvisoForm(ModelForm):
    class Meta:
        model = Aviso
        fields = '__all__'

class MensagemIdentificadaForm(ModelForm):
    class Meta:
        model = MensagemIdentificada
        fields = '__all__'

class NotificacaoForm(ModelForm):
    class Meta:
        model = Notificacao
        fields = '__all__'