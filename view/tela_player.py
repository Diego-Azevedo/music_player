from view.tela_abstrata import TelaAbstrata

class TelaPlayer(TelaAbstrata):
    def tela_opcoes(self):
        print("____PLAYER____")
        print("1 - Escolher Música")
        print("2 - Tocar Música Aleatória")
        print("0 - Voltar")
        opcao = int(input("Escolha a Opção: "))
        print()
        return opcao

    def mostra_musica(self, nome):
        print("--------TOCANDO--------")
        print("MÚSICA:", nome["nome"], "-", nome["artista"])
        print()

    def escolhe_musica(self, index, dados_musica):
        print(index, "-", dados_musica["nome"], "-", dados_musica["artista"])

    def escolhe_opcao(self):
        opcao = int(input("Escolha a Opção: "))
        return opcao

    def print_escolher_musica(self):
        print("--------ESCOLHER MÚSICA--------")        

    def quebra_linha(self):
        print()
           
        
    
    