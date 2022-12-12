from entidade.musica import Musica
from view.tela_player import TelaPlayer
from Dao.dao_registro import RegistroDAO
import os

class ControladorPlayer:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__registro_DAO = RegistroDAO()
        self.__musicas_tocadas = []
        self.__tela_player = TelaPlayer()
        self.__playlist_atual = None

    def abre_tela(self):
        while True:
            lista_opcoes = {1: self.escolher_musica, 2: self.tocar_musica_aleatoria, 
                            3: self.tocar_playlist, 0: self.retornar}
            lista_opcoes[self.__tela_player.tela_opcoes()]()

    def escolher_musica(self):
        lista_musicas = list(self.__controlador_sistema.controlador_cadastro.retorna_musicas())
        self.__tela_player.mostra_mensagem("--------ESCOLHER MÚSICA--------")
        for index, item in enumerate(lista_musicas):
            self.__tela_player.dados_musica(index, item.nome, item.artista)
        opcao_escolhida = self.__tela_player.escolhe_opcao()     
        try:
            if opcao_escolhida <= index:
                
                self.__tela_player.quebra_linha()
                self.__tela_player.mostra_mensagem("--------TOCANDO--------")
                self.__tela_player.mostra_musica(lista_musicas[opcao_escolhida].nome, lista_musicas[opcao_escolhida].artista)
                self.__musicas_tocadas.append(lista_musicas[opcao_escolhida])
                self.__registro_DAO.add(lista_musicas[opcao_escolhida])
                self.abre_tela_player()            
            else:

                raise KeyError
        except KeyError:
            self.__tela_player.mostra_mensagem("ESCOLHA UMA MÚSICA VÁLIDA \n")

    def tocar_musica_aleatoria(self):
        musica_aleatoria = self.__controlador_sistema.controlador_cadastro.retorna_musica_aleatoria()
        self.__tela_player.mostra_mensagem("--------TOCANDO--------")
        self.__tela_player.mostra_musica(musica_aleatoria.nome, musica_aleatoria.artista)  
        self.__musicas_tocadas.append(musica_aleatoria)
        self.__registro_DAO.add(musica_aleatoria)
        self.abre_tela_player()

    def tocar_playlist(self):
        play_list = self.__controlador_sistema.controlador_registro.retorna_playlist()
        self.__tela_player.mostra_mensagem("--------ESCOLHER PLAYLIST--------")
        if len(play_list) == 0:
            self.__tela_player.mostra_mensagem("CRIE UMA PLAYLIST PRIMEIRO! \n")
            self.__tela_player.quebra_linha()
        else:    
            for index, nome in enumerate(play_list):
                self.__tela_player.dados_playlist(index, nome.nome)
            opcao = self.__tela_player.escolhe_opcao()
            playlist_escolhida = play_list[opcao]
            self.__playlist_atual = playlist_escolhida
            self.__tela_player.quebra_linha()
            self.__tela_player.mostra_mensagem("--------TOCANDO PLAYLIST--------")
            self.__tela_player.mostra_musica(playlist_escolhida.lista_musicas[0].nome, playlist_escolhida.lista_musicas[0].artista)
            self.__musicas_tocadas.append(playlist_escolhida.lista_musicas[0])
            self.__registro_DAO.add(playlist_escolhida.lista_musicas[0])
            self.abre_tela_playlist()

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela_player(self):
        while True:
            lista_opcoes2 = {1: self.pausar_musica, 2: self.passar_musica,
                             3: self.voltar_musica, 4: self.curtir_musica,
                             5: self.descurtir_musica, 0:self.abre_tela}
            lista_opcoes2[self.__tela_player.player_opcoes()]()

    def abre_tela_playlist(self):
        while True:
            lista_opcoes3 = {1: self.pausar_musica, 2: self.passar_musica_playlist,
                             3: self.voltar_musica_playlist, 4: self.curtir_musica,
                             5: self.descurtir_musica, 0:self.abre_tela}
            lista_opcoes3[self.__tela_player.player_opcoes()]()                                 

    def passar_musica(self):
        lista_musicas = list(self.__controlador_sistema.controlador_cadastro.retorna_musicas())
        musica_atual = self.__musicas_tocadas[-1]
        for index, musica in enumerate(lista_musicas):
            if musica.nome == musica_atual.nome:
                n = index
        if n == (len(lista_musicas) - 1):
            n = 0
        self.__tela_player.mostra_mensagem("--------TOCANDO--------")        
        self.__tela_player.mostra_musica(lista_musicas[n+1].nome, lista_musicas[n+1].artista)
        self.__musicas_tocadas.append(lista_musicas[n+1])
        self.__registro_DAO.add(lista_musicas[n+1])

    def passar_musica_playlist(self):
        playlist_atual = self.__playlist_atual
        musica_atual = self.__musicas_tocadas[-1]
        for index, musica in enumerate(playlist_atual.lista_musicas):
            if musica.nome == musica_atual.nome:
                n = index
        if n == (len(playlist_atual.lista_musicas) - 1):
            n = 0
        self.__tela_player.mostra_mensagem("--------TOCANDO PLAYLIST--------")                   
        self.__tela_player.mostra_musica(playlist_atual.lista_musicas[n+1].nome, playlist_atual.lista_musicas[n+1].artista)
        self.__musicas_tocadas.append(playlist_atual.lista_musicas[n+1])
        self.__registro_DAO.add(playlist_atual.lista_musicas[n+1])                    

    def voltar_musica(self):
        lista_musicas = list(self.__controlador_sistema.controlador_cadastro.retorna_musicas())
        musica_atual = self.__musicas_tocadas[-1]
        for index, musica in enumerate(lista_musicas):
            if musica.nome == musica_atual.nome:
                n = index
        if n == 0:
            n = len(lista_musicas)
        self.__tela_player.mostra_mensagem("--------TOCANDO--------")        
        self.__tela_player.mostra_musica(lista_musicas[n-1].nome, lista_musicas[n-1].artista)
        self.__musicas_tocadas.append(lista_musicas[n-1])
        self.__registro_DAO.add(lista_musicas[n-1]) 

    def voltar_musica_playlist(self):
        playlist_atual = self.__playlist_atual
        musica_atual = self.__musicas_tocadas[-1]
        for index, musica in enumerate(playlist_atual.lista_musicas):
            if musica.nome == musica_atual.nome:
                n = index        
        if n == 0:
            n = len(playlist_atual.lista_musicas)
        self.__tela_player.mostra_mensagem("--------TOCANDO PLAYLIST--------")                   
        self.__tela_player.mostra_musica(playlist_atual.lista_musicas[n-1].nome, playlist_atual.lista_musicas[n-1].artista)
        self.__musicas_tocadas.append(playlist_atual.lista_musicas[n-1])
        self.__registro_DAO.add(playlist_atual.lista_musicas[n-1])                                

    def pausar_musica(self):
        musica_atual = self.__musicas_tocadas[-1]
        self.__tela_player.pausar_musica()
        self.__tela_player.mostra_mensagem("--------TOCANDO--------")
        self.__tela_player.mostra_musica(musica_atual.nome, musica_atual.artista) 

    def curtir_musica(self):
        self.__musicas_tocadas[-1].gostei = True

    def descurtir_musica(self):
        self.__musicas_tocadas[-1].gostei = False           

    def retorna_musicas(self):
        lista_registro = self.__registro_DAO.get_all()
        return lista_registro   
        #lista_musicas = self.__musicas_tocadas
        #return lista_musicas
        
    def excluir_registro(self):
        for registro in self.__registro_DAO.get_all():
            del registro

    def limpa_historico(self):
        self.__musicas_tocadas.clear()
        self.excluir_registro()
        os.remove("registro.pkl")
        #self.__registro_DAO.clear()
                           