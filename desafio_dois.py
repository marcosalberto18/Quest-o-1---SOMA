def is_fibonacci(num):
    if num < 0:
        return False
    
    a,b = 0,1

    while a <= num:
        if a == num:
            return True

        a,b = b, a+b    
    
    return False

numero = int(input('Digite um número: '))

if is_fibonacci(numero):
    print(f'O número {numero} digitado se encontra na sequência Fibonacci')

else:
    print(f"o Número {numero} não se encontra na sequência de Fibonacci!")

    
