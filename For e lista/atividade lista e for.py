# Etapa 1 - Criar uma lista de objetos com 5 itens
objetos = ["CPF", "carteira", "celular", "dinheiro", "caneta"]
print("lista de objetos criados")

# Etapa 2 - Adicionar mais um objeto ao final da lista
objetos.append("Espelho")
print("Espelho adicionado ao final da lista")

# Etapa 3 - Acessar o objeto que está na 2 posição e exiba-o
print("Acesso do objeto na 2 posição")
print(objetos[1])

# Etapa 4 - Remover um objeto da lista e exiba-o
print(objetos.pop(1))
print("Carteira removida da lista")

# Etapa 5 - Exibir o tamanho da lista
print(" A lista tem", len(objetos))

# Etapa 6 - Utilizar for para mostrar todos os itens
for objeto in objetos:
    print(objeto)
    
# Etapa 7 - Verificar se "cadeira" está na lista. Se sim remova- a, senão adicione.
if " cadeira" in objetos:
    objetos.remove("Cadeira")
    print("Cadeira removida")
else:
    objetos.append("cadeira")
    print("Cadeira adicionada na lista")
    
# Etapa 8 - Ordene a lista em ordem alfabética, exiba o antes e o depois.
print(objetos)
objetos.sort()
print(objetos)

# Etapa 9 - Exiba o primeiro e o último objeto e exiba eles.
x = len(objetos)
n1 = objetos [0]
n2 = objetos[x - 1] 
print("O Primeiro objeto é o " , n1, " , já o  último objeto é o ", n2)

# Etapa 10 - Limpe toda a lista
objetos.clear()
