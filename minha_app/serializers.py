from rest_framework import serializers
from .models import NotaFiscal, ItemNota

class ItemNotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemNota
        fields = '__all__'

class NotaFiscalSerializer(serializers.ModelSerializer):
    itens = ItemNotaSerializer(many=True)

    class Meta:
        model = NotaFiscal
        fields = ['id', 'numero', 'pais', 'criado_em', 'itens']
