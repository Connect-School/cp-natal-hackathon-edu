from django.contrib import admin
from .models import Usuario, Pai, Aluno, Gerente

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Gerente)
admin.site.register(Pai)
admin.site.register(Aluno)
