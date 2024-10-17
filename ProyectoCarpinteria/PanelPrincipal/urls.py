from django.urls import path
from PanelPrincipal.views import home

from . import views


urlpatterns = [
    path('', home, name="Home"),
    path('formulario/', views.registro, name="Rtro"),
    path('cerrar/', views.cerrar_sesion, name="cerrar"),
    path('logear/', views.iniciar_sesion, name="logear"),
    path('enviar/', views.enviar_correo, name="enviar"),
]


# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
