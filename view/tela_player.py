from view.tela_abstrata import TelaAbstrata

class TelaPlayer(TelaAbstrata):
    def tela_opcoes(self):
        print("____PLAYER____")
        print("1 - Escolher Música")
        print("2 - Tocar Música Aleatória")
        print("3 - Tocar Playlist")
        print("0 - Voltar")
        opcao = int(input("Escolha a Opção: "))
        print()
        return opcao

    def player_opcoes(self):
        print("____PLAYER OPCÕES____")
        print("1 - Pausar")
        print("2 - Passar Música")
        print("3 - Voltar Música")
        print("0 - Sair")
        opcao2 = int(input("Escolha a Opção: "))
        print()
        return opcao2           

    def mostra_musica(self, nome):
        print("MÚSICA:", nome["nome"], "-", nome["artista"])
        print()

    def escolhe_opcao(self):
        opcao = int(input("Escolha a Opção: "))
        return opcao

    def pausar_musica(self):
        print("--------MÚSICA PAUSADA--------")
        input("Clique para continuar: ")
        print()

    def dados_playlist(self, index, nome):
        print(index, "-", nome)     

           
        
    
    