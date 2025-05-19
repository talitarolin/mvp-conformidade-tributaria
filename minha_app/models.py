from django.db import models

from django.db import models

class NotaFiscal(models.Model):
    numero = models.CharField(max_length=20)
    pais = models.CharField(max_length=50)
    criado_em = models.DateTimeField(auto_now_add=True)

class ItemNota(models.Model):
    nota = models.ForeignKey(NotaFiscal, on_delete=models.CASCADE, related_name='itens')
    categoria = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imposto_aplicado = models.DecimalField(max_digits=5, decimal_places=2)

class RegraFiscal(models.Model):
    pais = models.CharField(max_length=50)
    categoria = models.CharField(max_length=100)
    faixa_maxima = models.DecimalField(max_digits=10, decimal_places=2)
    aliquota = models.DecimalField(max_digits=5, decimal_places=2)
    justificativa_legal = models.TextField()
# Create your models here.
