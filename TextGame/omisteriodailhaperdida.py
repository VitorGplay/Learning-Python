#Importações
import random


#Funções
#Função para gerar a tranca
def generate_lock():
    # Gera uma fechadura aleatória
    lock = [[0 for _ in range(3)] for _ in range(3)]
    numbers = list(range(1, 10))
    random.shuffle(numbers)
    for i in range(3):
        for j in range(3):
            lock[i][j] = numbers.pop()
    return lock
#Funlção para mostrar a tranca
def print_lock(lock):
    # Imprime a fechadura
    print("Fechadura:")
    for row in lock:
        print(" | ".join(map(str, row)))
        print("-" * 9)
#Função para verificar o segredo
def check_solution_lock(lock, solution):
    # Verifica se a solução da fechadura está correta
    for i in range(3):
        for j in range(3):
            if lock[i][j] != solution[i][j]:
                return False
    return True
#Função para obter a entrada do usuario para a tranca
def get_lock_input():
    # Obtém a entrada do usuário para a fechadura
    while True:
        try:
            solution = []
            for i in range(3):
                row = list(map(int, input("Digite os 3 números para a linha {} separados por espaço: ".format(i + 1)).split()))
                if len(row) != 3:
                    raise ValueError("Por favor, digite exatamente 3 números separados por espaço.")
                solution.append(row)
            return solution
        except ValueError as e:
            print(e)
#Função para resovler a tranca
def resolve_tranca():
    # Gerar o quebra-cabeça da fechadura
    lock_solution = generate_lock()

    # Mostrar o quebra-cabeça da fechadura
    input("Solucionar")
    print("Depois de muito tempo tentando, você percebe que não é bom em matemática.")
    input("Continuar")
    print("Você então vasculha a biblioteca em busca da resposta pro segredo.")
    input("Continuar")
    print("Depois de muito tempo procurando, encontra um papel embaixo do tapete")
    input("Nele está escrito:")
    print_lock(lock_solution)

    # Pedir ao jogador para inserir os números na fechadura
    print("Digite os números de 1 a 9 na fechadura para abrir a porta.")
    input("Pressione qualquer tecla para continuar.")

    while True:
        solution = get_lock_input()
        if check_solution_lock(lock_solution, solution):
            print("Parabéns! Você abriu a porta.")
        else:
            print("A combinação está incorreta. Tente novamente.")
#Função para tomar decisao
def tomar_decisao():
    while True:
        decisao = input("Sabendo disso, você decide:\n1. Sair em busca do tesouro!\n2. Desistir e ir para casa!\nEscolha sua opção: ")
        if decisao == '1':
            print("Você então decide sair em uma aventura, em busca do tesouro perdido!")
            print("...")
            input("Continuar")
            opcao1()
            break
        elif decisao == '2':
            print("Você decide pelo mais lógico e racional e vai em direção à saída para casa!")
            print("...")
            input("Continuar")
            opcao2()
            break
        else:
            print("Opção inválida. Por favor, escolha '1' ou '2'.")

#Função decisao tomada
def opcao1():
    print("Você vai em direção à porta de saída.")
    input("Abrir a porta?")
    print("Você tenta abrir, mas ela nem se mexe.")
    input("Tentar novamente")
    print("Não adianta!")
    input("Tentar novamente")
    print("Enquanto tenta, você observa uma tranca diferente. Com uma série de números.")
    input("Olhar mais de perto")
    print("É uma tranca com um segredo.")
    input("Tentar aleatoriamente.")
    print("Não funciona!")
    print("Você tenta resolver usando a lógica.")
    input("Continuar")
    print("É uma fechadura com segredo de 3x3")
    print("Você precisa resolver isso usando matemática")
    resolve_tranca()
def opcao2():
    print("Você vai em direção à porta de saída.")
    input("Abrir a porta?")
    print("Você tenta abrir, mas ela nem se mexe.")
    input("Tentar novamente")
    print("Não adianta!")
    input("Tentar novamente")
    print("Enquanto tenta, você observa uma tranca diferente. Com uma série de números.")
    input("Olhar mais de perto")
    print("É uma tranca com um segredo.")
    input("Tentar aleatoriamente.")
    print("Não funciona!")
    print("Você tenta resolver usando a lógica.")
    input("Continuar")
    print("É uma fechadura com segredo de 3x3")
    print("Você precisa resolver isso usando matemática")
    resolve_tranca()
def main():
    print("O Mistério da Ilha Perdida!")
    print("Este é um jogo simples em Python, feito apenas para melhorar minha programação.")
    print("Trata-se de um jogo em texto, onde você deverá resolver quebra-cabeças para progredir. Haverá combate, sistema de HP e puzzles de matemática básica.")

    while True:
        continuar = input("Digite 'continuar' para progredir: ").lower()
        if continuar == 'continuar':
            break
    print("------------------------------------------------------------------------------------")
    print("Você acorda em meio a uma biblioteca escura à meia-noite. Parece que você está sozinho.")
    input("Pressione qualquer tecla para andar.")
    print("Você anda pela biblioteca à procura de alguém.")
    input("Procurar?")

    print("Você procurou,")
    input("Procurar?")
    print("procurou,")
    input("Procurar?")
    print("procurou,")
    print("Continuar?")
    print("procurou e não achou ninguém!")
    input("Desistir de procurar e ir embora?")
    print("Após desistir de procurar, você tenta sair da biblioteca quando se depara com um objeto retangular brilhante.")
    input("Observar o objeto?")
    print("Você observa com cautela.")
    input("Olhar de perto:")
    print("UM LIVRO!")
    input("Andar até ele?")
    print("Encantado pelo brilho, você vai em sua direção.")
    input("Abrir o livro?")
    print("Abre o estranho livro. Com uma escrita que você desconhece.")
    print("Mas, algo chama sua atenção.")
    input("Olhar ao chão:")
    print("Um pedaço de papel dobrado cai do livro. Nele há alguns padrões, linhas retas, curvas.")
    input("Observar com mais atenção:")

    print("É UM MAPA!")
    input("Manusear o mapa à procura de detalhes?")
    print("Você pega o mapa, gira ele, olha a frente e o fundo à procura de respostas.")
    input("Continuar")

    print("Enquanto manuseia o mapa, você observa que as linhas onduladas representam as ondas do mar.")
    input("Continuar")
    print("As linhas retas representam estradas.")
    input("Continuar")
    print("Os padrões, você não consegue identificar, mas observa que há um 'X' em algum ponto do oceano.")
    input("Continuar")
    print("Você então entende que o mapa é um mapa do tesouro!")
    print("Você tem a ideia de olhar um mapa das navegações para descobrir onde esse mapa do tesouro leva.")
    input("Procurar na biblioteca um mapa do século XV:")
    print("Você procura e encontra um mapa antigo.")
    input("Continuar")
    print("É um mapa das navegações portuguesas.")
    print("Nele você vê padrões e linhas familiares.")
    print("Os mesmos padrões do mapa do tesouro.")
    print("O tesouro está em algum lugar do oceano entre o Brasil e Portugal!")
    tomar_decisao()


    print("Depois de resolver o segredo, você sai da biblioteca...")
    print("Pensativo...")
    input("...")
    print("Você vai para sua casa!")
    input("Fim!")

if __name__ == "__main__":
    main()
# O MC tenta seguir o caminho para encontrar tesouros.
# Mas ele não consegue decifrar o mapa
# Sistema de puzzle simples, usando matemática básica.
# O MC desvenda o puzzle e consegue progredir até a ilha.