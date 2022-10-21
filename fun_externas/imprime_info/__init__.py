
def imprime_senha(senha=' ', senha_s=' '):
    from random import shuffle
    
    print('A sua nova senha é: ', end='')
            
    #embaralha lista para nova ordem aleatoria 
    shuffle(senha)

    #realiza ajuste de senha para apresentar no terminal
    if len(senha)> 0:
        for ajusta_espaço in senha:
            print(ajusta_espaço, end='')
        print('\n')
    
    elif len(senha_s)> 0:
        for ajusta_espaço in senha_s:
            print(ajusta_espaço, end='')
        print('\n')
