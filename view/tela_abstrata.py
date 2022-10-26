from abc import ABC, abstractmethod

class TelaAbstrata(ABC):

    @abstractmethod
    def tela_opcoes(self):
        pass

    def mostra_mensagem(self, msg):
        print(msg)

    def quebra_linha(self):
        print()    