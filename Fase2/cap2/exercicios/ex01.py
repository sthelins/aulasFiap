#Verificar se os batimentos cardíacos p/min se encontram na faixa adequada. Para isso, deve solicitar
#que usuário informe batimentos por minuto(BPM) e a Idade. Depois verificar em que faixa se encontra.
#abaixo, dentro ou acima

#Ate 2 anos - 120 a 140
# 8 a 17 anos - 80 a 100
# adulto sedentário - 70 a 80
#idoso 50 a 60

idade = int(input("Informe sua idade: "))
bpm = int(input("Informe seus batimento cardiácos por minuto(BPM): "))

if idade <= 2:
    if bpm >= 120 and bpm <= 140:
        print("Os batimentos estão normais")
    if bpm < 120:
        print("Os batimentos estão baixos")
    else:
        print("Os batimentos estão altos")
elif idade >=8 and idade <=17:
    if bpm >= 80 and bpm <= 100:
        print("Os batimentos estão normais")
    if bpm < 80:
        print("Os batimentos estão baixos")
    else:
        print("Os batimentos estão altos")
elif idade >=18 and idade <=60:
    if bpm >= 70 and bpm <= 80:
        print("Os batimentos estão normais")
    if bpm < 70:
        print("Os batimentos estão baixos")
    else:
        print("Os batimentos estão altos")
else:
    if bpm >= 50 and bpm <= 60:
        print("Os batimentos estão normais")
    if bpm < 50:
        print("Os batimentos estão baixos")
    else:
        print("Os batimentos estão altos")







