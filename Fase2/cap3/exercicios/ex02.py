# entrada - transações financeiras ao longo do dia e o valor de cada transação
# saída - valor gasto no total e media
qtndTransações = int(input("Digite quantas transações você fez hoje:  "))
soma = 0

for gasto in range(1, qtndTransações + 1):
    valor = float(input(f"Digite o valor da transação {gasto}: "))
    soma += valor

media = soma / qtndTransações
print(f"Você gastou no total R${soma} e a média de cada transação foi de {media:.2f}")