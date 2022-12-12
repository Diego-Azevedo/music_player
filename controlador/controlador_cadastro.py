from re import M
from entidade.musica import Musica
from view.tela_cadastro import TelaCadastro
from Dao.dao_musica import MusicaDAO
import random

class ControladorCadastro():

    def __init__(self, controlador_sistema):
            self.__musica_DAO = MusicaDAO()
            self.__tela_cadastro = TelaCadastro()
            self.__controlador_sistema = controlador_sistema


    def pega_musica_por_id(self, id: int):
        for musica in self.__musica_DAO.get_all():
            if(musica.id == id):
                return musica
        return None

    def ver_musica(self):
        dados_musica = [] 
        for musica in self.__musica_DAO.get_all():  
            dados_musica.append({"nome": musica.nome, "artista": musica.artista,
             "genero": musica.genero, "id": musica.id })
        if len(dados_musica) == 0:
            self.__tela_cadastro.mostra_mensagem("NÃO HÁ NENHUMA MÚSICA CADASTRADA")
        self.__tela_cadastro.mostra_musica(dados_musica)
        #for musica in self.__musicas:
        #for musica in self.__musica_DAO.get_all():    
        #    self.__tela_cadastro.mostra_musica({"nome": musica.nome, "artista": musica.artista,
        #     "genero": musica.genero, "id": musica.id })

    def incluir_musica(self):

        dados_musica = self.__tela_cadastro.pega_dados_musica()
        musica = Musica(dados_musica["nome"], dados_musica["artista"], dados_musica["genero"], dados_musica["id"])
        if dados_musica["nome"] != "" and dados_musica["artista"] != "" and dados_musica["genero"] != "" and dados_musica["id"] != "":
            #self.__musicas.append(musica)
            self.__musica_DAO.add(musica)
        else:
            self.__tela_cadastro.mostra_mensagem("PREENCHA TODOS OS CAMPOS \n") 

    def editar_musica(self):
        dados_musica = []
        self.ver_musica()
        id_musica = self.__tela_cadastro.seleciona_musica()
        musica = self.pega_musica_por_id(id_musica)
        if(musica is not None):
            novos_dados_musica = self.__tela_cadastro.pega_dados_musica()
            musica.nome = novos_dados_musica["nome"]
            musica.artista = novos_dados_musica["artista"]
            musica.genero = novos_dados_musica["genero"]
            musica.id = novos_dados_musica["id"]
            self.ver_musica()
            self.__musica_DAO.update(musica)
            self.__tela_cadastro.mostra_mensagem("MÚSICA EDITADA COM SUCESSO! \n")
        else:
            self.__tela_cadastro.mostra_mensagem("ATENCAO: MÚSICA NÃO EXISTE \n")

    def excluir_musica(self):
        dados_musica = []
        self.ver_musica()
        id_musica = self.__tela_cadastro.seleciona_musica()
        musica = self.pega_musica_por_id(id_musica)
        if(musica is not None):
            self.__musica_DAO.remove(musica)
            self.ver_musica()
        else:
            self.__tela_cadastro.mostra_mensagem("ATENCAO: música não existente")

        self.__tela_cadastro.mostra_musica(dados_musica)
        
        #for index, indice in enumerate(self.__musicas):
        #    if indice.nome == nome_musica:
        #        #self.__musicas.pop(index)
        #        self.__tela_cadastro.mostra_mensagem("MÚSICA EXCLUÍDA! \n") 
        #        self.__tela_cadastro.quebra_linha()
        #if indice.nome != nome_musica:
        #    self.__tela_cadastro.mostra_mensagem("A MÚSICA QUE VOCÊ TENTOU EXCLUIR NÃO EXISTE \n")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.ver_musica, 2: self.incluir_musica, 3: self.editar_musica, 4: self.excluir_musica, 
                        0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_cadastro.tela_opcoes()]()

    def retorna_musica_aleatoria(self):
        #musica_aleatoria = random.choice(self.__musicas)
        #musica_aleatoria = random.choiceself.__musica_DAO.get_all()
        #musica_aleatoria = self.__musica_DAO.get_all()
        #a_musica_aleatoria = random.choice(musica_aleatoria)
        musica_aleatoria = self.__musica_DAO.get()
        return musica_aleatoria

    def retorna_musicas(self):
        #musicas = self.__musicas
        musicas = self.__musica_DAO.get_all()
        print("PASSOU")
        return musicas

    def retorna_objetos_musica(self):
        return self.__musica_DAO.get_all()
        #return self.__musicas           