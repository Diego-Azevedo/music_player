from view.tela_player import TelaPlayer
from entidade.musica import Musica
from controlador.controlador_cadastro import ControladorCadastro

class ControladorPlayer:
    def __init__(self, controlador_sistema):
        self.musicas = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_player = TelaPlayer()


    def tocar_musica_aleatoria(self):
        print("Uma música aleatória está tocando")

    def escolher_musica(self):
        print("[Erro, essa parte ainda não existe]")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.escolher_musica, 2: self.tocar_musica_aleatoria, 
                        0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_player.tela_opcoes()]()