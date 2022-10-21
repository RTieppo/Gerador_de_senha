import os
from shutil import copyfile
from fun_externas import gera_dados

def limpa_arq():

     while True:
            valida_arquivos = os.listdir(r'C:\Users\Public')

            if 'gerador de senha' in valida_arquivos:
                
                verifica_arquivos = os.listdir(r'C:\Users\Public\gerador de senha')

                if 'senha.txt' in verifica_arquivos:
                    os.remove(r'C:\Users\Public\gerador de senha\senha.txt')

                if 'fonetica.txt' in verifica_arquivos:
                    os.remove(r'C:\Users\Public\gerador de senha\fonetica.txt')

                os.rmdir(r'C:\Users\Public\gerador de senha')
            else:
                break

def cria_ark_ini():
    while True:
        pasta = os.listdir(r'C:\Users\Public')

        if 'gerador de senha' in pasta:
            break

        else:
            os.makedirs(r'C:\Users\Public\gerador de senha')

def cria_txt_fonetico():
    criar_arquivo = open(r'C:\Users\Public\gerador de senha\fonetica.txt', 'w', encoding='utf-8')
    criar_arquivo.write('Sua nova senha é: ')
    criar_arquivo.close()

    for ajusta in gera_dados.senha_f:
        escreve_linha1 = open(r'C:\Users\Public\gerador de senha\fonetica.txt', 'a', encoding='utf-8')
        escreve_linha1.write(f'{ajusta[0]}')
        escreve_linha1.close()
        
    nova_linha = open(r'C:\Users\Public\gerador de senha\fonetica.txt', 'a', encoding='utf-8')
    nova_linha.write(f'\n\nPara melhor memorização grave as seguintes palavras: ')
    nova_linha.close()
        
    for ajusta_f in gera_dados.palavras_foneticas[0]:
        escreve_linha2 = open(r'C:\Users\Public\gerador de senha\fonetica.txt', 'a', encoding='utf-8')
        escreve_linha2.write(f'{ajusta_f} ')
        escreve_linha2.close()

def cria_txt_normal(senha=' ', senha_s=' '):
    criar_arquivo = open(r'C:\Users\Public\gerador de senha\senha.txt', 'w', encoding='utf-8')
    criar_arquivo.write('Sua nova senha é: ')
    criar_arquivo.close()

    if len(senha)>0:
        for ajusta_espaço in senha:
            criar_arquivo = open(r'C:\Users\Public\gerador de senha\senha.txt', 'a', encoding='utf-8')
            criar_arquivo.write(f'{ajusta_espaço}')
            criar_arquivo.close()
    elif len(senha_s) > 0:
        for ajusta_espaço in senha_s:
            criar_arquivo = open(r'C:\Users\Public\gerador de senha\senha.txt', 'a', encoding='utf-8')
            criar_arquivo.write(f'{ajusta_espaço}')
            criar_arquivo.close()

def salva_arquivo(fonetica=False):
    #Abre informações gerais do pc
    sistema = os.environ
    #indentifica user
    user = sistema['USERNAME']
    
    #Unifica user com caminho e gera lista
    caminho1 = os.path.join(r'C:\Users',user,r'Desktop')

    #unifica caminho final e grava txt
    caminho2 = os.path.join(caminho1,r'senha.txt')

    caminho3 = os.path.join(caminho1,r'fonetica.txt')

    if fonetica == False:
        copyfile(r'C:\Users\Public\gerador de senha\senha.txt',caminho2)
    
    else:
        copyfile(r'C:\Users\Public\gerador de senha\fonetica.txt', caminho3)