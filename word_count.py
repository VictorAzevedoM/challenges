# Crie um programa em Python que leia um arquivo de texto contendo palavras e conte quantas vezes cada palavra aparece no arquivo.
# Depois, exiba as palavras e suas contagens em ordem decrescente de ocorrência.

# Solução:

# Abre o arquivo para leitura
arquivo = open("palavras.txt", "r")


# Cria um dicionário vazio
dicionario = {}

# Percorre o arquivo

for linha in arquivo:
    # Remove os espaços em branco
    linha = linha.strip()
    # Separa as palavras
    palavras = linha.split()
    # Remove os caracteres especiais
    for i in range(len(palavras)):
        palavras[i] = palavras[i].strip(",.;:!?()[]{}")
    # Percorre as palavras
    for palavra in palavras:
        # Verifica se a palavra já está no dicionário
        if palavra in dicionario:
            # Incrementa a contagem
            dicionario[palavra] = dicionario[palavra] + 1
        else:
            # Inclui a palavra no dicionário
            dicionario[palavra] = 1

# Fecha o arquivo
arquivo.close()

# Cria uma lista vazia
lista = []

# Percorre o dicionário
for palavra in dicionario:
    # Inclui a palavra na lista
    lista.append(palavra)

# Ordena a lista
lista.sort()

# Percorre a lista
for palavra in lista:
    # Exibe a palavra e a contagem
    print(palavra, dicionario[palavra])

# Exibe a palavrava mais frequente e quantas vezes ela aparece
print(
    "A palavra mais frequente é", lista[0], "com", dicionario[lista[0]], "ocorrências"
)
