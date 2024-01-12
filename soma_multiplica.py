# Este desafio consiste em criar uma função que recebe uma lista de números inteiros e retorna a soma dos números pares multiplicada
# pelo maior número ímpar da lista.


def soma_multiplica(lista):
    numeros_pares = [num for num in lista if num % 2 == 0]
    maior_impar = max([num for num in lista if num % 2 != 0], default=0)
    return sum(numeros_pares) * maior_impar


print(soma_multiplica([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
