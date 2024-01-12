# Este desafio consiste em criar uma função que recebe uma lista de números inteiros e retorna a soma dos números pares multiplicada
# pelo maior número ímpar da lista.


def soma_multiplica(lista):
    soma = 0
    maior_impar = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
        else:
            if i > maior_impar:
                maior_impar = i
    return soma * maior_impar


print(soma_multiplica([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
