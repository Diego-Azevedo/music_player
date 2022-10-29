from abc import ABC, abstractmethod

class TelaAbstrata(ABC):

    @abstractmethod
    def tela_opcoes(self):
        pass

    def dados_musica(self, index, dados_musica):
        print(index, "-", dados_musica["nome"], "-", dados_musica["artista"])   

    def mostra_mensagem(self, msg):
        print(msg)

    def quebra_linha(self):
        print()    