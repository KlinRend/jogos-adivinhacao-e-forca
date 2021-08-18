import forca
import adivinhacao

def escolhe_jogo():
    print("*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x")
    print("-------------ESCOLHA O SEU JOGO---------------")
    print("*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x")

    print("\n(1) Forca; (2) Adivinhação")

    jogo = int(input("Escolha o seu jogo: "))

    if (jogo == 1):
        print("\nJogando Forca")
        forca.jogar()
    elif (jogo == 2):
        print("\nJogando Adivinhação")
        adivinhacao.jogar()
    else:
        print("Você deve digitar um número válido!")

if(__name__ == "__main__"):
    escolhe_jogo()