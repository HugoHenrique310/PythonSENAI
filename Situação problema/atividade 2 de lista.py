lista_nomes = []

while True:
    print("menu")
    print("")
    print("1 - Cadastrar nome ")
    print("2 - Verificar a quantidade de nomes na lista ")
    print("3 - Exibir a lista de nomes em ordem alfabética ")
    print("4 - Consulta de um nome ")
    escolha = int(input("Escolha uma das opções "))
    
    if escolha == 1:
        nome = input("Digite seu nome ")
        if nome in lista_nomes:
            print("Este nome já está na lista")
        else:
            lista_nomes.append(nome)
            print("Seu nome foi adicionado com sucesso")
    elif escolha == 2:
        print(" A lista tem", len(lista_nomes ))
    elif escolha == 3:
        lista_nomes.sort()
        for nome in lista_nomes:
            print(nome)
    elif escolha == 4:
        consulta_nome = input("Consultar  nome ")
        if consulta_nome in lista_nomes:
            opção = input(" Nome encontrado! Deseja removê-lo? (s/n)")
            if opção == "s":
                lista_nomes.remove (consulta_nome)
                print("Nome removido com sucesso")
        else:
            opção1 = input(" Nome não encontrado. Deseja adicioná-lo? (s/n)")
            if opção1 == "s":
                lista_nomes.append(consulta_nome)
                print("Nome adicionada a lista com sucesso")
                
              
