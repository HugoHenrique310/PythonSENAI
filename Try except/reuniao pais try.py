import inputs

lista_reuniao = []
lista_presente = []
lista_ausente = []


while True:
    print("menu")
    print("")
    print("1 - Cadastrar nome dos pais ")
    print("2 - exibir o total de pais ")
    print("3 - Exibir a lista de nomes em ordem alfabética ")
    print("4 - Confirmação de presença dos pais ")
    print("5 - Relatório de pais presetes e ausentes ")
    print("6 - sair ")
    escolha = inputs.input_int("Escolha uma das opções")
    
    if escolha == 1:
        nome = inputs.input_str("Digite seu nome ")
        if nome in lista_reuniao:
            print("Este nome já está na lista")
        else:
            lista_reuniao.append(nome)
            print("Seu nome foi adicionado com sucesso")
    elif escolha == 2:
            print(" A lista tem", len(lista_reuniao ))
    elif escolha == 3:
        lista_reuniao.sort()
        for nome in lista_reuniao:
            print(nome)
    elif escolha == 4:
        for nome in lista_reuniao:
            print(nome)
            nome_consulta = inputs.input_str("está presente? (s/n)")
            if  nome_consulta == "s":
                lista_presente.append(nome)
                print(" Está presente")
            else:
                lista_ausente.append(nome)
                print(" Está ausente")
    elif escolha == 5:
        print("Pais presentes na reunião ")
        for nome in lista_presente:
            print(nome)
            print("")
        print("Pais ausentes na reunião ")
        for nome in lista_ausente:
            print(nome)
            print("")
            
    elif escolha == 6:
        print("Sair")
        break
         
     
                
    