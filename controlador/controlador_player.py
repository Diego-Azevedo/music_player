from view.tela_player import TelaPlayer

class ControladorPlayer:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_player = TelaPlayer()


    def tocar_musica_aleatoria(self):
        musica_aleatoria = self.__controlador_sistema.controlador_cadastro.retorna_musica_aleatoria()
        self.__tela_player.mostra_musica(musica_aleatoria)


    def escolher_musica(self):
        lista_musicas = self.__controlador_sistema.controlador_cadastro.retorna_musicas()
        self.__tela_player.print_escolher_musica()
        for index, item in enumerate(lista_musicas):
            self.__tela_player.escolhe_musica(index, item)
        opcao_escolhida = self.__tela_player.escolhe_opcao()       
        self.__tela_player.quebra_linha()
        self.__tela_player.mostra_musica(lista_musicas[opcao_escolhida])    

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.escolher_musica, 2: self.tocar_musica_aleatoria, 
                        0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_player.tela_opcoes()]()