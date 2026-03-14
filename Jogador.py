class Jogador:
    def __init__(self, simbolo):
        self.simbolo = simbolo

escolha = str(input("Você deseja ser O ou X ? : "))
if escolha == "O":
    jogador1 = Jogador("O") #Objetos
    jogador2 = Jogador("X")
elif escolha == "X":
    jogador1 = Jogador("X")
    jogador2 = Jogador("O")
else:
    print("Digite uma opção válida")

#______________________________________________________________________________
