#função linear
def verificar(numero):
    # Caso especial para números menores que 2
    if numero < 2:
        return False
    #numero**0.5 serve para comparar com a raiz quadrada do numero.
    #ex raiz de 9 é 3, significa que a resposta da raiz é um numero diferente de 1, portanto não é primo
    for i in range(2, int(numero**0.5)+1):
        if numero % i == 0:
            return False
    return True

def primo(valorPrimo):
    prim = []
    for i in range(valorPrimo+1):
        #é adicionado na lista somente se for true
        if verificar(i):
            prim.append(i)
    return prim

valor = int(input("Favor informar um valor: "))
if valor >= 2:
    print("p("+str(valor)+") = "+str(primo(valor)))
else:     
    print("Favor informar um valor maior que 1")