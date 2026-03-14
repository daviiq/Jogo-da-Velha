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