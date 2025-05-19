from datetime import datetime

def hora_atual(nome):
    hora = datetime.now().hour
    if hora > 0 and hora <= 5:
        print("boa madrugada ", nome)
    elif hora > 5 and hora <= 12:
        print("bom dia ", nome)
    elif hora > 12 and hora <= 19:
        print("boa tarde ", nome)
    else:
        print("boa noite ", nome)

hora_atual(input("digite seu nome "))                