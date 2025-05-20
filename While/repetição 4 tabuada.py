while True:
    print("Menu")
    print("")
    print("[1] fatorial")
    print("[2] quadrado")
    print("[3] cubo")
    print("[4] tabuada")
    print("[0] sair")
    escolha = int(input("Escolha um número "))
    if escolha == 0:
        break
    elif escolha == 1:
        n = int (input("Digite um número "))
        fatorial = 1
        while (n > 0 ):
            fatorial = fatorial*n
            n = n - 1
            print("O fatorial do número será:", fatorial)
    elif escolha == 2:
        n = int (input("Digite um número para saber o seu quadrado "))
        resultado = n * n
        print("O quadrado será:", resultado)
    elif escolha == 3:
        n = int (input("Digite um número para saber o seu cubo "))
        resultado = n* n* n
        print("O resultado do cubo será:", resultado)
    elif escolha == 4:
        n = int (input("Digite um número da tabuada "))
        print(n, 'X 1 =', n *1)
        print(n, 'X 2 =', n *2)
        print(n, 'X 3 =', n *3)
        print(n, 'X 4 =', n *4)
        print(n, 'X 5 =', n *5)
        print(n, 'X 6 =', n *6)
        print(n, 'X 7 =', n *7)
        print(n, 'X 8 =', n *8)
        print(n, 'X 9 =', n *9)
        print(n, 'X 10 =', n *10)
    elif escolha == 0:
        print("Sair")