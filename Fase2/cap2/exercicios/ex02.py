#Uma agência de viagens ofertará descontos progressivos na compra de pacotes, dependendo do número
#de viajantes que estão no mesmoo grupo e moram na mesma residência

#receber valor bruto do pacote; categoria de assentos no voo; quantidade de viajantes que moram na mesma
#casa; calcular os descontos de acordo com a tabela:

#ECONÔMICA 2 viajantes 3%
#          3 viajantes 4%
#          4 ou mais viajantes 5%
#----------------------------------------
#EXECUTIVA 2 viajantes 5%
#          3 viajantes 7%
#          4 ou mais viajantes 8%
#----------------------------------------
#PRIMEIRA CLASSE 2 viajantes 10%
#                3 viajantes 15%
#                4 ou mais viajantes 20%

#O programa deverá exibir o valor Bruto da viagem, o valor do desconto, valor líquido da viajante
#e o valor médio por viajante

print("Por favor, Digite os números a seguir de acordo com a classe:")
classe = int(input("1 - Econômica | 2 - Executiva | 3 - Primeira classe  "))

viajantes = int(input("Quantos serão os viajantes que moram na mesma casa?  "))
valorBruto = float(input("Informe o valor bruto da viagem:  "))
valorDesconto = 0
valorLiquido = 0

if classe == 1:
    if viajantes == 1:
        print("Você não ganhou descontos")
    if viajantes == 2:
        valorDesconto = valorBruto * 0.03
    if viajantes == 3:
        valorDesconto = valorBruto * 0.04
    if viajantes >= 4:
        valorDesconto = valorBruto * 0.05
elif classe == 2:
    if viajantes == 1:
        print("Você não ganhou descontos")
    if viajantes == 2:
        valorDesconto = valorBruto * 0.05
    if viajantes == 3:
        valorDesconto = valorBruto * 0.07
    if viajantes >= 4:
        valorDesconto = valorBruto * 0.08
elif classe == 3:
    if viajantes == 1:
        print("Você não ganhou descontos")
    if viajantes == 2:
        valorDesconto = valorBruto * 0.1
    if viajantes == 3:
        valorDesconto = valorBruto * 0.15
    if viajantes >= 4:
        valorDesconto = valorBruto * 0.2
else:
    print("Categoria inexistente")

valorLiquido = valorBruto - valorDesconto
print( f"Voces ganharam um desconto de R${valorDesconto},portanto o valor da viajem ficará R${valorLiquido}")

