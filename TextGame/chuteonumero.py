import random

def verificar_continuar():
    while True:
        continuar = input("Deseja continuar? ('s' para sim, 'n' para não): ").lower()
        if continuar == 's':
            return True
        elif continuar == 'n':
            return False
        else:
            print("Opção inválida. Por favor, digite 's' para sim ou 'n' para não.")

def main():
    #Instruções para o usuário
    print("Bem-vindo ao jogo Chute o Número!")
    print("Tente adivinhar o número secreto entre 1 e 100.")
    print("Dica: se está perto significa que é um até 5 números acima ou abaixo. Boa sorte!")

    while True:
        #Gerar um número aleatório entre 1 e 100
        numero_secreto = random.randint(1, 100)
        margem_de_erro = 5

        #Loop principal do jogo
        while True:
            #Solicitar ao jogador que faça um chute
            chute = int(input("Digite o seu chute: "))

            #Verificar se o chute está correto
            if chute == numero_secreto:
                print("Parabéns! Você acertou o número secreto", numero_secreto)
                break
            elif abs(chute - numero_secreto) <= margem_de_erro:
                print("Perto! Tente novamente.")
            elif chute < numero_secreto:
                print("Muito baixo! Tente novamente.")
            else:
                print("Muito alto! Tente novamente.")

        # Verificar se o jogador deseja continuar
        if not verificar_continuar():
            break

if __name__ == "__main__":
    main()
