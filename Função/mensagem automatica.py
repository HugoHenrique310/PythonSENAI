from datetime import datetime

nome= input ("Digite seu nome: ")

def hora_atual():
    return datetime.now().hour

def apresentar_saudação ():
    
    if hora_atual () >= 0 and hora_atual () <= 5:
        print("Boa madrugada", nome)
    
    elif hora_atual () > 5 and hora_atual () <= 12:
        print("Bom dia", nome)
    
    elif hora_atual () > 12 and hora_atual () <= 19:
        print("Boa tarde", nome)
    else:
        print("Boa noite", nome)
    
    hora_atual()
    
apresentar_saudação()

