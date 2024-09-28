hora = input('Digite a hora atual: ')
hora_1 = int(hora)


if  hora_1 <= 11:
    print('Você está pela manhã, bom dia!') 
elif hora_1 <= 18:
    print('Você está pela tarde, boa tarde!')
elif hora_1 <= 24:
    print('Você está de noite, boa noite!')
else:
    print('Desculpe, esse não é um horário válido!')