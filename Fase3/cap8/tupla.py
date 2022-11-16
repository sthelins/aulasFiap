#tuplas são imutaveis
# pode navegar usando loop
#ocupam menos espaço que as listas na memoria RAM

categorias = ("comida", "roupa", "eletrodomestico")

print(categorias)

print(categorias[0])

#desempacotar
teste1, teste2, teste3 = categorias

print(teste1)
print(teste2)
print(teste3)

for categoria in categorias:
    print(categoria)

