from view.tela_abstrata import TelaAbstrata

class TelaRegistro(TelaAbstrata):
    def tela_opcoes(self):
        print("____REGISTRO____")
        print("1 - Histórico do Player")
        print("2 - Limpar Histórico")
        print("0 - Voltar")
        opcao = int(input("Escolha a Opção: "))
        print()
        return opcao 