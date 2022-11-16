dicionario = {}

#inserir um novo  via código
dicionario["Sthefany"] = "estudante"
dicionario["André"] = "professor"

#inserir dados por uma fonte ativida
nome_colaborador = input("Informe o nome do colaborador: ")
cargo_colaborador = input("Informe o cargo do colaborador: ")

dicionario[nome_colaborador] = cargo_colaborador
for nome, cargo in dicionario.items():
    print(f"Colaborador: {nome} - {cargo}")

#alterar um dado
dicionario["André"] = "recruta"

dicionario[nome_colaborador] = cargo_colaborador
for nome, cargo in dicionario.items():
    print(f"Colaborador: {nome} - {cargo}")


