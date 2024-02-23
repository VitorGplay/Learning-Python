import random
def simular_dado(minimo, maximo):
    return random.randint(minimo, maximo)
def main():
    minimo = 1
    maximo = 6
    continuar = True
    while continuar:
        input("Pressione Enter para lançar o dado...")
        resultado = simular_dado(minimo, maximo)
        print("O dado mostra:", resultado)

        escolha = input("Deseja lançar o dado novamente? (s/n)").lower()
        if escolha !='s':
            continuar = False
if __name__== "__main__":
    main()