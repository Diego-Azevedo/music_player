from re import M
from entidade.musica import Musica
from view.tela_cadastro import TelaCadastro
import random

class ControladorCadastro():

    def __init__(self, controlador_sistema):
            self.__musicas = [musica0, musica1, musica2, musica3, musica4,
                              musica5, musica6, musica7, musica8, musica9]
            self.__tela_cadastro = TelaCadastro()
            self.__controlador_sistema = controlador_sistema

    def pega_musica_por_nome(self, nome: str):
        for musica in self.__musicas:
            if(musica.nome == nome):
                return musica
        return None

    def ver_musica(self):
        dados_musica = [] 
        for musica in self.__musicas:
            dados_musica.append({"nome": musica.nome, "artista": musica.artista,
             "genero": musica.genero, "tempo": musica.tempo })
        self.__tela_cadastro.mostra_musica(dados_musica)

    '''def incluir_musica(self):
        self.__tela_cadastro.mostra_mensagem("--------CADASTRAR MÚSICA--------")
        dados_musica = self.__tela_cadastro.pega_dados_musica()
        musica = Musica(dados_musica["nome"], dados_musica["artista"], dados_musica["genero"], dados_musica["tempo"])
        if dados_musica["nome"] != "" and dados_musica["artista"] != "" and dados_musica["genero"] != "" and dados_musica["tempo"] != "":
            self.__musicas.append(musica)
        else:
            self.__tela_cadastro.mostra_mensagem("PREENCHA TODOS OS CAMPOS \n")'''

    def incluir_musica(self):
        dados_musica = self.__tela_cadastro.pega_dados_musica()
        musica = Musica(dados_musica["nome"], dados_musica["artista"], dados_musica["genero"], dados_musica["tempo"])
        self.__musicas.append(musica)

    def editar_musica(self):
        self.ver_musica()
        nome = self.__tela_cadastro.seleciona_musica()
        musica = self.pega_musica_por_nome(nome)

        if(musica is not None):
            novos_dados_musica = self.__tela_cadastro.pega_dados_musica()
            musica.nome = novos_dados_musica["nome"]
            musica.artista = novos_dados_musica["artista"]
            musica.genero = novos_dados_musica["genero"]
            musica.tempo = novos_dados_musica['tempo']
            self.ver_musica()
        else:
            self.__tela_cadastro.mostra_mensagem("ATENCAO: música não existente")

    def excluir_musica(self):
        self.ver_musica()
        nome_musica = self.__tela_cadastro.seleciona_musica()
        musica = self.pega_musica_por_nome(nome_musica)

        if(musica is not None):
            self.__musicas.remove(musica)
            self.ver_musica()
        else:
            self.__tela_cadastro.mostra_mensagem("ATENCAO: música não existente")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.ver_musica, 2: self.incluir_musica, 3: self.editar_musica, 4: self.excluir_musica, 
                        0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_cadastro.tela_opcoes()]()

    def retorna_musica_aleatoria(self):
        musica_aleatoria = random.choice(self.__musicas)
        return musica_aleatoria

    def retorna_musicas(self):
        musicas = self.__musicas
        return musicas

    def retorna_objetos_musica(self):
        return self.__musicas           

#Musicas cadastradas
musica0 = Musica("TôBem", "Djonga", "Rap", 3.21)
musica1 = Musica("Hey Baby", "Stephen Marley", "Reggae", 4.54)
musica2 = Musica("You And Me", "Soja", "Reggae", 4.50)
musica3 = Musica("After Midnight", "Eric Clapton", "Rock", 8.10)
musica4 = Musica("505", "Arctic Monkeys", "Rock", 4.13)
musica5 = Musica("November Rain", "Guns N Roses", "Rock", 3.21)
musica6 = Musica("Sweet Child O' Mine", "Guns N Roses", "Rock", 4.54)
musica7 = Musica("Psychosocial", "Slipknot", "Rock", 4.50)
musica8 = Musica("Unsainted", "Slipknot", "Rock", 8.10)
musica9 = Musica("Come As You Are", "Nirvana", "Rock", 4.13)
