from entidade.musica import Musica

class Playlist:
    def __init__(self, nome: str, lista_musicas: list[Musica]):
        self.__nome = nome
        self.__lista_musicas = lista_musicas

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def lista_musicas(self):
        return self.__lista_musicas

    @lista_musicas.setter
    def musicas(self, lista_musicas: list[Musica]):
        self.lista_musicass = lista_musicas
