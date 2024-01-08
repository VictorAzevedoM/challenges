import timeit

#O desafio é criar um programa em Python que converta um número decimal em sua representação binária

#Solução 1
def decimal_to_binary1(decimal):
    binary=""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2  
    return binary

#Solução 2
def decimal_to_binary2(decimal):
  return bin(decimal)[2:]

#Solução 3
def decimal_to_binary3(decimal):
  return format(decimal, 'b')

#Solução 4  
def decimal_to_binary4(decimal):
  return f'{decimal:b}' 

# As funções de conversão binária já definidas

def compare_functions(decimal):
    times = {}

    start_time = timeit.default_timer()
    decimal_to_binary1(decimal)
    times['decimal_to_binary1'] = timeit.default_timer() - start_time

    start_time = timeit.default_timer()
    decimal_to_binary2(decimal)
    times['decimal_to_binary2'] = timeit.default_timer() - start_time

    start_time = timeit.default_timer()
    decimal_to_binary3(decimal)
    times['decimal_to_binary3'] = timeit.default_timer() - start_time

    start_time = timeit.default_timer()
    decimal_to_binary4(decimal)
    times['decimal_to_binary4'] = timeit.default_timer() - start_time

    fastest_function = min(times, key=times.get)
    return fastest_function

fastest = compare_functions(10)
print(f"A função mais rápida é: {fastest}")



compare_functions(10) 
