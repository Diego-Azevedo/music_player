import PySimpleGUI as sg

from view.tela_abstrata import TelaAbstrata

class TelaCadastro(TelaAbstrata):


    def tela_opcoes(self):
        self.init_components()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        # cobre os casos de voltar, não clicar em nada e fechar janela, ou clicar cancelar
        if values['0'] or button in (None,'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def close(self):
        self.__window.Close()

    def init_components(self):
        #sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Player de Música', font=("Helvica",25))],
            [sg.Text('Escolha sua opção', font=("Helvica",15))],
            [sg.Radio('Listar Música',"RD1", key='1')],
            [sg.Radio('Cadastras Música',"RD1", key='2')],
            [sg.Radio('Alterar Música',"RD1", key='3')],
            [sg.Radio('Excluir Música',"RD1", key='4')],
            [sg.Radio('Sair',"RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Player de Música').Layout(layout)       

    def pega_dados_musica(self):
        nome = input("Nome: ")
        artista = input("Artista: ")
        genero = input("Genero: ")
        tempo = input("Tempo: ")
        print()
        return {"nome": nome, "artista": artista, "genero": genero, "tempo": tempo}
 
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
        nome = input("NOME DA MÚSICA QUE DESEJA EXCLUIR: ")
        return nome

    def edita_musica(self):
        nome = input("NOME DA MÚSICA QUE DESEJA EDITAR: ")
        return nome
