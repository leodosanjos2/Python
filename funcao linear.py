#função linear
def fibonacci(valor: int) -> int:
    if valor >= 0:
        while len(fib) < valor:
            proxVal = fib[-1] + fib[-2]
            fib.append(proxVal)
    else: 
        return print("Favor informar um número maior ou igual a zero")
    return fib

valor = int(input("Informe um valor maior ou igual a zero: "))
fib = [0, 1]

#chama a função para resolução
fibonacci(valor)

#laço de repetição para mostrar o valor e chamar a função
for i in range (valor):
    print("fib("+str(fib[i])+"); ", end = "")
#end = "" serve para que o interpretador entenda que
#no final do print sera deixado em branco retirando o \n de quebra de linha