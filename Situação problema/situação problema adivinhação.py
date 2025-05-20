import random
print("Olá jogador bem vindo ao jogo de adivinhação")
print("Para começar a jogar eu usarei um intervalo de 0 a 100 para o jogo, você tem que adivinhar o número escolhido por mim")
print("A cada chute seu mostrarei uma mensagem se o chute está maior ou menor do que o número misterioso")
n_aleatorio = random.randint(1,100)

while True:
    n = int(input("Digite um número entre 1 e 100 "))
    if n_aleatorio > n:
        print("O número é maior que " , n)
    elif n_aleatorio < n:
        print("O número é menor que " , n)
    else:
        print("Parabens você adivinhou o número misterioso é ", n)
        print("Deseja continuar o jogo ? ")
        print("[1] - Sim ")
        print("[2] - Não")
        escolha = int(input("Escolha uma das opções: "))
        if escolha == 1:
            print("O jogo irá recomeçar")
            n_aleatorio = random.randint(1,100)

        else:
            print("Fim de jogo")
            break
        