from entidade.musica import Musica
from view.tela_abstrata import TelaAbstrata

class TelaPlayer(TelaAbstrata):


    def ler_opcao(self, mensagem: str = "", inteiros_validos: [] = None):
        while True:
            valor_lido = input(mensagem)
            try:
                inteiro = int(valor_lido)
                if inteiros_validos and inteiro not in inteiros_validos:
                    raise ValueError
                return inteiro
            except ValueError: 
                print("Selecione uma opcao valida")


    def tela_opcoes(self):
        print("____PLAYER____")
        print("1 - Escolher Música")
        print("2 - Tocar Música Aleatória")
        print("3 - Tocar Playlist")
        print("0 - Voltar")
        opcao = self.ler_opcao("Escolha a opcao: ", [0, 1, 2, 3, 3])
        print()
        return opcao

    def player_opcoes(self):
        print("____PLAYER OPCÕES____")
        print("1 - Pausar")
        print("2 - Passar Música")
        print("3 - Voltar Música")
        print("0 - Sair")
        opcao2 = self.ler_opcao("Escolha a opcao: ", [0, 1, 2, 3])
        print()
        return opcao2           

    def mostra_musica(self, nome):
        print("MÚSICA:", nome["nome"], "-", nome["artista"])
        print()

    def escolhe_opcao(self):
        opcao = int(input("Escolha a Opção: "))
        return opcao

    def pausar_musica(self):
        print("--------MÚSICA PAUSADA--------")
        input("Clique para continuar: ")
        print()

    def dados_playlist(self, index, nome):
        print(index, "-", nome)