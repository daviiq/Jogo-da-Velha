tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

#Cria o método para mostrar o tabuleiro:
def mostrar_tabuleiro():
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

#Cria o método para jogar
def jogar(linha, coluna, simbolo):
    if tabuleiro[linha][coluna] == " ":
        tabuleiro[linha][coluna] = simbolo
        return True
    else:
        print("Posição já ocupada!")
        return False

#Verificar a vitória
def verificar_vitoria(simbolo):
    #verifica as linhas
    for i in range(3):
        if tabuleiro[i][0] == simbolo and tabuleiro[i][1] == simbolo and tabuleiro[i][2] == simbolo:
            return True
        
    #verifica as colunas
    for j in range(3):
        if tabuleiro[0][j] == simbolo and tabuleiro[1][j] == simbolo and tabuleiro [2][j] == simbolo: return True

    #Verificar Diagonal principal
    if tabuleiro[0][0] == simbolo and tabuleiro[1][1] == simbolo and tabuleiro[2][2] == simbolo: return True