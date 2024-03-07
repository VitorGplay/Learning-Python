#programa que simula uma calculadora
#funções
def adicao():
    a = float(input("Digite um número: "))
    b = float(input("Digite outro número: "))
    c = a + b
    if c.is_integer():
        print("O resultado das soma é:", int(c))
    else:
        print("O resultado das soma é:", c)
def subtracao():
    a = float(input("Digite um número: "))
    b = float(input("Digite outro número: "))
    c = a - b
    print("O resultado da subtração é:", c)
def multiplicacao():
    a = float(input("Digite um número: "))
    b = float(input("Digite outro número: "))
    c = a * b
    print("O resultado da multiplicação é:", c)
def divisao():
    a = float(input("Digite um número: "))
    b = float(input("Digite outro número: "))
    c = a / b
    print("O resultado da divisão é:", c)
def raizquadrada():
    a = float(input("Digite um número: "))
    b = a ** 0.5
    print("O resultado é:","{:.2f}".format(b))
def potenciaquadrada():
    a = float(input("Digite um número: "))
    b = a ** 2
    print(b)
#Função para escolher funções
def escolherfuncao():
    print("Escolha a operação: ")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicão")
    print("4. Divisão")
    print("5. Raiz quadrada")
    print("6. Potência")
    escolha = int(input("Digite o número da operação desejada: "))
    if escolha == 1:
        adicao()
    elif escolha == 2:
        subtracao()
    elif escolha == 3:
        multiplicacao()
    elif escolha == 4:
        divisao()
    elif escolha == 5:
        raizquadrada()
    elif escolha == 6:
        potenciaquadrada()

escolherfuncao()
#Adição
#adicao()
#Subtração
#subtracao()
#Multiplicação
#multiplicacao()
#Divisão
#divisao()
#Raiz quadrada
#raizquadrada()
#Pontência
#potenciaquadrada()
