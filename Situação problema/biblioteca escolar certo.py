import inputs
lista_livros = []

while True:
    print("Biblioteca Escolar")
    print("")
    print("1 - Cadastrar livro ")
    print("2 - Verificar a quantidade de livros na lista ")
    print("3 - Exibir a lista de livros em ordem alfabética e o titulo dos livros ")
    print("4 - Buscar  livros de um autor específico ")
    print("5 - Buscar todos os livros de  determinada categoria. ")
    print("6 - Editar os dados de um livro. ")
    print("0 - Sair ")
    escolha = inputs.input_int("Escolha uma das opções ")
    
    if escolha == 1:
        titulo = inputs.input_str ("Digite o título do livro ")
        autor = inputs.input_str("Digite o nome do autor do livro ")
        categoria = inputs.input_str("Digite a categoria do livro ")
        isbn = inputs.input_int("Digite a ISBN livro ")
        ano_de_publicacao = inputs.input_int("Digite o ano de publicação do livro ")
        
        livro1 = {
            "titulo": titulo,
            "autor": autor,
            "categoria": categoria,
            "isbn": isbn,
            "ano_de_publicacao": ano_de_publicacao,
        }

        for livro in lista_livros:
            if livro ["isbn"] == livro1["isbn"]:
                print("")
                print("Esse isbn já está na lista")
                break
            else:
                lista_livros.append(livro1)
                print("Livro cadastrado")
        else:
            lista_livros.append(livro1)
            print("Livro cadastrado")
                
        
            
    elif escolha == 2:
        print(" A lista tem", len(lista_livros))
        
    elif escolha == 3:
        for valores in lista_livros:
            print(f"{valores['titulo']}")
            
    elif escolha == 4:
        autor = inputs.input_str("Autor (a)")
        for livro in lista_livros:
            for chave,valor in livro.items():
                if autor == livro["autor"]:
                    print(f"  {chave}:{valor}")
            print("")
            
    elif escolha == 5:
        categorias = inputs.input_str("categoria ")
        for livro in lista_livros:
            for chave,valor in livro.items():
                if categorias == livro["categoria"]:
                    print(f"  {chave}:{valor}")
            print("")
            
    elif escolha == 6:
        print("Digite o isbn:")
        print("")
        alterar = inputs.input_int ("escolha:")
        for livro in lista_livros:
            if alterar == livro ["isbn"]:
                livro["titulo"] = inputs.input_str("titulo ")
                livro["autor"] = inputs.input_str("autor ")
                livro["categoria"] = inputs.input_str("categoria ")
                livro["ano_de_publicacao"] = inputs.input_int("ano de publicação ")
        
        
    if escolha == 0:
        print("Sair")
        break
