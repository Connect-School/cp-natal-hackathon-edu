from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('public.urls')),
    path('login/', auth_views.login, {'template_name': 'login.html'}, name='login'),
    path('logout/', auth_views.logout, {'next_page': '/'}, name='logout'),
    path('api/', include("api.urls")),
    path('core/', include('core.urls')),
    path('escola/', include('escola.urls')),
    path('secretaria/', include('secretaria.urls')),
    path('dired/', include('dired.urls')),
    path('informavel/', include('informavel.urls')),
]
