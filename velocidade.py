velocidade = 61
local_carrokm = 101

RADAR_1 = 60
LOCAL_1 = 99
RADAR_RANGE = 1

if local_carrokm <= LOCAL_1:
    print('Radar (60KM/H) a frente!')
else:
    print("Passou por um radar!")  
if velocidade <= RADAR_1:
    print('Está dentro da velocidade permitida pelo radar!')
else:
    print('O carro ultrapassou o limite de velocidade permitido.')
      