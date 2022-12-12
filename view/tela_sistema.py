import PySimpleGUI as sg

from view.tela_abstrata import TelaAbstrata

class TelaInicial(TelaAbstrata):
    def __init__(self):
        self.__window = None

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
        if values['0'] or button in (None,'Sair'):
            opcao = 0
        self.close()
        return opcao

    def close(self):
        self.__window.Close()

    def init_components(self):
        sg.ChangeLookAndFeel('DarkAmber')
        layout = [
            [sg.Text('Player de Música', font=("Helvica",25))],
            [sg.Text('Escolha sua opção', font=("Helvica",15))],
            [sg.Radio('Música',"RD1", key='1')],
            [sg.Radio('Player',"RD1", key='2')],
            [sg.Radio('Registro',"RD1", key='3')],
            [sg.Radio('Sair',"RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Player de Música').Layout(layout)
