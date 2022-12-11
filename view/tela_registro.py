from view.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg

class TelaRegistro(TelaAbstrata):
    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.open()
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        if values['0'] or button in (None,'Cancelar'):
            opcao = 0
        self.close()
        return opcao


    def init_opcoes(self):
        #sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Player de Música', font=("Helvica",25))],
            [sg.Text('Escolha sua opção', font=("Helvica",15))],
            [sg.Radio('Criar Playlist',"RD1", key='1')],
            [sg.Radio('Excluir Playlist',"RD1", key='2')],
            [sg.Radio('Histórico do Player',"RD1", key='3')],
            [sg.Radio('Limpar Histórico',"RD1", key='4')],
            [sg.Radio('Sair',"RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Player de Música').Layout(layout)

    def seleciona_musica(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('-------- SELECIONAR PLAYLIST ----------', font=("Helvica", 25))],
        [sg.Text('Digite o nome da playlist:', font=("Helvica", 15))],
        [sg.Text('NOME:', size=(15, 1)), sg.InputText('', key='nome')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona musica').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        self.close()
        return nome

    def seleciona_musica(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('-------- SELECIONAR MÚSICA ----------', font=("Helvica", 25))],
        [sg.Text('Digite o nome da mùsica:', font=("Helvica", 15))],
        [sg.Text('NOME:', size=(15, 1)), sg.InputText('', key='nome')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona musica').Layout(layout)

        button, values = self.open()
        posicao = values['nome']
        self.close()
        return posicao              

    def mostra_musica(self, index, dados_musica):
        [sg.Text(index, "-", "MÚSICA:", dados_musica["nome"], "-", "ARTISTA:", dados_musica["artista"])]

    def mostra_playlist(self, index, nome):
        [sg.Text(index, '-'), nome]    

    def mostra_musica_adicionada(self, msg, musica, mensagem, playlist):
        [sg.Text(msg, musica, mensagem, playlist)]

    def mostra_registro(self, ouvidas, curtidas):
        [sg.Text('Você escutou um total de', ouvidas, 'músicas, e favoritou', curtidas, 'músicas.', font=("Helvica",25))],

    def continuar(self):
        [sg.Text('Escolha sua opção', font=("Helvica",15))],
        [sg.Radio('Continuar',"RD1", key='1')],
        [sg.Radio('Salvar e Sair',"RD1", key='2')],
        print("1 - Continuar")
        print("0 - Salvar e Sair")
        retorno = input("Escolha a Opção: ")
        return retorno

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values