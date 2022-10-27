from view.tela_registro import TelaRegistro

class ControladorRegistro:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_registro = TelaRegistro()

    def abre_tela(self):
        lista_opcoes = {1: self.ultimas_musicas_tocadas, 2: self.limpar_lista, 
                        0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_registro.tela_opcoes()]()    

    def ultimas_musicas_tocadas(self):
        pass

    def limpar_lista(self):
        pass

    def retornar(self):
        self.__controlador_sistema.abre_tela()


        

