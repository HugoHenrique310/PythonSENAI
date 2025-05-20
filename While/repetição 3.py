quanti = 0
valor_total = 0


while True:
    print("Menu")
    print("")
    print("0 - Sair")
    print("1 - Mostrar a quantidade e o valor total das despesas")
    print("2 - Adicionar valor da despesa")
    escolha = int(input("Escolha um número "))
    
    if escolha == 1:
        print("A quantidade é ", quanti, "E o valor total é ", valor_total)
    elif escolha == 2:
        valor = int(input("Digite um valor "))
        quanti += 1
        valor_total = valor_total + valor
    elif escolha == 0:
        print("Sair")
        break
    