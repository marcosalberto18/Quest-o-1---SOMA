numero_int = input('Digite um número inteiro: ')
numero_int_2 = int(numero_int)
numero_int_par = numero_int_2 % 2 



if numero_int.isdigit():
    print(f'Seu {numero_int_2} é inteiro!')
    if numero_int_par == 0:
        print('Seu número é par!')
    else:
        print('Seu número é impar!') 
else: 
    print(f'Esse número não é inteiro!') 

  