class TelaArtista:
    def tela_opcoes(self):
        print("____Artista____")
        print("Escolha uma opcao")
        print("1 - Ver artistas")
        print("2 - Incluir artista")
        print("3 - Editar artista")
        print("4 - Excluir artista")
        print("0 - Retornar")
        opcao = int(input("Escolha a opcao:"))
        return opcao

    # lembrar de fazer o tratamento de excessoes 
    def mostra_artista(self, dados_artista):
        print("NOME DO ARTISTA: ", dados_artista["nome"])
        print("GENERO MUSICAL: ", dados_artista["genero"])
        print("ALBUNS: ") #caso seja implementado albuns
        print("\n")

    def pega_dados_artista(self):
        print("-------- CADASTRO DE ARTISTA ----------")
        nome = input("Nome: ")
        genero = input("Genero musical: ")

        return {"nome": nome, "genero": genero}

    def mostra_mensagem(self, msg):
        print(msg)
