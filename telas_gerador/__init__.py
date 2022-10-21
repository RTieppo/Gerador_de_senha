#Bibliotecas extras

from PySimpleGUI import PySimpleGUI as sg

#Definição das fontes para a interface grafica

fontP = ('Consolas', 15)
fontP2 = ('Consolas', 12)
fontgit = ('consolas', 8)

#Define o layout para a tela principal

#Cada espaço entre [] defini uma linha do layout da interface grafica

def tela_gerador():

    sg.theme('DarkAmber')
    

    layout = [
        [sg.Column([[sg.Image(r'.\IMG\Cadeado.png')]],justification= 'l'),
        sg.Column([[sg.Output(size = (80,8), key='-senha-', font=fontP2,)]])],

        [sg.Text('Escolha o nivel da senha', font=fontP)],

        [sg.Radio('Básica','Radio1', key= '-fraca-', font=fontP2),
        sg.Radio('Media','Radio1', key='-media-', font=fontP2), sg.Radio('Forte','Radio1', key='-forte-', font=fontP2)],

        [sg.Text('=='*35)],

        [sg.Text('Personalização', font=fontP)],

        [sg.Checkbox('Minúsculas', key='-minusculas-', pad=(0,0), font=fontP2), sg.Checkbox('Números ', key='-numeros-', pad=(0,0), font=fontP2)],

        [sg.Checkbox('Maiúsculas', key='-maiusculas-', pad=(0,0), font=fontP2),sg.Checkbox('Palavras', key='-palavras-', pad=(0,0), font=fontP2),
        sg.Checkbox('Especiais ', key='-especiais-',pad=(0,0), font=fontP2)],

        [sg.Text('=='*35)], 

        [sg.Text('Fácil memorização', font=fontP)],

        [sg.Button('Fonética', font=fontP2)],
        
        [sg.Text('=='*35)],

        [sg.Text('', key= '-Aviso-', font=fontP, text_color='red')],

        [sg.Button('Gerar', size=(5,0), font=fontP2),sg.Button('Resetar',size=(10,0), font=fontP2),
        sg.Button('Sair', size=(5,0), font=fontP2)],

        [sg.Text('', key='-Novo_botão-'), sg.Text('', key='-botão_email-')],

        [sg.Text('Github: RTieppo', font=fontgit)],


    ]
    return sg.Window('Gerador de senha', size=(500,610), finalize= True, layout=layout, margins=(0,0), element_justification='c', icon=(r'.\IMG\Cadeado.ico'))

def tela_email():

    sg.theme('DarkAmber')

    layout = [

        [sg.Text('\nDigite o seu e-mail:', font=fontP2)],

        [sg.Input(key='-email_user-')],

        [sg.Text('', key='-aviso_geral-', font=fontP2, text_color='green'), sg.Text('', key='-aviso_geral_2-', font=fontP2, text_color='red')],

        [sg.Text('',key='-enviado-', font=fontP2, text_color='green')],

        [sg.Button('Enviar', font=fontP2)],

        [sg.Button('Sair', font=fontP2), sg.Button('Voltar', font=fontP2)]
    ]
    return sg.Window('Gerador de senaha', size=(400,220), finalize= True, layout=layout, margins=(0,0), no_titlebar= True, element_justification='c')   