from .base import ValidadorFiscal
from minha_app.models import RegraFiscal

class ValidadorBrasil(ValidadorFiscal):
    def validar(self, nota):
        erros = []
        for item in nota.itens.all():
            regras = RegraFiscal.objects.filter(pais='Brasil', categoria=item.categoria, faixa_maxima__gte=item.preco)
            if not regras.exists():
                continue
            regra = regras.order_by('faixa_maxima').first()
            if item.imposto_aplicado != regra.aliquota:
                erros.append({
                    'item_id': item.id,
                    'erro': 'Alíquota incorreta',
                    'esperado': float(regra.aliquota),
                    'aplicado': float(item.imposto_aplicado),
                    'justificativa': regra.justificativa_legal
                })
        return erros
