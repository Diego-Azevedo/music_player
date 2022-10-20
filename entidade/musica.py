#from genero import Genero

class Musica:
    def __init__(self, nome: str, artista: str, genero: str, tempo: float): #lembrar de mudar o genero para abstract
        self.__nome = nome
        self.__artista = artista
        self.__genero = genero
        self.__tempo = tempo

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome
    
    @property
    def artista(self):
        return self.__artista

    @artista.setter
    def artista(self, artista: str):
        self.__artista = artista

    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, genero: str):
        self.__genero = genero
    

    @property
    def tempo(self):
        return self.__tempo

    @tempo.setter
    def tempo(self, tempo: float):
        self.__tempo = tempo
