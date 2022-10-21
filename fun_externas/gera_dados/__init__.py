from random import choice, shuffle, randint

arquivo_caracteres = open(r'.\Txt_aqr\Caracter.txt','r', encoding='utf-8').readlines()
arquivo_2_3_letras = open(r'.\Txt_aqr\letras_2_3.txt','r', encoding='utf-8').readlines()
arquivo_4_5_letras = open(r'.\Txt_aqr\letras_4_5.txt', 'r', encoding='utf-8').readlines()
arquivos_6_7_letras = open(r'.\Txt_aqr\letras_6_7.txt', 'r', encoding='utf-8').readlines()
arquivo_fonetica = open(r'.\Txt_aqr\Alfabeto_fonetico.txt', 'r', encoding='utf-8').readlines()

senha_f = list()
palavras_foneticas = list()


#opções de 8 caracteres
def fonetica(ciclo):
    senha_f.clear()
    palavras_foneticas.clear()
    palavras = 0

    if ciclo == 8:

        print('Gerando senha de 8 carcteres...')
    
        while palavras < ciclo:

            if palavras < 3:
                palavra = choice(str(arquivo_fonetica[0]).split())
                senha_f.append(f'{palavra}')
                palavras += 1
            
            elif palavras < 4:
                numero = choice(str(arquivo_caracteres[0]).split())
                senha_f.append(f'{numero}')
                palavras +=1
            
            elif palavras < 5:
                especial = choice(str(arquivo_caracteres[3]).split())
                senha_f.append(f'{especial}')
                palavras += 1
            
            elif palavras < 6:
                palavra = choice(str(arquivo_fonetica[0]).split())
                senha_f.append(f'{palavra.capitalize()}')
                palavras += 1
            
            else:
                palavra = choice(str(arquivo_fonetica[0]).split())
                senha_f.append(f'{palavra}')
                palavras += 1
                
    elif ciclo == 12:
        print('Gerando senha de 12 carcteres...')

        while palavras < ciclo:

            if palavras < 4:
                palavra = choice(str(arquivo_fonetica[0]).split())
                senha_f.append(f'{palavra}')
                palavras += 1
            
            elif palavras < 6:
                numero = choice(str(arquivo_caracteres[0]).split())
                senha_f.append(f'{numero}')
                palavras +=1
            
            elif palavras < 7:
                especial = choice(str(arquivo_caracteres[3]).split())
                senha_f.append(f'{especial}')
                palavras += 1
            
            elif palavras < 8:
                palavra = choice(str(arquivo_fonetica[0]).split())
                senha_f.append(f'{palavra.capitalize()}')
                palavras += 1
            
            else:
                palavra = choice(str(arquivo_fonetica[0]).split())
                senha_f.append(f'{palavra}')
                palavras += 1

    elif ciclo == 16:
        print('Gerando senha de 16 carcteres...')
        while palavras < ciclo:

            if palavras < 1:
                palavra = choice(str(arquivo_fonetica[0]).split())
                senha_f.append(f'{palavra.capitalize()}')
                palavras += 1
            
            elif palavras < 2:
                especial = choice(str(arquivo_caracteres[3]).split())
                senha_f.append(f'{especial}')
                palavras += 1

            elif palavras < 7:
                palavra = choice(str(arquivo_fonetica[0]).split())
                senha_f.append(f'{palavra}')
                palavras += 1
            
            elif palavras < 9:
                numero = choice(str(arquivo_caracteres[0]).split())
                senha_f.append(f'{numero}')
                palavras +=1
            
            elif palavras < 10:
                palavra = choice(str(arquivo_fonetica[0]).split())
                senha_f.append(f'{palavra.capitalize()}')
                palavras += 1
            
            else:
                palavra = choice(str(arquivo_fonetica[0]).split())
                senha_f.append(f'{palavra}')
                palavras += 1
    
    print('A sua nova senha é: ', end='')

    shuffle(senha_f)

    palavras_foneticas.append(senha_f[:])

    for ajusta_espaço in senha_f:
        print(ajusta_espaço[0], end='')

    print('\n')

    for apresenta_palavras in palavras_foneticas[0]:
        print(apresenta_palavras, end=' ')
        
    print('\n')

def sem_preferencia(n_base):
    senha_s = list()
    contador = 0
    while contador < n_base:
        linha = int(randint(0,3))
        caracter_aleatorio = choice(str(arquivo_caracteres[linha]).split())
        senha_s.append(caracter_aleatorio)
        contador += 1
    return senha_s