primeiro_numero = (input('Digite o primeiro número: '))
segundo_numero = (input('Digite o segunto número: '))
operação = (input('sua operação é (+-*/):  '))

numero_valido = None

operação_1 = '+-*/'


try:
    numero_1 = float(primeiro_numero)
    numero_2 = float(segundo_numero)
    numero_valido = True
except:
    numero_valido = None
    print('Esse número não é válido')
if numero_valido is None:
    print('Esse número não é válido')
    continue
if len(operação) > 1:
    print('Digite apenas um sinal de operação!')
    continue
if operação not in operação_1:
    print('Digite uma operação válida "+ = /*"')
    continue