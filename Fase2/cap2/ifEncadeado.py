#>1000 3gb
#>500 1,5gb
#>200 500mb
#<200 nada

pontuacao = int(input("Informe a pontuação: "))

if pontuacao > 1000:
    print("Você ganhou 3gb de bônus")
else:
    if pontuacao > 500:
        print("Você ganhou 1.5gb de bônus")
    else:
        if pontuacao > 200:
            print("Você ganhou 500mb de bônus")
        else:
            print("Você não ganhou nada")