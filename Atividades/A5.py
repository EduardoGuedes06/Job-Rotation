#Escreva um programa que inverta os caracteres de um string.

def String_invertida(string): 
    if len(string) == 0: 
        return string 
    else: 
        return String_invertida(string[1:]) + string[0]
def Main(): 
    string = input(str("Escreva : "))
    print ("String original : ",end="") 
    print (string) 
    print ("String invertida : ",end="") 
    print (String_invertida(string))
Main()