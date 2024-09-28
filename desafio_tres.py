dias_valores = [{"dia": 1,
		"valor": 22174.1664},{"dia": 2,
		"valor": 24537.6698},{"dia": 3,
		"valor": 26139.6134},{"dia": 4,
		"valor": 0.0},{"dia": 5,
		"valor": 0.0},{"dia": 6,
		"valor": 26742.6612},{"dia": 7,
		"valor": 0.0},{"dia": 8,
		"valor": 42889.2258},{"dia": 9,
		"valor": 46251.174},{"dia": 10,
		"valor": 11191.4722},{"dia": 11,
		"valor": 0.0},{"dia": 12,
		"valor": 0.0},{"dia": 13,
		"valor": 3847.4823},{"dia": 14,
		"valor": 373.7838},{"dia": 15,
		"valor": 2659.7563},{"dia": 16,
		"valor": 48924.2448},{"dia": 17,
		"valor": 18419.2614},{"dia": 18,
		"valor": 0.0},{"dia": 19,
		"valor": 0.0},{"dia": 20,
		"valor": 35240.1826},{"dia": 21,
		"valor": 43829.1667},{"dia": 22,
		"valor": 18235.6852},{"dia": 23,
		"valor": 4355.0662},{"dia": 24,
		"valor": 13327.1025},{"dia": 25,
		"valor": 0.0},{"dia": 26,
		"valor": 0.0},{"dia": 27,
		"valor": 25681.8318},{"dia": 28,
		"valor": 1718.1221},{"dia": 29,
		"valor": 13220.495},{"dia": 30,
		"valor": 8414.61}]

soma = sum(dia['valor'] for dia in dias_valores)
dias = len([dia for dia in dias_valores if dia['valor'] > 0])

pergunta = input("O que deseja saber: ").lower().strip()

if pergunta == "maior dia" or pergunta == "quero saber o maior dia":
    numero_maior = max(dias_valores, key=lambda x: x['valor'])
    print(f'O maior valor é:{numero_maior['valor']}, no dia {numero_maior['dia']}')
elif pergunta == "menor dia" or pergunta == "quero saber o menor dia":
    numero_menor = min([d for d in dias_valores if d['valor'] > 0], key=lambda x: x['valor'] )
    print(f'Sem contar os dias cujos valores estão zerados, o menor valor é: {numero_menor['valor']}, no dia {numero_menor['dia']}')
elif pergunta == "quantidade de dias em que os valores superaram a média total":
	media_mensal = soma / dias
	print(f'{media_mensal:.2f} é a média mensal!')
    
	dias_acima_media = sum(1 for dia in dias_valores if dia['valor']>media_mensal)
	print(f'foram {dias_acima_media} dias acima da média mensal')

else:
	print('Comando invalido!')
	
    
