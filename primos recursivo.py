#função recursiva
def verificar(numeroTeste, parametro=None):
    if parametro is None:
        parametro = numeroTeste-1

    if numeroTeste <= 1:
        return False
    elif parametro == 1:
        return True
    elif numeroTeste % parametro == 0:
        return False
    else:
        return verificar(numeroTeste, parametro-1)


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