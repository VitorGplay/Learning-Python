import random

def generate_lock():
    lock = [[0 for _ in range(3)] for _ in range(3)]
    numbers = list(range(1, 10))
    random.shuffle(numbers)
    for i in range(3):
        for j in range(3):
            lock[i][j] = numbers.pop()
    return lock

def print_lock(lock):
    print("Tranca:")
    for row in lock:
        print(" | ".join(map(str, row)))
        print("-" * 9)

def check_solution_lock(lock, solution):
    for i in range(3):
        for j in range(3):
            if lock[i][j] != solution[i][j]:
                return False
    return True

def main():




    #Mostrar o titulo do jogo
    print("O Mistério da Ilha Perdida!")
    #Explicar como o jogo funcionará
    print("É um jogo simples em python, feito apenas para melhorar minha programação. ")
    print("Trata-se de um jogo em texto, onde você deverá resolver puzzles para progredir. Haverá combate,sistema de HP e puzzles de matemática básica. ")


    #Fazer um sistema para fechar o programa
    while True:
        continuar = input("Digite 'continuar' pra progredir: ").lower()
        if continuar == 'continuar':
            break
    print("------------------------------------------------------------------------------------")
    #O MC acorda em uma biblioteca e econtra-a vazia.
    print("Você acorda em meio a uma biblioteca escura a meia noite. Parece que você está sozinho.")
    input("Pressione qualquer tecla para andar.")
    print("Você anda pela biblioteca à procura de alguém.")
    input("Procurar?")
    #Ele procura por alguém e econtra um livro
    print("Você procurou, ")
    input("Procurar?")
    print("procurou, ")
    input("Procurar?")
    print("procurou, ")
    print("Continuar?")
    print("procurou e não achou ninguém!")
    input("Desistir de procurar e ir embora?")
    print("Após desistir de procurar, você tenta sair da biblioteca quando se depara com um objeto retangular brilhante.")
    input("Observar o objeto?")
    print("Você observa com cautela.")
    input("Olhar de perto: ")
    print("UM LIVRO!")
    input("Andar até ele?")
    print("Encantado pelo brilho, você vai em sua direção.")
    input("Abrir o livro?")
    print("Abre o estranho livro. Com uma escrita que você desconhece.")
    print("Mas, algo chama sua atenção.")
    input("Olhar ao chão: ")
    print("Um pedaço de papel dobrado cai do livro. Nele há alguns padrões, linhas retas, curvas.")
    input("Observar com mais atenção:")
    #Neste livro ele vê um mapa suspeito
    print("É UM MAPA!")
    input("Manuseiar o mapa a procura de detalhes?")
    print("Você pega o mapa, gira ele, olha a frente e o fundo a procura de repostas.")
    input("continuar")
    #O mapa mosra uma ilha desconhecida no oceano
    print("Enquanto manuseia o mapa, você obeserva que as linhas onduladas representam as ondas do mar.")
    input("continuar")
    print("As linhas restas, representam estradas.")
    input("continuar")
    print("Os padrões, você não consegue identificar, mas observa que há um 'X' em algum ponto do oceano.")
    input("continuar")
    print("Você então, entende que o mapa é um mapa do tesouro!")
    print("Você tem a ideia de olhar um mapa das navegações para descobrir onde esse mapa do tesouro leva.")
    input("Procurar na biblioteca um mapa do século XV:")
    print("Você procura, e econtra um mapa antigo.")
    input("continuar")
    print("É um mapa das navegações portuguesas.")
    print("Nele você vê padrões, e linhas familiares.")
    print("Os mesmos padrões do mapa do tesouro.")
    print("O tesouro está em algum lugar do oceano entre o brasil e portugal!")
    print("Sabendo disso, você se decide: ")
    input("Sair em busca do tesouro!")
    input("Desistir e ir pra casa!")
    print("Você então decide sair em uma aventura, em busca do tesouro perdido!")
    input("continuar")

    # Solução para a fechadura

    lock_solution = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    #O MC tenta sair da bibliteca mas na porta há um tipo de tranca com segredo. Ele tem de decifrar o segredo.
    print("Você vai em direção a porta de saída.")
    input("Abrir a porta?")
    print("Você tenta abrir, mas, ela nem se mexe.")
    input("Tentar novamente")
    print("Não adianta!")
    input("Tentar novamente")
    print("Enquanto tenta, você obseva uma tranca diferente. Com uma série de números.")
    input("Olhar mais de perto")
    print("É uma tranca com um segredo.")
    input("Tentar aleatoriamente.")
    print("Não funciona!")
    print("Você tenta resolver usando a lógica.")
    input("continuar")
    print("É uma fechadura com segredo de 3x3")
    print("Você precisa resolver isso usando matemática")
    # Gerar o quebra-cabeça da fechadura
    lock_solution = generate_lock()

    # Mostrar o quebra-cabeça da fechadura
    input("Solucinoar")
    print("Depois de muito tempo tentando, você percebe que não é bom em matemática.")
    input("continuar")
    print("Você então vasculha a biblioteca em busca da resposta pro segredo.")
    input("continuar")
    print("Depois de muito tempo procurando, encontra um papel em baixo do tapete")
    input("Nele está escrito:")
    print_lock(lock_solution)

    # Pedir ao jogador para inserir os números na fechadura
    print("Digite os números de 1 a 9 na fechadura para abrir a porta.")
    input("Pressione qualquer tecla para continuar.")

    while True:
        try:
            solution = []
            for i in range(3):
                row = list(
                    map(int, input("Digite os 3 números para a linha {} separados por espaço: ".format(i + 1)).split()))
                solution.append(row)
            if check_solution_lock(lock_solution, solution):
                print("Parabéns! Você abriu a porta.")
                break
            else:
                print("A combinação está incorreta. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Tente novamente.")

#O MC tenta seguir o caminho para econtrar tesouros.

#Mas ele não consegue decifrar o mapa
#Sistema de puzzle simples, usando matemática básica.
#O MC desvenda o puzzle, e consegue progredir até a ilha.

if __name__ == "__main__":
    main()