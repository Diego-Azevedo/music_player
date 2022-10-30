from view.tela_abstrata import TelaAbstrata

class TelaInicial(TelaAbstrata):
    
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
        print("____PlayerDeMusica____")
        print("Escolha uma opção")
        print("1 - Música")
        print("2 - Player")
        print("3 - Registro")
        print("0 - Sair")
        opcao = self.ler_opcao("Escolha a opcao: ", [0, 1, 2, 3])
        print()
        return opcao