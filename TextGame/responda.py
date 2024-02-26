import random

def reponda():
    #Listade possiveis respostas
    respostas = [
        "Sim.",
        "Não.",
        "Talvez.",
        "Não sei, cara.",
        "Provavelmente sim.",
        "Provavelmente não.",
        "Não posso responder agora."
        ]
    #Loop para continuar repondendo até o usuario estar satisfeito.
    while True:
        #Pergunta ao usuário
        input("Qual é a sua dúvida? ")

        #Escolher uma resposta aleatória da lista
        resposta = random.choice(respostas)

        #Exibir a resposta
        print(resposta)

        # Verificar se o unuario deseja continuar
        while True:
            continuar = input("Resta alguma dúvida? (s/n): ").lower()
            if continuar =='s':
                break
        else:
            print("Por favor, responda apenas com 's' ou 'n'.")

        if continuar == 'n':
            break

if __name__ == "__main__":
    reponda()