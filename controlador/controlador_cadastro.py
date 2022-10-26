from entidade.musica import Musica
from view.tela_cadastro import TelaCadastro
import random

class ControladorCadastro():

    def __init__(self, controlador_sistema):
            self.__musicas = [musica0, musica1, musica2, musica3, musica4]
            self.__tela_cadastro = TelaCadastro()
            self.__controlador_sistema = controlador_sistema

    def pega_musica_por_nome(self, nome: str):
        for musica in self.__musicas:
            if(musica.nome == nome):
                return musica
            return None
    
    #mostra a lista de músicas cadastradas
    def ver_musica(self):
        for musica in self.__musicas:
            self.__tela_cadastro.mostra_musica({"nome": musica.nome, "artista": musica.artista,
             "genero": musica.genero, "tempo": musica.tempo })

    def incluir_musica(self):
        self.__tela_cadastro.mostra_mensagem("--------CADASTRAR MÚSICA--------")
        dados_musica = self.__tela_cadastro.pega_dados_musica()
        musica = Musica(dados_musica["nome"], dados_musica["artista"], dados_musica["genero"], dados_musica["tempo"])
        self.__musicas.append(musica)

    def editar_musica(self):
        self.__tela_cadastro.mostra_mensagem("--------EDITAR MÚSICA--------")
        self.ver_musica()
        nome_musica = self.__tela_cadastro.edita_musica()
        for indice in self.__musicas:
            if indice.nome == nome_musica:
                novos_dados_musica = self.__tela_cadastro.pega_dados_musica()
                indice.nome = novos_dados_musica["nome"]
                indice.artista = novos_dados_musica["artista"]
                indice.genero = novos_dados_musica["genero"]
                indice.tempo = novos_dados_musica["tempo"]
                self.__tela_cadastro.mostra_mensagem("MÚSICA EDITADA COM SUCESSO!")
                ####CORRIGIR ELSE#### 
            #else:
            #   self.__tela_cadastro.mostra_mensagem("Música não existe")
     
    #TRATAR EXCEÇÃO
    def excluir_musica(self):
        self.__tela_cadastro.mostra_mensagem("--------EXCLUIR MÚSICA--------")
        self.ver_musica()
        nome_musica = self.__tela_cadastro.exclui_musica()
        for index, indice in enumerate(self.__musicas):
            if indice.nome == nome_musica:
                self.__musicas.pop(index)
                self.__tela_cadastro.mostra_mensagem("MÚSICA EXCLUÍDA!")
                self.__tela_cadastro.quebra_linha()

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
        return {"nome": musica_aleatoria.nome, "artista": musica_aleatoria.artista}

    def retorna_musicas(self):
        lista_musicas = []
        for musica in self.__musicas:
            lista_musicas.append({"nome": musica.nome, "artista": musica.artista})
        return lista_musicas       
        

#Musicas cadastradas
musica0 = Musica("TôBem", "Djonga", "Rap", 3.21)
musica1 = Musica("Hey Baby", "Stephen Marley", "Reggae", 4.54)
musica2 = Musica("You And Me", "Soja", "Reggae", 4.50)
musica3 = Musica("November Rain", "Guns N Roses", "Rock", 8.10)
musica4 = Musica("505", "Arctic Monkeys", "Rock", 4.13)
