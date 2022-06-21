
def f(n):
    
    

    contador = 0

    um = 0
    dois = 1
    x = 0
    while contador <= n:
        print(um)
        x = um + dois
        um = dois
        dois = x
        contador = contador + 1

   
num = int(input("nº da seq: "))
f(num)
