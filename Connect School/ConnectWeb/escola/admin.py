from django.contrib import admin
from .models import GerenteEscola, Escola, Professor

# Register your models here.
admin.site.register(Escola)
admin.site.register(GerenteEscola)
admin.site.register(Professor)