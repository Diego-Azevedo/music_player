from view.tela_abstrata import TelaAbstrata

class TelaRegistro(TelaAbstrata):
    def tela_opcoes(self):
        print("____REGISTRO____")
        print("1 - Ultimas Tocadas")
        print("2 - Limpar lista")
        print("0 - Voltar")
        opcao = int(input("Escolha a Opção: "))
        print()
        return opcao