class Musica:
    def __init__(self, nome: str, artista: str, genero: str, id: int, gostei = False): #lembrar de mudar o genero para abstract
        self.__nome = nome
        self.__artista = artista
        self.__genero = genero
        self.__id = id
        self.__gostei = gostei

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
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def gostei(self):
        return self.__gostei

    @gostei.setter
    def gostei(self, gostei):
        self.__gostei = gostei
