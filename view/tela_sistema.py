from view.tela_abstrata import TelaAbstrata

class TelaInicial(TelaAbstrata):
    def tela_opcoes(self):
        print("____PlayerDeMusica____")
        print("Escolha uma opção")
        print("1 - Artista")
        print("2 - Genero")
        print("3 - Musica")
        print("0 - Sair")
        opcao = int(input("Escolha a opcao:"))
        return opcao