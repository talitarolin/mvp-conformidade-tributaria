from django.contrib import admin  # Adicione esta linha
from django.urls import path
from minha_app.views import ValidarNotaFiscalView

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('validar-nota/', ValidarNotaFiscalView.as_view(), name='validar-nota'),
    
]