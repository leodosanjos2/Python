#função recursiva
def fibonacci(valor):

    if valor == 0:
        return 0
    elif valor == 1:
        return 1
    else:
        return fibonacci(valor - 1)+fibonacci(valor - 2)

valor = int(input("Informe um valor maior ou igual a zero: "))
#verificação de parametros para entrar na função
if valor < 0:
    print("Favor informar um número maior ou igual a zero")
else: 
    for i in range (valor):
        #chama a função e apresenta o resultado
        print("f("+str(fibonacci(i))+"); ", end = "")
#end = "" serve para que o interpretador entenda que
#no final do print sera deixado em branco retirando o \n de quebra de linha