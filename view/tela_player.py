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
        # cobre os casos de voltar, não clicar em nada e fechar janela, ou clicar cancelar
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

    def player_opcoes(self):
        print("____PLAYER OPCÕES____")
        print("1 - Pausar")
        print("2 - Passar Música")
        print("3 - Voltar Música")
        print("4 - Curtir Música")
        print("5 - Descurtir Música")
        print("0 - Sair")
        opcao2 = self.ler_opcao("Escolha a opcao: ", [0, 1, 2, 3, 4, 5])
        print()
        return opcao2           

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
