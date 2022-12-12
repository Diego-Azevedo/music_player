from entidade.musica import Musica
from view.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg

class TelaPlayer(TelaAbstrata):

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
        if values['0'] or button in (None,'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def close(self):
        self.__window.Close()

    def init_components(self):
        #sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkAmber')
        layout = [
            [sg.Text('Player de Música', font=("Helvica",25))],
            [sg.Text('Escolha sua opção', font=("Helvica",15))],
            [sg.Radio('Escolher Música',"RD1", key='1')],
            [sg.Radio('Tocar Música Aleatória',"RD1", key='2')],
            [sg.Radio('Tocar Playlist',"RD1", key='3')],
            [sg.Radio('Sair',"RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Player de Música').Layout(layout)  

    def tela_opcoes_player(self):
        self.init_components_player()            
        button, values = self.__window.Read()
        opcao2 = 0
        if values['1']:
            opcao2 = 1
        if values['2']:
            opcao2 = 2
        if values['3']:
            opcao2 = 3
        if values['4']:
            opcao2 = 4
        if values['5']:
            opcao2 = 5
        if values['0'] or button in (None,'Cancelar'):
            opcao2 = 0
        self.close()
        return opcao2

    def init_components_player(self):
        sg.ChangeLookAndFeel('DarkAmber')
        layout = [
            [sg.Text('Player de Música', font=("Helvica",25))],
            [sg.Text('Escolha sua opção', font=("Helvica",15))],
            [sg.Radio('Pausar',"RD1", key='1')],
            [sg.Radio('Passar Música',"RD1", key='2')],
            [sg.Radio('Voltar Música',"RD1", key='3')],
            [sg.Radio('Curtir Música',"RD1", key='4')],
            [sg.Radio('Descurtir Música',"RD1", key='5')],
            [sg.Radio('Sair',"RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Player de Música').Layout(layout)         

    def mostra_musica(self, nome, artista):
        print("MÚSICA:", nome, "-", artista)
        print()    

    def escolhe_opcao(self):
        opcao = int(input("Escolha a Opção: "))
        return opcao

    def pausar_musica(self):
        print("--------MÚSICA PAUSADA--------")
        input("CLIQUE PARA CONTINUAR: ")
        print()

    def dados_playlist(self, index, nome):
        print(index, "-", nome)
