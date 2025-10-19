import random

# ========================
# Questão 1
# ========================
print("=== Questão 1 ===")
# Ler quantidade indefinida de números inteiros (mínimo de 4)
lista = []
print("Digite números inteiros (digite 'fim' para encerrar, mínimo 4 valores):")
while True:
    valor = input()
    if valor.lower() == "fim" and len(lista) >= 4:
        break
    elif valor.lower() == "fim":
        print("Digite pelo menos 4 valores!")
    else:
        try:
            lista.append(int(valor))
        except ValueError:
            print("Entrada inválida. Digite um número inteiro ou 'fim'.")

print("Lista original:", lista)
print("3 primeiros elementos:", lista[:3])
print("2 últimos elementos:", lista[-2:])
print("Lista invertida:", lista[::-1])
print("Elementos de índice par:", lista[0::2])
print("Elementos de índice ímpar:", lista[1::2])


# ========================
# Questão 2
# ========================
print("\n=== Questão 2 ===")
urls = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]
dominios = [url[4:-4] for url in urls]  # remove "www." e ".com"
print("URLs:", urls)
print("Domínios:", dominios)


# ========================
# Questão 3
# ========================
print("\n=== Questão 3 ===")
# Criar lista com 20 elementos entre -10 e 10
lista_random = [random.randint(-10, 10) for _ in range(20)]
print("Original:", lista_random)

# Dividir a lista em duas metades e contar negativos
metade = len(lista_random) // 2
parte1 = lista_random[:metade]
parte2 = lista_random[metade:]

negativos1 = sum(1 for x in parte1 if x < 0)
negativos2 = sum(1 for x in parte2 if x < 0)

# Determinar qual metade remover
if negativos1 >= negativos2:
    del lista_random[:metade]
else:
    del lista_random[metade:]

print("Editada:", lista_random)
