from abc import ABC, abstractmethod

class TelaAbstrata(ABC):

    def ler_opcao(self, mensagem: str = "", inteiros_validos: [] = None):
        while True:
            valor_lido = input(mensagem)
            try:
                inteiro = int(valor_lido)
                if inteiros_validos and inteiro not in inteiros_validos:
                    raise ValueError
                return inteiro
            except ValueError: 
                print("SELECIONE UMA OPÇÃO VÁLIDA")

    @abstractmethod
    def tela_opcoes(self):
        pass

    def dados_musica(self, index, dados_musica):
        print(index, "-", dados_musica["nome"], "-", dados_musica["artista"])   

    def mostra_mensagem(self, msg):
        print(msg)

    def quebra_linha(self):
        print()    
