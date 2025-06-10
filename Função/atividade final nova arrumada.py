import inputs

alunos = []

def cadastro_aluno():
    nome = inputs.input_str ("Digite o nome do aluno ")
    nota1 = inputs.input_float("Digite uma nota: ")
    nota2 = inputs.input_float("Digite outro nota: ")   
    nota3 = inputs.input_float("Digite outro nota: ")
    media = int(calcular_media(nota1,nota2,nota3))
    estado = indicar_estado_aluno(media)  
        
    aluno1 = {
        "nome": nome,
        "nota1": nota1,
        "nota2": nota2,
        "nota3": nota3,
        "media": media,
        "estado": estado,           
    }
    
    if aluno1 in alunos:
            print("Esse aluno já está na lista")
        
    else:
        alunos.append(aluno1)
        print("Aluno cadastrado")        
        
def calcular_media(nota1,nota2,nota3):
    soma = nota1 + nota2 + nota3
    media = soma / 3
    return media              
    
def indicar_estado_aluno(media):
    if media >= 7:
        return "Aprovado"
            
    elif media >= 5 and media <= 7:
        return "Recuperação"
    
    elif media < 5:
        return "Reprovado"
def exibir_relatorio(alunos):
    for aluno in alunos:
        print("")
        print("Nome -",f" {aluno['nome']}")
        print("Media -",f" {aluno['media']}")
        print("Estado -",f" {aluno['estado']}")
        print("")    

while True:
    print("Menu")
    print("")
    print("[1] Informar o nome do aluno ")
    print("[2] Cadastrar vários alunos e exibir um resumo final com o nome de cada aluno e sua situação")
    print("[3] Sair ")
    print("")
    escolha = inputs.input_int("Escolha uma das opções ")
    if escolha == 1:
        cadastro_aluno()
    elif escolha == 2:
        exibir_relatorio(alunos)
    elif escolha == 3:
        print("Sair")
        break       