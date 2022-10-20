from view.tela_abstrata import TelaAbstrata

class TelaInicial(TelaAbstrata):
    def tela_opcoes(self):
        print("____PlayerDeMusica____")
        print("Escolha uma opção")
        print("1 - Música")
        print("2 - [EM BREVE]")
        print("3 - [EM BREVE]")
        print("0 - Sair")
        opcao = int(input("Escolha a opcao:"))
        return opcao