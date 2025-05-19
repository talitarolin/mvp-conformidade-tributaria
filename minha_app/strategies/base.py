from abc import ABC, abstractmethod

class ValidadorFiscal(ABC):
    @abstractmethod
    def validar(self, nota):
        pass
