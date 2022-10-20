
from view.tela_sistema import TelaInicial
#from controlador.controlador_artista import ControladorArtista
from controlador.controlador_cadastro import ControladorCadastro

class ControladorSistema:
    def __init__(self):
        self.__tela_sistema = TelaInicial()
        self.__controlador_cadastro = ControladorCadastro(self)

    @property
    def controlador_artista(self):
        return self.__controlador_cadastro

    def inicializa_sistema(self):
        self.abre_tela()
    
    def cadastra_musica(self):
        self.__controlador_cadastro.abre_tela()
    
    def genero(self):
        self.abre_tela

    def musica(self):
        self.abre_tela

    def sair(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_musica, 2: self.genero, 3: self.musica,
                        0: self.sair}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()