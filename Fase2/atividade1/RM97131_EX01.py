#Sthefany Lins de Albuquerque

#entrada - assinatura do cliente, faturamento anual
#calcular valor do bonus
#saída - o valor do bonus e o que o cliente deve pagar

#BASIC - 30%
#SILVER - 20%
#GOLD - 10%
#PLATINUM - 5%

print("Digite o número de acordo com o sua assinatura")
assinatura = int(input("1 - BASIC| 2 - SILVER| 3 - GOLD | 4 - PLATINUM  "))
faturamento = float(input("Agora, digite seu faturamento anual  "))
pagamento = 0
bonus = 0

if assinatura == 1:
    pagamento = faturamento * 0.3
    bonus = 30
elif assinatura == 2:
    pagamento = faturamento * 0.2
    bonus = 20
elif assinatura == 3:
    pagamento = faturamento * 0.1
    bonus = 10
elif pagamento == 4:
    pagamento = faturamento * 0.05
    bonus = 5
else:
    print("Plano não existente")

print(f"O bônus é {bonus}% e o que deve ser pago é R${pagamento}")

