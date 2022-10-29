from view.tela_abstrata import TelaAbstrata

class TelaRegistro(TelaAbstrata):
    def tela_opcoes(self):
        print("____REGISTRO____")
        print("1 - Histórico do Player")
        print("2 - Limpar Histórico")
        print("3 - Criar Playlist")
        print("0 - Voltar")
        opcao = int(input("Escolha a Opção: "))
        print()
        return opcao

    def nome_playlist(self):
        nome = input("Nome da Playlist: ")
        return nome

    def escolher_musica(self):
        posicao = int(input("Escolha uma música: "))
        return posicao     

    def mostra_musica(self, index, dados_musica):
        print(index, "-", "MÚSICA:", dados_musica["nome"], "-", "ARTISTA:", dados_musica["artista"])

    def mostra_musica_adicionada(self, msg, musica, mensagem, playlist):
        print(msg, musica, mensagem, playlist)    

    def continuar(self):
        print("1 - Continuar")
        print("0 - Salvar e Sair")
        retorno = input("Escolha a Opção: ")
        return retorno    
  