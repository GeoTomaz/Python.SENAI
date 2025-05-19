num1 = int(input("digite um número "))
num2 = int(input("digite outro número "))
soma = num1 + num2
media = soma / 2
if num1 > 0 and num1 <= 100 and num2 > 0 and num2 <= 100:
    print("")
    if media >= 70 and media <= 100:
        print("o aluno está aprovado ")
    elif media > 50 and media < 70:
        print("o aluno está de recuperação ")
    elif media < 50:
        print("o aluno está reprovado ")
else:
    print("algo está errado,digite um número de 0 a 100 ")
    