from view.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg

class TelaRegistro(TelaAbstrata):

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
            [sg.Radio('Criar Playlist',"RD1", key='1')],
            [sg.Radio('Excluir Playlist',"RD1", key='2')],
            [sg.Radio('Historico do Player',"RD1", key='3')],
            [sg.Radio('Limpar Histórico',"RD1", key='4')],
            [sg.Radio('Sair',"RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Player de Música').Layout(layout)   

    def nome_playlist(self):
        nome = input("Nome da Playlist: ")
        return nome

    def escolher_musica(self):
        posicao = int(input("Escolha uma música: "))
        return posicao

    def escolher_musica(self):
        posicao = int(input("Escolha uma playlist: "))
        return posicao              

    def mostra_musica(self, index, dados_musica):
        print(index, "-", "MÚSICA:", dados_musica["nome"], "-", "ARTISTA:", dados_musica["artista"])

    def mostra_playlist(self, index, nome):
        print(index, "-", nome)    

    def mostra_musica_adicionada(self, msg, musica, mensagem, playlist):
        print(msg, musica, mensagem, playlist)

    def mostra_registro(self, ouvidas, curtidas):
        print("Você escutou um total de", ouvidas, "músicas, e favoritou", curtidas, "músicas.")
        print()        

    def continuar(self):
        print("1 - Continuar")
        print("0 - Salvar e Sair")
        retorno = input("Escolha a Opção: ")
        return retorno
