
class TelaInicial:
    def tela_opcoes(self):
        print("____PlayerDeMusica____")
        print("Escolha uma opção")
        print("1 - Artista")
        print("2 - Genero")
        print("3 - Musica")
        print("0 - Sair")
        opcao = int(input("Escolha a opcao:"))
        return opcao

class ControladorSistema:
    def __init__(self):
        self.__tela_sistema = TelaInicial()

    def inicializa_sistema(self):
        self.abre_tela()
    
    def artista(self):
        self.abre_tela
    
    def genero(self):
        self.abre_tela

    def musica(self):
        self.abre_tela

    def sair(self):
        self.abre_tela

    def abre_tela(self):
        lista_opcoes = {1: self.artista, 2: self.genero, 3: self.musica,
                        0: self.sair}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()


if __name__ == "__main__":
    ControladorSistema().inicializa_sistema()