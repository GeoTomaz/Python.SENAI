ano_nascimento = int(input("digite o ano do seu nascimento "))
idade = 2025 - ano_nascimento
if idade <= 10:
    print("essa pessoa é uma criança ")
elif idade >= 11 and idade <= 17:
    print("essa pessoa é adoslencente ")
elif idade >= 18 and idade <= 59:
    print("essa pessoa é adulta ")
elif idade >= 60 and idade <= 115:
    print("essa pessoa é idosa ")
else:
    print("morreu já ")
