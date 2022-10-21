 #Bibliotecas extras

import email
from PySimpleGUI import PySimpleGUI as sg

import re

#funções extras

import dados_email

#Definição das fontes para a interface grafica

fontP = ('Consolas', 15)
fontP2 = ('Consolas', 12)
fontgit = ('consolas', 8)

#Define o layout para a tela principal

#Cada espaço entre [] defini uma linha do layout da interface grafica


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

janela_email = tela_email()


while True:
    Windows, eventos, valores = sg.read_all_windows()

    if Windows == janela_email and eventos == 'Sair':
        break

    elif Windows == janela_email and eventos == 'Voltar':
        pass
        #criação no loop principal fora do de test

    elif Windows == janela_email and eventos == 'Enviar':
        Windows['-aviso_geral-'].update('')
        Windows['-aviso_geral_2-'].update('')

        analisa = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

        Email = valores['-email_user-']

        varificador_de_fonetica = str(open(r'.\Gerador_de_senha\Senha\fonetica.txt', 'r', encoding='utf-8').read())

        if (re.search(analisa,Email)):
            Windows['-aviso_geral-'].update('Email Valido')
            Windows.refresh()

            EMAIL_ADDRESS = dados_email.email
            EMAIL_PASSWORD = dados_email.senha
            senha_user = str(open(r'.\Gerador_de_senha\Senha\senha.txt', 'r', encoding='utf-8').read())
        
            msg = EmailMessage()
            msg['subject'] = 'Nova senha'
            msg['From'] = dados_email.email
            msg['To'] = Email
            
            if varificador_de_fonetica != '':
                msg.set_content(f'Sua nova senha é: {senha_user}\nPara melhor memorização grave as seguintes palavras: {varificador_de_fonetica}')
                
            else:
                msg.set_content(f'Sua nova senha é: {senha_user}')

            try:
                with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
                    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
                    smtp.send_message(msg)
                    Windows['-enviado-'] .update('Senha Enviada!')
            
            except TimeoutError as erro1:
                Windows['-aviso_geral-'].update('')
                Windows['-aviso_geral_2-'].update('Verifiqeu sua conecção')
                
            except Exception as erro2:
                sg.popup_error(erro2, no_titlebar= True)

        else:
            Windows['-aviso_geral_2-'].update('Email invalido')