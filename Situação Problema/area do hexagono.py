#1-calcular a área do hexágono

#passo a passo
#1-obtenha o número do lado do triângulo
#2-multiplique esse número por ele mesmo
#3-calcule a raiz
#4-multiplique o lado do triângulo pela raiz
#5-divida o resultado da multiplicação por 4
#6-multiplique o resultado da divisão por 6
#7-exiba o resultado

lado = int(input("escreva um número do lado dos triângulos "))
quadrado = lado * lado
raiz = round(3 ** 0.5)
multiplicaçao = raiz * quadrado
at = multiplicaçao / 4
ah = 6 * at
print("a área do hexagono é ", ah)