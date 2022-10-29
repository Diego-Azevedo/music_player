from view.tela_player import TelaPlayer

class ControladorPlayer:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__musicas_tocadas = []
        self.__tela_player = TelaPlayer()

    def abre_tela(self):
        while True:
            lista_opcoes = {1: self.escolher_musica, 2: self.tocar_musica_aleatoria, 
                            3: self.tocar_playlist, 0: self.retornar}
            lista_opcoes[self.__tela_player.tela_opcoes()]()

    def escolher_musica(self):
        lista_musicas = self.__controlador_sistema.controlador_cadastro.retorna_musicas()
        self.__tela_player.mostra_mensagem("--------ESCOLHER MÚSICA--------")
        for index, item in enumerate(lista_musicas):
            self.__tela_player.dados_musica(index, item)
        opcao_escolhida = self.__tela_player.escolhe_opcao()       
        self.__tela_player.quebra_linha()
        self.__tela_player.mostra_mensagem("--------TOCANDO--------")
        self.__tela_player.mostra_musica(lista_musicas[opcao_escolhida])
        self.__musicas_tocadas.append(lista_musicas[opcao_escolhida])
        self.abre_tela_player()            

    def tocar_musica_aleatoria(self):
        musica_aleatoria = self.__controlador_sistema.controlador_cadastro.retorna_musica_aleatoria()
        self.__tela_player.mostra_mensagem("--------TOCANDO--------")
        self.__tela_player.mostra_musica(musica_aleatoria)
        self.__musicas_tocadas.append(musica_aleatoria)
        self.abre_tela_player()

    def tocar_playlist(self):
        play_list = self.__controlador_sistema.controlador_registro.retorna_playlist()
        self.__tela_player.mostra_mensagem("--------ESCOLHER PLAYLIST--------")
        if len(play_list) == 0:
            self.__tela_player.mostra_mensagem("Crie uma Playlist Primeiro!")
            self.__tela_player.quebra_linha()
        else:    
            for index, nome in enumerate(play_list):
                self.__tela_player.dados_playlist(index, nome.nome)
            opcao = self.__tela_player.escolhe_opcao()
            self.__tela_player.quebra_linha()
            self.__tela_player.mostra_mensagem("--------TOCANDO PLAYLIST--------")
            self.__tela_player.quebra_linha()
               
    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela_player(self):
        while True:
            lista_opcoes2 = {1: self.pausar_musica, 2: self.passar_musica,
                             3: self.voltar_musica, 0:self.abre_tela}
            lista_opcoes2[self.__tela_player.player_opcoes()]()                         

    def passar_musica(self):
        lista_musicas = self.__controlador_sistema.controlador_cadastro.retorna_musicas()
        musica_atual = self.__musicas_tocadas[-1]
        for index, indice in enumerate(lista_musicas):
            if indice['nome'] == musica_atual['nome']:
                n = index
        if n == (len(lista_musicas) - 1):
            n = 0
        self.__tela_player.mostra_mensagem("--------TOCANDO--------")        
        self.__tela_player.mostra_musica(lista_musicas[n+1])
        self.__musicas_tocadas.append(lista_musicas[n+1])        

    def pausar_musica(self):
        musica_atual = self.__musicas_tocadas[-1]
        self.__tela_player.pausar_musica()
        self.__tela_player.mostra_mensagem("--------TOCANDO--------")
        self.__tela_player.mostra_musica(musica_atual)

    def voltar_musica(self):
        lista_musicas = self.__controlador_sistema.controlador_cadastro.retorna_musicas()
        musica_atual = self.__musicas_tocadas[-1]
        for index, indice in enumerate(lista_musicas):
            if indice['nome'] == musica_atual['nome']:
                n = index
        if n == 0:
            n = len(lista_musicas)
        self.__tela_player.mostra_mensagem("--------TOCANDO--------")        
        self.__tela_player.mostra_musica(lista_musicas[n-1])
        self.__musicas_tocadas.append(lista_musicas[n-1])

    def retorna_musicas(self):
        lista_musicas = []
        for musica in self.__musicas_tocadas:
            lista_musicas.append(musica)
        return lista_musicas

    def limpa_historico(self):
        self.__musicas_tocadas.clear()                                 