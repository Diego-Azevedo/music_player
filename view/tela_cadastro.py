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
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- DADOS MÚSICA ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('Artista:', size=(15, 1)), sg.InputText('', key='artista')],
            [sg.Text('Gênero:', size=(15, 1)), sg.InputText('', key='genero')],
            [sg.Text('Id:', size=(15, 1)), sg.InputText('', key='id')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Player de Música').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        artista = values['artista']
        genero = values['genero']
        id = values['id']

        self.close()
        return {"nome": nome, "artista": artista, "genero": genero, "id": id}
 
    def mostra_musica(self, dados_musica):
        string_todas_musicas = ""
        for dado in dados_musica:
            string_todas_musicas = string_todas_musicas + "MÚSICA: " + str(dado["nome"]) + '\n'
            string_todas_musicas = string_todas_musicas + "ARTISTA: " + str(dado["artista"]) + '\n'
            string_todas_musicas = string_todas_musicas + "GÊNERO: " + str(dado["genero"]) + '\n'
            string_todas_musicas = string_todas_musicas + "ID: " + str(dado["id"]) + '\n\n'

        sg.Popup('-------- LISTA DE MÚSICAS ----------', string_todas_musicas)

    def seleciona_musica(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('-------- SELECIONAR MÚSICA ----------', font=("Helvica", 25))],
        [sg.Text('Digite o ID da música:', font=("Helvica", 15))],
        [sg.Text('ID:', size=(15, 1)), sg.InputText('', key='nome')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona musica').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        self.close()
        return nome


    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values

#__________________________________________________________________      
    '''def mostra_nome_musica(self, nome):
        print("MÚSICA:", nome["nome"])
        print()    

    def exclui_musica(self):
        id = input("ID DA MÚSICA QUE DESEJA EXCLUIR: ")
        return id

    def edita_musica(self):
        id = int(input("ID DA MÚSICA QUE DESEJA EDITAR: "))
        return id'''
