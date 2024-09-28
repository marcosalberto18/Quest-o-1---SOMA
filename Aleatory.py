from time import sleep
from random import randint 

print('=-' * 10)
print('JOGO PIROCUDO')
print('=-' * 10)
print('Escolha um numero ')
print('[1] Pedra')
print('[2] Papel')
print('[3] Tesoura')
jogada = int(input('Digite um dos números acima:'))

if jogada == 1:
    print('Você escolheu ---> Pedra! <---')
elif jogada == 2:
    print('Você escolheu ---> Papel <---')
elif jogada == 3:
    print('Você escolheu ---> Tesoura <---')

pc = randint(1,3)

if pc == 1:
    print('O PC jogou pedra ')
    if jogada == 1:
        print('O jogo empatou!')
    elif jogada == 2:
        print('Você ganhou!')
    elif jogada == 3:
        print('Você PERDEU HAHAH!')
if pc == 2:
    print('O pc jogou Papel')
    if jogada == 2:
        print('O jogo empatou!')
    elif jogada == 1:
        print('Você ganhou!')
    elif jogada == 3:
        print('Você perdeu HAHAH!')
if pc == 3:
    print('O pc jogou Tesoura!')
    if jogada == 3:
        print('O jogo empatou!')
    elif jogada == 2:
        print('Você perdeu HAHAH!')
    elif jogada == 1:
        print('Você ganhou!') 
        

        



