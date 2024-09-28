nome = input('Digite seu primeiro nome: ')
um1 = len(nome)
um2= len(nome)

if um1 <= 4:
    print('Seu nome tem até 4 letras, é curto!')
elif um1 >= 5 and um2 <= 6:
    print(f'seu nome tem entre 5 e 6 letras, é normal!')
else:
    print('Seu nome tem mais de 6 letras, é grande!')