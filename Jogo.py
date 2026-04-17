import random
import Jogador
import Tabuleiro

#Chama o tabuleiro
Tabuleiro.mostrar_tabuleiro()

#Define que o jogador atual é o jogador 1
jogador_atual = Jogador.jogador1

#Loop para jogar
while True:
    print(f"Jogador {jogador_atual.simbolo}")
    linha = int(input("Linha (0-2): "))
    coluna = int(input("Coluna (0-2): "))

    if Tabuleiro.jogar(linha,coluna,jogador_atual.simbolo):
        Tabuleiro.mostrar_tabuleiro()

        #Verifica a Vitória
        if Tabuleiro.verificar_vitoria(jogador_atual.simbolo):
            print(f"Jogador {jogador_atual.simbolo} venceu !")
            break

        #Verifica Empate
        if Tabuleiro.verificar_empate():
            print("Empate!")
            break

        #Alterna entre jogadores
        if jogador_atual == Jogador.jogador1:
            jogador_atual = Jogador.jogador2
        else:
            jogador_atual = Jogador.jogador1
