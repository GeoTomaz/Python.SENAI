# Etapa 1 - criar uma lista com 5 objetos
objetos = ["lapis ", "borracha ", "apontador ", "cola ", "tesoura "]
print("lista de objetos ", objetos)

# Etapa 2 - adicionar mais um objeto na lista
objetos.append("caneta ")
print("caneta adicionada na lista de objetos ")

# Etapa 3 - acessar o objeto da 2° posição e exibir
print("na segunda posição está a ", objetos[1])

# Etapa 4 - remover um objeto da lista e exibir
print(objetos.pop(4), "removida ")


# Etapa 5 - exibir o tamanho da lista
print("a quantidade de objetos é ", len(objetos))

# Etapa 6 - mostrar os itens com o for
print("LISTA ")
for objeto in objetos:
    print(objeto)

# Etapa 7 - verifique se "cadeira" esta na lista, se não tiver colocar e se tiver tirar
if "cadeira" in objetos:
    objetos.remove("cadeira ")
    print("cadeira removida ")
else:
    objetos.append("cadeira ")
    print("cadeira adicionada")

# Etapa 8 - colocar a lista em ordem alfabética e exibir antes e depois
print("antes",objetos)
objetos.sort()
print("depois",objetos)

# Etapa 9 - exibir o primeiro e o ultimo objeto
x = len(objetos)
n1 = objetos[0]
n2 = objetos[x - 1]
print("primeiro objeto:", n1,"e o ultimo objeto:",n2)

# Etapa 10 - limpar a lista
objetos.clear()
print("lista limpada ")
