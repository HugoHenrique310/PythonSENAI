import random
print("Olá jogador bem vindo ao jogo de par ou ímpar")
print("Para começar a jogar você deve escolher se quer ser par ou ímpar")
print("A partir da sua opção serei o oposto")
print("Você deve escolher um número de 1 a 10")
print("Você só ganha quando a soma do seu número e do meu número seja igual a opção que você escolheu")

while True:
    print("Menu Game")
    print("[1] - Ímpar ")
    print("[2] - Par")
    print("[3] - Sair")
    escolha = int(input("Escolha um número: "))
    if escolha == 1:
        print("A opção selecionada é ímpar")
        n1 = int (input("Escolha um número de 1 a 10: "))
    elif escolha == 2:
        print("A opção selecionada é par")
        n1 = int (input("Escolha um número de 1 a 10: "))
    elif escolha == 3:
        print("Sair")
        break
    n_aleatorio = random.randint(1,10)
    
    print("Maquina", n_aleatorio)
    soma = n_aleatorio + n1
    print("O resultado é", soma)
    if soma % 2 == 0:
        if escolha == 1:
            print("O jogador perdeu")
        else:
             print("O jogador venceu")
    else:
        print("")
        if escolha == 2:
            print("O jogador perdeu")
        else:
            print("O jogador venceu")