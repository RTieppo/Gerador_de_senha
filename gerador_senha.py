#Bibliotecas extras
from time import sleep
from PySimpleGUI import PySimpleGUI as sg
from random import choice, randint

# funções externas
from dados_email import dado_email,dado_senha
from fun_externas import gera_dados
from fun_externas import imprime_info
from fun_externas import manipula_txt
from fun_externas import email
import telas_gerador

#Faz a abertura da janela principal do Gerador de senha e define atribuição das demais janelas
manipula_txt.cria_ark_ini()
janela_gerador = telas_gerador.tela_gerador()
janela_email = None

#Definição das fontes para a interface grafica
fontP = ('Consolas', 15)
fontP2 = ('Consolas', 12)
fontgit = ('consolas', 8)

#Abre os arquivos usados para gerar as senha e faz a leitura dos arquivos linha a linha 
arquivo_caracteres = open(r'.\Txt_aqr\Caracter.txt','r', encoding='utf-8').readlines()
arquivo_2_3_letras = open(r'.\Txt_aqr\letras_2_3.txt','r', encoding='utf-8').readlines()
arquivo_4_5_letras = open(r'.\Txt_aqr\letras_4_5.txt', 'r', encoding='utf-8').readlines()
arquivos_6_7_letras = open(r'.\Txt_aqr\letras_6_7.txt', 'r', encoding='utf-8').readlines()
arquivo_fonetica = open(r'.\Txt_aqr\Alfabeto_fonetico.txt', 'r', encoding='utf-8').readlines()

#Limita a criação do botão de salvameno ou qualquer outro botão
limita_criação_botão = 0

#Armazena caracteres gerados aleatorios quando senha gerada
senha = list()

#validação fonetica
verificador_de_fonetica = False

#contador Global
contador = 0

while True:
    Windows, eventos, valores = sg.read_all_windows()

    if Windows == janela_gerador and eventos == sg.WIN_CLOSED or Windows == janela_gerador and eventos == 'Sair':
        print(f'{"Finalizando aplicação..."}'.center(40))
        janela_gerador.refresh()
        sleep(1)
        print(f'{"Obrigado, por usar!"}'.center(40))
        janela_gerador.refresh()
        manipula_txt.limpa_arq()
        sleep(1)
        break
    
    elif Windows == janela_gerador and eventos == 'Resetar':
        janela_gerador.close()
        janela_gerador = telas_gerador.tela_gerador()
        limita_criação_botão = 0
    
    elif Windows == janela_gerador and eventos == 'Salvar':
        manipula_txt.salva_arquivo(varificador_de_fonetica)
        Windows['-Aviso-'].update('Salvo na área de trabalho')

    elif Windows == janela_gerador and eventos == 'Email':
        #abre tela de envio de email
        janela_email = telas_gerador.tela_email()
        #esconde tela principal 
        janela_gerador.hide()
        
    if Windows == janela_email and eventos == 'Sair':
        manipula_txt.limpa_arq()
        sleep(1)
        break

    elif Windows == janela_email and eventos == 'Voltar':
        #abre a tela principal de novo e fecha a de envio de email
        janela_gerador.un_hide()
        janela_email.close()

    elif Windows == janela_email and eventos == 'Enviar':
        #Limpa informações apresentadas para o usuario da tela
        Windows['-aviso_geral-'].update('')
        Windows['-aviso_geral_2-'].update('')
        Windows['-enviado-'].update('')
        email_envio = valores['-email_user-']
        analisa = email.valida_email(email_envio)

        if analisa == True:
            Windows['-aviso_geral-'].update(' Email Valido!')
            Windows.refresh()
            sleep(1)
            Windows['-enviado-'].update('Enviando Aguarde...')
            Windows.refresh()
            envia = email.envia_email(dado_email,dado_senha,email_envio,verificador_de_fonetica)
            Windows['-enviado-'] .update(envia)
            
            if envia == 'erro':
                Windows['-aviso_geral-'].update('')
                Windows['-enviado-'].update('')
                Windows['-aviso_geral_2-'].update('Verifique sua conexão!')
            
            elif envia == 'erro_geral':
                Windows['-aviso_geral-'].update('')
                Windows['-aviso_geral_2-'].update('')
                Windows['-enviado-'].update('')

        else:
            Windows['-aviso_geral_2-'].update('E-mail invalido!')

    elif Windows == janela_gerador and eventos == 'Fonética':
        #verifica se o botão ja foi criado/cria botão

        verificador_de_fonetica = True
        #reseta as informações da tela
        Windows['-Aviso-'].update('')

        #Valida se todos os valores variaveis são falsos para gerar a senha fonetica 
        if valores['-minusculas-'] == False and valores['-numeros-'] == False and valores['-maiusculas-'] == False and valores['-especiais-'] == False and valores['-palavras-'] == False:

                if valores['-fraca-'] == True or valores['-media-'] == True or valores['-forte-'] == True:
                    if limita_criação_botão == 0:
                        janela_gerador.extend_layout(janela_gerador['-Novo_botão-'],
                        [[sg.Button('Salvar', font=fontP2), sg.Button('Email', font=fontP2)]])
                        limita_criação_botão = 10

                if valores['-fraca-'] == True:

                    gera_dados.fonetica(8)
                    manipula_txt.cria_txt_fonetico()

                elif valores['-media-'] == True:
    
                    gera_dados.fonetica(12)
                    manipula_txt.cria_txt_fonetico()

                elif valores['-forte-'] == True:

                    gera_dados.fonetica(16)
                    manipula_txt.cria_txt_fonetico()

                #informa que faltou escolher o nivel da senh
                
                else:
                    Windows['-Aviso-'].update('Escolha um nível de senha')
            
            #informa caso o user tente gerar senha personalizada na opção fonetica
        else:
            Windows['-Aviso-'].update('Personalização não permitida!')

    elif Windows == janela_gerador and eventos == 'Gerar':
        senha.clear()
        contador = 0
        varificador_de_fonetica = False
        #reseta as informações da tela
        Windows['-Aviso-'] .update('')

        if valores['-fraca-'] == True or valores['-media-'] == True or valores['-forte-'] == True:
            #Define os valores variaveis para a verificação dos eventos verdadeiros no loop 'for' secundário
            valores_variaveis = ('-minusculas-', '-numeros-', '-maiusculas-', '-especiais-', '-palavras-')

            if limita_criação_botão == 0:
                janela_gerador.extend_layout(janela_gerador['-Novo_botão-'],
                [[sg.Button('Salvar', font=fontP2), sg.Button('Email', font=fontP2)]])
                limita_criação_botão = 10

            #verifica o nivel foi selecionado 
            if valores['-fraca-'] == True:
                print('Gerando senha de 8 carcteres...')

                #valida quais eventos variaveis foram selecionados para gerar senha personalizada
                for variaveis in valores_variaveis:
                    if valores[variaveis] == True:

                        while contador < 8:

                            if valores['-palavras-'] == True:

                                if contador < 6:
                                    palavra_aleatoria = choice(str(arquivo_2_3_letras[0]).split())
                                    senha.append(palavra_aleatoria)
                                    contador += len(palavra_aleatoria)
                                
                                elif contador == 6:
                                    palavra_aleatoria = choice(str(arquivo_2_3_letras[1]).split())
                                    senha.append(palavra_aleatoria)
                                    contador += len(palavra_aleatoria)

                            if valores['-minusculas-'] == True:
                                if contador < 8:
                                    senha.append(choice(str(arquivo_caracteres[2]).split()))
                                    contador += 1

                            if valores['-numeros-'] == True:
                                if contador < 8:
                                    senha.append(choice(str(arquivo_caracteres[0]).split()))
                                    contador += 1

                            if valores['-maiusculas-'] == True:
                                if contador < 8:
                                    senha.append(choice(str(arquivo_caracteres[1]).split()))
                                    contador += 1

                            if valores['-especiais-'] == True:
                                if contador < 8:
                                    senha.append(choice(str(arquivo_caracteres[3]).split()))
                                    contador += 1     
                
                #Caso não tenha personalização vai gerar senha aleatoria sem a opção de palavras   
                sem = gera_dados.sem_preferencia(8)
                imprime_info.imprime_senha(senha, sem)
                manipula_txt.cria_txt_normal(senha,sem)

            #verifica o nivel foi selecionado
            elif valores ['-media-'] == True:
                print('Gerando senha de 12 carcteres...')

                #valida quais eventos variaveis foram selecionados para gerar senha personalizada
                for variaveis in valores_variaveis:
                    if valores[variaveis] == True:

                        while contador < 12:

                            if valores['-palavras-'] == True:

                                if contador < 5:
                                    linha_aleatoria = int(randint(0,1))
                                    palavra_aleatoria = choice(str(arquivo_4_5_letras[linha_aleatoria]).split())
                                    senha.append(palavra_aleatoria)
                                    contador += len(palavra_aleatoria)

                                elif contador == 9:
                                    palavra_aleatoria = choice(str(arquivo_2_3_letras[0]).split())
                                    senha.append(palavra_aleatoria)
                                    contador += len(palavra_aleatoria)
                                
                                else:
                                    palavra_aleatoria = choice(str(arquivo_2_3_letras[1]).split())
                                    senha.append(palavra_aleatoria)
                                    contador += len(palavra_aleatoria)
                                
                            if valores['-minusculas-'] == True:
                                if contador < 12:
                                    senha.append(choice(str(arquivo_caracteres[2]).split()))
                                    contador += 1

                            if valores['-numeros-'] == True:
                                if contador < 12:
                                    senha.append(choice(str(arquivo_caracteres[0]).split()))
                                    contador += 1

                            if valores['-maiusculas-'] == True:
                                if contador < 12:
                                    senha.append(choice(str(arquivo_caracteres[1]).split()))
                                    contador += 1

                            if valores['-especiais-'] == True:
                                if contador < 12:
                                    senha.append(choice(str(arquivo_caracteres[3]).split()))
                                    contador += 1

                    #Caso não tenha personalização vai gerar senha aleatoria sem a opção de palavras            
            
                sem = gera_dados.sem_preferencia(12)
                imprime_info.imprime_senha(senha, sem)
                manipula_txt.cria_txt_normal(senha,sem)
                
            #verifica o nivel foi selecionado
            elif valores ['-forte-'] == True:
                print('Gerando senha de 16 carcteres...')
                
                #valida quais eventos variaveis foram selecionados para gerar senha personalizada
                for variaveis in valores_variaveis:
                    if valores[variaveis] == True:
                        while contador < 16:

                            if valores['-palavras-'] == True:

                                if contador < 6:
                                    linha_aleatoria = int(randint(0,1))
                                    palavra_aleatoria = choice(str(arquivos_6_7_letras[linha_aleatoria]).split())
                                    senha.append(palavra_aleatoria)
                                    contador += len(palavra_aleatoria)

                                elif contador == 11:
                                    palavra_aleatoria = choice(str(arquivo_4_5_letras[1]).split())
                                    senha.append(palavra_aleatoria)
                                    contador += len(palavra_aleatoria)
                                
                                elif contador == 14:
                                    palavra_aleatoria = choice(str(arquivo_2_3_letras[1]).split())
                                    senha.append(palavra_aleatoria)
                                    contador += len(palavra_aleatoria)
                                
                                else:
                                    palavra_aleatoria = choice(str(arquivo_4_5_letras[0]).split())
                                    senha.append(palavra_aleatoria)
                                    contador += len(palavra_aleatoria)
                                
                            if valores['-minusculas-'] == True:
                                if contador < 16:
                                    senha.append(choice(str(arquivo_caracteres[2]).split()))
                                    contador += 1

                            if valores['-numeros-'] == True:
                                if contador < 16:
                                    senha.append(choice(str(arquivo_caracteres[0]).split()))
                                    contador += 1

                            if valores['-maiusculas-'] == True:
                                if contador < 16:
                                    senha.append(choice(str(arquivo_caracteres[1]).split()))
                                    contador += 1

                            if valores['-especiais-'] == True:
                                if contador < 16:
                                    senha.append(choice(str(arquivo_caracteres[3]).split()))
                                    contador += 1
                
                #Caso não tenha personalização vai gerar senha aleatoria sem a opção de palavras            
                sem = gera_dados.sem_preferencia(16)
                imprime_info.imprime_senha(senha, sem)
                manipula_txt.cria_txt_normal(senha,sem)

            #informa o user caso ele não tenha selecionado um nivel 
        else:
            Windows['-Aviso-'] .update('Escolha um nível de senha')
