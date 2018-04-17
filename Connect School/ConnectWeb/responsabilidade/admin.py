from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Dependente)
admin.site.register(Responsavel)

admin.site.register(PaiResponsavel)
admin.site.register(AlunoDependente)

admin.site.register(ProfessorDependente)

admin.site.register(GerenteEscolaDependente)

admin.site.register(EscolaResponsavel)
admin.site.register(EscolaDependente)

admin.site.register(DiredResponsavel)
admin.site.register(DiredDependente)

admin.site.register(SecretariaResponsavel)