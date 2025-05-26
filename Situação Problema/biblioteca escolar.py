import inputs
lista_livros = []

while True :
    print("menu de gerenciamentos de cadastro de livros ")
    print("[1] - Permitir cadastrar um livro por vez ")
    print("[2] - Exibir todos os livros cadastrados de forma organizada ")
    print("[3] - Mostrar ao final a quantidade total de livros registrados ")
    print("[4] - Gerar uma lista apenas com os títulos, para usar na criação de etiquetas ")
    print("[5] - Buscar todos os livros de um autor específico")
    print("[6] - Buscar todos os livros de uma determinada categoria")
    print("[7] - Permitir editar os dados de um livro")
    print("[8] - sair ")
    
    escolha = inputs.input_int("escolha uma opção")
    
    if escolha == 1:
        
        titulo = inputs.input_str("digite o nome do livro")
        autor = inputs.input_str("digite o nome do autor")
        ano_publicacao = inputs.input_int("digite o ano de publicação")
        categoria = inputs.input_str("digite a categoria")
        isbn = inputs.input_int("digite o isnb")
        
        livro = {
            "titulo": titulo,
            "autor": autor,
            "ano de publicacao": ano_publicacao,
            "categoria": categoria,
            "isbn": isbn
            }
            
        if livro in lista_livros:
            print("este nome já está na lista ")
        else:
            lista_livros.append(livro)
            print("nome do livro adicionado ")
    
    elif escolha == 2:
        for livro in lista_livros:
           
            print("")
            print("TITULO -",f" {livro['titulo']}")
            print("ISBN -",f" {livro['isbn']}")
            print("AUTOR -",f" {livro['autor']}")
            print("CATEGORIA -",f" {livro['categoria']}")
            print("ANO DE PUBLICAÇÃO -",f" {livro['ano de publicacao']}")
            print("")
    
    elif escolha == 3:
        print("a quantidade de livros adicionados é ", len(lista_livros))
        
    elif escolha == 4:
        for titulo in lista_livros:
            print("TITULO -",f" {titulo['titulo']}")
            
    elif escolha == 5:
        autor_escolhido = inputs.input_str("digite o nome do autor")
        for livro in lista_livros:
            if autor_escolhido == livro['autor']:
                print("")
                print("TITULO -",f" {livro['titulo']}")
                print("ISBN -",f" {livro['isbn']}")
                print("AUTOR -",f" {livro['autor']}")
                print("CATEGORIA -",f" {livro['categoria']}")
                print("ANO DE PUBLICAÇÃO -",f" {livro['ano de publicacao']}")
                print("")
    
    elif escolha == 6:
        categoria_escolhida = inputs.input_str("digite a categoria")
        for livro in lista_livros:
            if categoria_escolhida == livro['categoria']:
                print("")
                print("TITULO -",f" {livro['titulo']}")
                print("ISBN -",f" {livro['isbn']}")
                print("AUTOR -",f" {livro['autor']}")
                print("CATEGORIA -",f" {livro['categoria']}")
                print("ANO DE PUBLICAÇÃO -",f" {livro['ano de publicacao']}")
                print("")
                
    elif escolha == 7:
        isbn_editar = inputs.input_int("digite o ISBN do livro que deseja editar:")
        for livro in lista_livros:
            if livro['isbn'] == isbn_editar:
                print("livro encontrado. Faça as alterações:")
                livro['titulo'] = inputs.input_str("digite um novo titulo:")
                livro['isbn'] = inputs.input_int("digite um novo ISBN:")
                livro['categoria'] = inputs.input_str("digite uma nova categoria:")
                livro['ano de publicacao'] = inputs.input_int("digite um novo ano d epublicação:")
                livro['autor'] = inputs.input_str("digite um novo autor:")
                print("dados do livro atualizados com sucesso")
            else:
                print("livro não encontrado")
            
    elif escolha == 8:
        print("saindo... ")
        break