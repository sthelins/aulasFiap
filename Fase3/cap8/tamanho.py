#primeiro importamos o módulo sys
import sys
#depois criamos algumas variáveis de exemplo
nome = "Bruce Wayne"
idade = 30
peso = 92.3
#Vamos exibir em uma mensagem o nome da variável, o tipo (type) e o tamanho (getsizeof)
print("A variável nome é do tipo {} e tem {} bytes".format(type(nome), sys.getsizeof(nome)))
print("A variável idade é do tipo {} e tem {} bytes".format(type(idade), sys.getsizeof(idade)))
print("A variável peso é do tipo {} e tem {} bytes".format(type(peso), sys.getsizeof(peso)))

#agora vamos criar uma lista vazia
lista = []
#E verificar o tamanho
print("O objeto lista é do tipo {} e tem {} bytes".format(type(lista), sys.getsizeof(lista)))

#criar tupla vazia
tupla_vazia = ()

#printando o tipo e tamanho 
print("O objeto tupla_vazia é do tipo {} e ocupa {} bytes na memória".format(type(tupla_vazia), sys.getsizeof(tupla_vazia)))