dicionario = {}

#inserir um novo  via código
dicionario["Sthefany"] = "estudante"
dicionario["André"] = "professor"
dicionario["Felipe"] = "diretor"


#remover um dado
dicionario.pop('André')
for nome, cargo in dicionario.items():
    print(f"Colaborador: {nome} - {cargo}")

#remover o ultimo elemento
dicionario.popitem()
print("")

for nome, cargo in dicionario.items():
    print(f"Colaborador: {nome} - {cargo}")