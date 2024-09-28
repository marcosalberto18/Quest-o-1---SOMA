nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:  
    print(f'Seu nome é {nome}')
    print(f'esse é seu nome invertido: {(nome [-1::-1])}')
    print(f'Seu nome tem {len(nome [0::1])} letras')
    print(f'A primeira letra do seu nome é: {(nome [0:1:1])}')
    print(f'A última letra do seu nome é: {(nome [:-2:-1])}')
    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('seu nome não contém espaços')
else:
    print('Desculpe, não detectamos nenhum caracter!')            