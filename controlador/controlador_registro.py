from view.tela_registro import TelaRegistro

class ControladorRegistro:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_registro = TelaRegistro()

    def abre_tela(self):
        lista_opcoes = {1: self.historico_player, 2: self.limpar_lista, 
                        0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_registro.tela_opcoes()]()

    def historico_player(self):
        historico = self.__controlador_sistema.controlador_player.retorna_musicas()
        self.__tela_registro.mostra_mensagem("--------REGISTRO DO PLAYER--------")
        self.__tela_registro.quebra_linha()
        self.__tela_registro.mostra_mensagem("Histórico:")
        for index, item in enumerate(historico):
            self.__tela_registro.dados_musica(index, item)
        self.__tela_registro.quebra_linha() 

    def limpar_lista(self):
        self.__controlador_sistema.controlador_player.limpa_historico()
        self.__tela_registro.mostra_mensagem("Histórico excluído!")
        self.__tela_registro.quebra_linha() 

    def retornar(self):
        self.__controlador_sistema.abre_tela()


        

