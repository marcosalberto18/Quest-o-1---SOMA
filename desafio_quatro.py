#
sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53


calculo1 = sp / 180759.98 * 100

calculo2 = rj / 180759.98 *  100

calculo3 = mg / 180759.98 * 100

calculo4 = es /180759.98 * 100

calculo5 = outros / 180759.98 * 100


variavel = input('digite um mês: (SP, RJ, MG, ES, Outros): ').lower().strip()


if variavel == "sp":
   print(f'{calculo1:.2f}%')
elif variavel == "rj":
    print(f'{calculo2:.2f}%')
elif variavel == "mg":
    print(f'{calculo3:.2f}%')
elif variavel == "es":
    print(f'{calculo3:.2f}%')
elif variavel == "outros":
    print(f'{calculo4:.2f}%')
else:
    print('mês invalido!')