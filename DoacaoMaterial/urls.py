from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('index/', include('doador.urls')),
    path('admin/', admin.site.urls),
    path('doador/', include('doador.urls')),
    path('resposta-cadastro/', include('doador.urls'))
]
