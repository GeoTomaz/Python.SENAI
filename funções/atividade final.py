import inputs

alunos = []

def menu():
    print("MENU")
    print("[1] - informar o nome do aluno")
    print("[2] - exibir um resumo final com o nome de cada aluno e sua situação")
    print("[3] - sair ")

  
  
def calcular_media(nota1, nota2, nota3):
    soma_media = nota1 + nota2 + nota3
    media = soma_media / 3
    return media

def verificar_situacao(media):
    if media >= 7:
        return "aprovado"
    elif media > 5 and media < 6.9:
        return "repcuperação"
    elif media < 5:
        return "reprovado"
        
def cadastrar_aluno():
    nome = inputs.input_str("digite seu nome ")
    nota1 = inputs.input_int("digite a nota ")
    nota2 = inputs.input_int("digite a nota ")
    nota3 = inputs.input_int("digite a nota ")
    
    media = int(calcular_media(nota1, nota2, nota3))
    situacao = verificar_situacao(media)
    
    aluno = {
            "nome": nome,
            "nota1": nota1,
            "nota2": nota2,
            "nota3": nota3,
            "media": media,
            "situacao": situacao
            }
    if aluno in alunos:
        print("este nome já está na lista ")
    else:
        alunos.append(aluno)
        print("nome do aluno adicionado ")
        
def mostrar_relatorio(alunos):
    for aluno in alunos:
        print("")
        print("NOME -",f" {aluno['nome']}")
        print("MÉDIA -",f" {aluno['media']}")
        print("SITUAÇÃO -",f" {aluno['situacao']}")
        print("")

while True:
    menu()
    opção = inputs.input_int("escolha uma opção ")
    if opção == 1:
        cadastrar_aluno()
    elif opção == 2:
        mostrar_relatorio(alunos)
    elif opção == 3:
        break
        

        
    
    
    