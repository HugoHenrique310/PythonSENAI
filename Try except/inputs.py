def input_str(mensagens):
    while True:
        name = str(input(mensagens))
        if  not name.isalpha():
            print("Digite apenas letras")
        else:
            return name
                   
def input_int(mensagens):
    while True:
        try:
            numero = int(input(mensagens))
            return numero
        
        except ValueError:
            print("Digite somente números ex:6")
            
            
def input_float(mensagens,casa):
    while True:
        try:
            nm = float(input(mensagens))
            return round (nm, casa)
        
        except ValueError:
            print("Digite somente números ex:6")
            
            