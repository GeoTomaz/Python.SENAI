num = int(input("digite um número "))
def verificação_numero(num):
    if num >= 0:
        print("numero positivo")
        return True
    else:
        print("número negativo")
        return False
    
verificação_numero(num)