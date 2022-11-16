#maça
#chocolate
#arroz
#frango

dicionario = {
    "maça": "fruta",
    "chocolate": "doce",
    "arroz": "carboidrato",
    "frango": "proteina"
}

#print(type(dicionario))
#print(dicionario)

#retorna o valor
#for valor in dicionario.values():
 #   print(valor)

#retorna as chaves
#for chave in dicionario.keys():
#    print(chave)

#print(dicionario["chocolate"])

#retorna uma lista de tuplas
#cada item é um tupla
print(dicionario.items())

for chave, valor in dicionario.items():
    print("{} -- {}".format(chave,valor))