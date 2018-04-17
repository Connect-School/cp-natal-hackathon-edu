from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Mensagem)
admin.site.register(MensagemIdentificada)
admin.site.register(MensagemForum)

admin.site.register(Notificacao)

admin.site.register(Informavel)
admin.site.register(Aviso)

admin.site.register(InformavelResolvivel)
admin.site.register(Bullying)

admin.site.register(InformavelForum)
admin.site.register(InformavelForumOrganizacao)
admin.site.register(InformavelForumUsuario)