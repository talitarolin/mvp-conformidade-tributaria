from django.urls import path
from minha_app.views import ValidarNotaFiscalView

urlpatterns = [
    # outras rotas...
    path('validar-nota/', ValidarNotaFiscalView.as_view(), name='validar-nota'),
]
