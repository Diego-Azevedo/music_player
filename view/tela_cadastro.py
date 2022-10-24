class TelaCadastro():
    def tela_opcoes(self):
        print("____MÚSICA____")
        print("Escolha a opção:")
        print("1 - Listar Música")
        print("2 - Cadastrar Música")
        print("3 - Alterar Música")
        print("4 - Excluir Música")
        print("0 - Retornar")
        opcao = int(input("Escolha a opcao:"))
        print()
        return opcao

    def pega_dados_musica(self):
        print("-------- CADASTRO DE MÚSICA --------")
        nome = input("Nome: ")
        artista = input("Artista: ")
        genero = input("Genero: ")
        tempo = input("Tempo: ")
        print()

        return {"nome": nome, "artista": artista, "genero": genero, "tempo": tempo}

    # lembrar de fazer o tratamento de excessoes 
    def mostra_musica(self, dados_musica):
        print("MÚSICA: ", dados_musica["nome"])
        print("ARTISTA: ", dados_musica["artista"])
        print("GENERO MUSICAL: ", dados_musica["genero"]) 
        print("TEMPO: ", dados_musica["tempo"])
        print()

    def mostra_nome_musica(self, nome):
        print("MÚSICA:", nome["nome"])
        print()    

    def mostra_mensagem(self, msg):
        print(msg)

    def exclui_musica(self):
        nome = input("Nome da música que deseja excluir: ")
        return nome

    def quebra_linha(self):
        print()    