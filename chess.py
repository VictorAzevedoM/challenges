# Crie um programa em Python para implementar um jogo de xadrez simples em modo texto para dois jogadores.
# O programa deve permitir que os jogadores façam movimentos válidos de peças (pode começar apenas com peões e permitir movimentos simples).
# O jogo deve exibir o tabuleiro após cada movimento e determinar o vencedor ou empate quando aplicável.

# Importando bibliotecas
import os
import sys
import time
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Definindo variáveis globais
global tabuleiro
global tabuleiro_inicial
global tabuleiro_final
global tabuleiro_anterior

# Definindo funções


# Função para limpar a tela
def clear():
    os.system("cls" if os.name == "nt" else "clear")


# Função para imprimir o tabuleiro
def print_tabuleiro(tabuleiro):
    print("    A   B   C   D   E   F   G   H")
    print("  +---+---+---+---+---+---+---+---+")
    for i in range(0, 8):
        print(i + 1, end=" ")
        for j in range(0, 8):
            print("|", tabuleiro[i][j], end=" ")
        print("|", i + 1)
        print("  +---+---+---+---+---+---+---+---+")
    print("    A   B   C   D   E   F   G   H")


# Função para verificar se o movimento é válido


def movimento_valido(tabuleiro, linha, coluna, linha_destino, coluna_destino, jogador):
    # Verifica se a peça é do jogador
    if jogador == 1:
        if tabuleiro[linha][coluna] not in ["P", "T", "C", "B", "R", "D"]:
            return False
    elif jogador == 2:
        if tabuleiro[linha][coluna] not in ["p", "t", "c", "b", "r", "d"]:
            return False
    # Verifica se a peça é do adversário
    if jogador == 1:
        if tabuleiro[linha_destino][coluna_destino] in ["P", "T", "C", "B", "R", "D"]:
            return False
    elif jogador == 2:
        if tabuleiro[linha_destino][coluna_destino] in ["p", "t", "c", "b", "r", "d"]:
            return False
    # Verifica se a peça é do jogador
    if jogador == 1:
        if tabuleiro[linha][coluna] == "P":
            if linha_destino == linha - 1 and coluna_destino == coluna:
                return True
            elif linha_destino == linha - 2 and coluna_destino == coluna and linha == 6:
                return True
            elif linha_destino == linha - 1 and coluna_destino == coluna - 1:
                return True
            elif linha_destino == linha - 1 and coluna_destino == coluna + 1:
                return True
            else:
                return False
        elif tabuleiro[linha][coluna] == "T":
            if linha_destino == linha and coluna_destino > coluna:
                for i in range(coluna + 1, coluna_destino):
                    if tabuleiro[linha][i] != " ":
                        return False
                return True
            elif linha_destino == linha and coluna_destino < coluna:
                for i in range(coluna_destino + 1, coluna):
                    if tabuleiro[linha][i] != " ":
                        return False
                return True
            elif coluna_destino == coluna and linha_destino > linha:
                for i in range(linha + 1, linha_destino):
                    if tabuleiro[i][coluna] != " ":
                        return False
                return True
            elif coluna_destino == coluna and linha_destino < linha:
                for i in range(linha_destino + 1, linha):
                    if tabuleiro[i][coluna] != " ":
                        return False
                return True
            else:
                return False
        elif tabuleiro[linha][coluna] == "C":

            def is_valid_move(
                tabuleiro, jogador, linha, coluna, linha_destino, coluna_destino
            ):
                if jogador == 1:
                    if tabuleiro[linha][coluna] == "P":
                        if linha_destino == linha - 1 and coluna_destino == coluna:
                            return True
                        elif (
                            linha_destino == linha - 2
                            and coluna_destino == coluna
                            and linha == 6
                        ):
                            return True
                        elif (
                            abs(linha_destino - linha) == 1
                            and abs(coluna_destino - coluna) == 1
                        ):
                            return True
                        else:
                            return False
                    elif tabuleiro[linha][coluna] == "T":
                        if linha_destino == linha or coluna_destino == coluna:
                            return True
                        else:
                            return False
                    elif tabuleiro[linha][coluna] == "C":
                        if (
                            abs(linha_destino - linha) == 2
                            and abs(coluna_destino - coluna) == 1
                        ):
                            return True
                        elif (
                            abs(linha_destino - linha) == 1
                            and abs(coluna_destino - coluna) == 2
                        ):
                            return True
                        else:
                            return False
                    elif tabuleiro[linha][coluna] == "B":
                        if abs(linha_destino - linha) == abs(coluna_destino - coluna):
                            return True
                        else:
                            return False
                    elif tabuleiro[linha][coluna] == "R":
                        if (
                            abs(linha_destino - linha) <= 1
                            and abs(coluna_destino - coluna) <= 1
                        ):
                            return True
                        else:
                            return False
                    elif tabuleiro[linha][coluna] == "D":
                        if (
                            abs(linha_destino - linha) <= 1
                            and abs(coluna_destino - coluna) <= 1
                        ):
                            return True
                        elif (
                            abs(linha_destino - linha) == 1
                            and abs(coluna_destino - coluna) == 2
                        ):
                            return True
                        elif (
                            abs(linha_destino - linha) == 2
                            and abs(coluna_destino - coluna) == 1
                        ):
                            return True
                        else:
                            return False
                    else:
                        return False
                elif jogador == 2:
                    if tabuleiro[linha][coluna] == "p":
                        if linha_destino == linha + 1 and coluna_destino == coluna:
                            return True
                        elif (
                            linha_destino == linha + 2
                            and coluna_destino == coluna
                            and linha == 1
                        ):
                            return True
                        elif (
                            abs(linha_destino - linha) == 1
                            and abs(coluna_destino - coluna) == 1
                        ):
                            return True
                        else:
                            return False
                    elif tabuleiro[linha][coluna] == "t":
                        if linha_destino == linha or coluna_destino == coluna:
                            return True
                        else:
                            return False
                    elif tabuleiro[linha][coluna] == "c":
                        if (
                            abs(linha_destino - linha) == 2
                            and abs(coluna_destino - coluna) == 1
                        ):
                            return True
                        elif (
                            abs(linha_destino - linha) == 1
                            and abs(coluna_destino - coluna) == 2
                        ):
                            return True
                        else:
                            return False
                    elif tabuleiro[linha][coluna] == "b":
                        if abs(linha_destino - linha) == abs(coluna_destino - coluna):
                            return True
                        else:
                            return False
                    elif tabuleiro[linha][coluna] == "r":
                        if (
                            abs(linha_destino - linha) <= 1
                            and abs(coluna_destino - coluna) <= 1
                        ):
                            return True
                        else:
                            return False
                    elif tabuleiro[linha][coluna] == "d":
                        if (
                            abs(linha_destino - linha) <= 1
                            and abs(coluna_destino - coluna) <= 1
                        ):
                            return True
                        elif (
                            abs(linha_destino - linha) == 1
                            and abs(coluna_destino - coluna) == 2
                        ):
                            return True
                        elif (
                            abs(linha_destino - linha) == 2
                            and abs(coluna_destino - coluna) == 1
                        ):
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False


# Função para pedir a jogada ao jogador
def pedir_jogada(tabuleiro, jogador):
    while True:
        try:
            jogada = input("Jogador " + str(jogador) + ": ")
            if jogada == "sair":
                sys.exit()
            if len(jogada) != 4:
                raise ValueError
            coluna = ord(jogada[0]) - 65
            linha = int(jogada[1]) - 1
            coluna_destino = ord(jogada[2]) - 65
            linha_destino = int(jogada[3]) - 1
            if (
                linha < 0
                or linha > 7
                or coluna < 0
                or coluna > 7
                or linha_destino < 0
                or linha_destino > 7
                or coluna_destino < 0
                or coluna_destino > 7
            ):
                raise ValueError
            if (
                movimento_valido(
                    tabuleiro, linha, coluna, linha_destino, coluna_destino, jogador
                )
                == False
            ):
                raise ValueError
            break
        except ValueError:
            print("Jogada inválida!")
    return linha, coluna, linha_destino, coluna_destino


# Função para verificar se o jogo acabou
def jogo_acabou(tabuleiro):
    if "R" not in tabuleiro:
        print("Jogador 2 venceu!")
        return True
    elif "r" not in tabuleiro:
        print("Jogador 1 venceu!")
        return True
    else:
        return False


# Executando o programa
# Inicializando o tabuleiro
tabuleiro_inicial = [
    ["T", "C", "B", "D", "R", "B", "C", "T"],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    ["t", "c", "b", "d", "r", "b", "c", "t"],
]
tabuleiro = tabuleiro_inicial
tabuleiro_anterior = tabuleiro_inicial
print_tabuleiro(tabuleiro)
# Inicializando variáveis
jogador = 1
# Loop principal
while True:
    # Pedir jogada ao jogador
    linha, coluna, linha_destino, coluna_destino = pedir_jogada(tabuleiro, jogador)
    # Fazer a jogada
    tabuleiro[linha_destino][coluna_destino] = tabuleiro[linha][coluna]
    tabuleiro[linha][coluna] = " "
    # Verificar se o jogo acabou
    if jogo_acabou(tabuleiro):
        break
    # Imprimir o tabuleiro
    print_tabuleiro(tabuleiro)
    # Trocar de jogador
    if jogador == 1:
        jogador = 2
    else:
        jogador = 1
    # Aguardar 1 segundo
    time.sleep(1)
    # Limpar a tela
    clear()
# Imprimir o tabuleiro final

# Fim do programa
