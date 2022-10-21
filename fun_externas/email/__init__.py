import email
import re
import smtplib
from email.message import EmailMessage
from PySimpleGUI import PySimpleGUI as sg

def valida_email(email):
    #composição de carcteres para validação de email
    analisa = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if (re.search(analisa,email)):
        return True
    
    else:
        return False

def envia_email(dado_email,dado_senha,email_envio,verificador_de_fonetica):
    
    #Puxa informações para envio de email
    EMAIL_ADDRESS = dado_email
    EMAIL_PASSWORD = dado_senha
    
    #faz a montagem do email para envio
    msg = EmailMessage()
    msg['subject'] = 'Nova senha'
    msg['From'] = dado_email
    msg['To'] = email_envio
    
    #valida se a senha a ser enviada é uma fonetica ou uma simples

    if verificador_de_fonetica == True:
        fonetica = str(open(r'C:\Users\Public\gerador de senha\fonetica.txt', 'r', encoding='utf-8').read())

        msg.set_content(f'{fonetica}')

    else:
        normal = str(open(r'C:\Users\Public\gerador de senha\senha.txt', 'r', encoding='utf-8').read())
        msg.set_content(f'{normal}')
    
    #exceção de erro
    try:
        #faz o envio de email
        with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
            smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
            smtp.send_message(msg)
            #informa user se email enviado
            return 'Senha Enviada!'
    
    #Unico erro detectado inicialmente
    except TimeoutError:
        return 'erro'
        
    #informa user se ouver erro inesperado
    except Exception as erro2:
        sg.popup_error(erro2, no_titlebar= True)
        return 'erro_geral'
    