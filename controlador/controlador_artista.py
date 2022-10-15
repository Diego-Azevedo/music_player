from view.tela_artista import TelaArtista
from entidade.artista import Artista

class ControladorArtista():
    
    def __init__(self, controlador_sistema):
        self.__artistas = []
        self.__tela_artista = TelaArtista()
        self.__controlador_sistema = controlador_sistema
    
    def ver_artistas(self):
        pass

    def incluir_artista(self):
     dados_artista = self.__tela_artista.pega_dados_artista()
     Artista = Artista(dados_artista["nome"], dados_artista["genero"])
     self.__artistas.append(Artista)

    def editar_artista(self):
        pass

    def excluir_artista(self):
        pass

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.ver_artistas, 2: self.incluir_artista, 3: self.editar_artista, 4: self.excluir_artista, 
                        0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_artista.tela_opcoes()]()