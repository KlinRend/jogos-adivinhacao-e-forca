import random

def jogar():
    print("***********************************************")
    print("Bem-vindo ao meu primeiro jogo de Adivinhação!")
    print("***********************************************")

    numero_secreto = random.randint(1, 100)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("Digite (1) para Fácil; (2) para Médio; e (3) para Difícil.")

    nivel = int(input("Escola o seu nível de dificuldade: "))

    if (nivel == 1):
        total_de_tentativas = 25
    elif (nivel == 2):
        total_de_tentativas = 12
    else:
        total_de_tentativas = 5

    # utilizar .format para interpolar strings
    for rodada in range (1, total_de_tentativas + 1):
        print(f"\nTentativa {rodada} de {total_de_tentativas}")
        print(f"O número secreto é {numero_secreto}")
        chute = int(input("\nDigite o seu número: "))

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print("\nVocê acertou!")
            break
        else:
            if maior:
                print("Você errou! O seu chute foi maior que o número secreto.")
            elif menor:
                print("Você errou! O seu chute foi menor que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos

    print(f"Fim de jogo! O número secreto é {numero_secreto} e sua pontuação final é {pontos}!")

if(__name__ == "__main__"):
    jogar()