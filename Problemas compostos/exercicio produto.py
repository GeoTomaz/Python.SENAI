# passo a passo

# 1 solicite o nome de um produto e o preço

# 2 quais informacoes preciso para chegar no resultado
# nome do produto
# preço do produto
# quanto o preço do produto diminuiu

# 3
#passo1  obtenha um produto
#passo2 obtenha o valor do produto
#passo3 aplique um desconto de 5% no valor do produto
#passo4 exiba o novo preço do produto e quanto ele diminuiu

produto = str(input("nome do produto "))
preço = float(input("preço do produto"))
porcentagem = preço / 20
valor_final = preço - porcentagem
print(" o  desconto é de " , porcentagem, "reais")
print(" o novo valor é ", valor_final, "reais")
