from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {}
    context['usuario_autenticado'] = request.user.is_authenticated

    return render(request, 'public/index.html', context)
