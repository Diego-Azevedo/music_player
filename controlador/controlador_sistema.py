from view.tela_sistema import TelaInicial
from controlador.controlador_cadastro import ControladorCadastro
from controlador.controlador_player import ControladorPlayer
from controlador.controlador_registro import ControladorRegistro

class ControladorSistema:
    def __init__(self):
        self.__tela_sistema = TelaInicial()
        self.__controlador_cadastro = ControladorCadastro(self)
        self.__controlador_player = ControladorPlayer(self)
        self.__controlador_registro = ControladorRegistro(self)

    @property
    def controlador_cadastro(self):
        return self.__controlador_cadastro

    @property
    def controlador_player(self):
        return self.__controlador_player

    @property
    def controlador_registro(self):
        return self.__controlador_registro    

    def inicializa_sistema(self):
        self.abre_tela()

    def cadastra_musica(self):
        self.__controlador_cadastro.abre_tela()

    def player(self):
        self.__controlador_player.abre_tela()

    def registro(self):
        self.__controlador_registro.abre_tela()

    def sair(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_musica, 2: self.player, 3: self.registro,
                        0: self.sair}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
