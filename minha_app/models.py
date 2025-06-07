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

class NotaFiscalAprovada(models.Model):
    nota = models.ForeignKey(NotaFiscal, on_delete=models.CASCADE, related_name='notas_aprovadas')
    status = models.CharField(max_length=20)
    data_aprovacao = models.DateTimeField(auto_now_add=True)
    motivo_rejeicao = models.TextField(null=True, blank=True)
    def __str__(self):
        return f"Nota {self.nota.numero} - {self.status}"
    
class NotaFiscalRejeitada(models.Model):
    nota = models.ForeignKey(NotaFiscal, on_delete=models.CASCADE, related_name='notas_rejeitadas')
    status = models.CharField(max_length=20)
    data_rejeicao = models.DateTimeField(auto_now_add=True)
    motivo_rejeicao = models.TextField()
    def __str__(self):
        return f"Nota {self.nota.numero} - {self.status}"
    

