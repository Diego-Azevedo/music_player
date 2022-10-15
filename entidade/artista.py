class Artista:
    def __init__(self, nome: str, genero: str):
        self.__nome = nome
        self.__genero = genero

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome
    
    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, genero: str):
        self.__genero = genero
