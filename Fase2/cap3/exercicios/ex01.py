#Quantos alimentos o usuário consumiu e depois informar as calorias deles
# depois informar o total de calorias no final

qtndAlimentos = int(input("Informe quantos alimentos você consumiu hoje  "))
i = 0
soma = 0


while i < qtndAlimentos:
    calorias = float(input(f"Informe a caloria do alimento {i + 1}: "))
    i += 1
    soma = soma + calorias

print(f"O total de calorias consumidas foi {soma}")

somaFor = 0
caloriasFor = 0
for alimento in range(1, qtndAlimentos + 1):
    caloriasFor = float(input(f"Informe a caloria do alimento {alimento}: "))
    somaFor += caloriasFor

print(f"O total de calorias consumidas foi {somaFor}")