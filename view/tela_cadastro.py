from view.tela_abstrata import TelaAbstrata

class TelaCadastro(TelaAbstrata):

    def ler_opcao(self, mensagem: str = "", inteiros_validos: [] = None):
        while True:
            valor_lido = input(mensagem)
            try:
                inteiro = int(valor_lido)
                if inteiros_validos and inteiro not in inteiros_validos:
                    raise ValueError
                return inteiro
            except ValueError: 
                print("Selecione uma opcao valida")

    def tela_opcoes(self):
        print("____MÚSICA____")
        print("Escolha a opção:")
        print("1 - Listar Música")
        print("2 - Cadastrar Música")
        print("3 - Alterar Música")
        print("4 - Excluir Música")
        print("0 - Retornar")
        opcao = self.ler_opcao("Escolha a opcao: ", [0, 1, 2, 3, 4])
        print()
        return opcao

    def pega_dados_musica(self):
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

    def exclui_musica(self):
        nome = input("Nome da música que deseja excluir: ")
        return nome

    def edita_musica(self):
        nome = input("Nome da música que deseja editar: ")
        return nome

    