valorCompra = float(input("Digite o valor da compra: "))
formaPagamento= int(input('1-Dinheiro / 2-Cartão: '))

if valorCompra > 100 and formaPagamento == 2:
    valorCompra = valorCompra * 0.9
    print("Você ganhou desconto")
else:
    print("Você não ganhou desconto")

print("O valor a pagar é {}".format(valorCompra))