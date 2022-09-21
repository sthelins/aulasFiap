#Criar um algorittmo onde o usuário possa digitar o voto de ccada um dos 5 mebros
#da equipe e no final exiba qual foi o console escolhidos e com quantos votos
#opcoes PLAYSTATION, XBOX e NINTENDO

print("Digite um numero de acordo com as opçoes")
voto1 = int(input("1 - PLAYSTATION| 2 - XBOX| 3 - NINTENDO "))
voto2 = int(input("1 - PLAYSTATION| 2 - XBOX| 3 - NINTENDO "))
voto3 = int(input("1 - PLAYSTATION| 2 - XBOX| 3 - NINTENDO "))
voto4 = int(input("1 - PLAYSTATION| 2 - XBOX| 3 - NINTENDO "))
voto5 = int(input("1 - PLAYSTATION| 2 - XBOX| 3 - NINTENDO "))

xbox = 0
play = 0
nin = 0

if voto1 == 1:
    play += 1
elif voto1 == 2:
    xbox += 1
elif voto1 == 3:
    nin += 1
else:
    print("O colaborador digitou uma opção inexistente e seu voto será desconsiderado")

if voto2 == 1:
    play += 1
elif voto2 == 2:
    xbox += 1
elif voto2 == 3:
    nin += 1
else:
    print("O colaborador digitou uma opção inexistente e seu voto será desconsiderado")

if voto3 == 1:
    play += 1
elif voto3 == 2:
    xbox += 1
elif voto3 == 3:
    nin += 1
else:
    print("O colaborador digitou uma opção inexistente e seu voto será desconsiderado")

if voto4 == 1:
    play += 1
elif voto4 == 2:
    xbox += 1
elif voto4 == 3:
    nin += 1
else:
    print("O colaborador digitou uma opção inexistente e seu voto será desconsiderado")

if voto5 == 1:
    play += 1
elif voto5 == 2:
    xbox += 1
elif voto5 == 3:
    nin += 1
else:
    print("O colaborador digitou uma opção inexistente e seu voto será desconsiderado")

if play > xbox and play > nin:
    print(f"O ganhador foi o PLAYSTATION, com {play} votos")
if xbox > play and xbox > nin:
    print(f"O ganhador foi o XBOX, com {xbox} votos")
if nin > xbox and nin > play:
    print(f"O ganhador foi o NINTENDO, com {nin} votos")




