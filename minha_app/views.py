from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import NotaFiscal
from .serializers import NotaFiscalSerializer
from .strategies.brasil import ValidadorBrasil
from .strategies.argentina import ValidadorArgentina
from .strategies.alemanha import ValidadorAlemanha

class ValidarNotaFiscalView(APIView):
    def get_strategy(self, pais):
        if pais == 'Brasil':
            return ValidadorBrasil()
        elif pais == 'Argentina':
            return ValidadorArgentina()
        elif pais == 'Alemanha':
            return ValidadorAlemanha()
        else:
            raise NotImplementedError('Validador não implementado para este país')

    def post(self, request):
        serializer = NotaFiscalSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        nota = serializer.save()
        strategy = self.get_strategy(nota.pais)
        erros = strategy.validar(nota)
        return Response({'erros': erros})
