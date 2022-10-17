import string
from view.tela_artista import TelaArtista
from entidade.artista import Artista

class ControladorArtista():
    
    def __init__(self, controlador_sistema):
        self.__artistas = []
        self.__tela_artista = TelaArtista()
        self.__controlador_sistema = controlador_sistema

    def pega_artista_por_nome(self, nome: string):
        for artista in self.__artistas:
            if(artista.nome == nome):
                return artista
            return None
    
    #mostra a lista de artistas cadastrados
    def ver_artistas(self):
        for artista in self.__artistas:
            self.__tela_artista.mostra_artista({"nome": artista.nome, "genero": artista.genero})

    def incluir_artista(self):
     dados_artista = self.__tela_artista.pega_dados_artista()
     artista = Artista(dados_artista["nome"], dados_artista["genero"])
     self.__artistas.append(artista)

    def editar_artista(self):
        self.ver_artistas()
        nome_artista = self.__tela_artista.seleciona_artista()
        artista = self.pega_artista_por_nome(nome_artista)

        if(artista is not None):
            novos_dados_artista = self.__tela_artista.pega_dados_artista()
            artista.nome = novos_dados_artista["nome"]
            artista.genero = novos_dados_artista["genero"]
            self.ver_artistas()
        else:
            self.__tela_artista.mostra_mensagem("Artista não existe")

    def excluir_artista(self):
        self.ver_artistas()
        nome_artista = self.__tela_artista.seleciona_artista()
        artista = self.pega_artista_por_nome(nome_artista)

        if(artista is not None):
            self.__artistas.remove(artista)
            self.ver_artistas()
        else:
            self.__tela_artista.mostra_mensagem("Artista não existe")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.ver_artistas, 2: self.incluir_artista, 3: self.editar_artista, 4: self.excluir_artista, 
                        0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_artista.tela_opcoes()]()