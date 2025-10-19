import random

# ========================
# Questão 1
# ========================
print("=== Questão 1 ===")
lista = [random.randint(-100, 100) for _ in range(20)]
lista_ordenada = sorted(lista)
indice_maior = lista.index(max(lista))
indice_menor = lista.index(min(lista))

print("Lista ordenada:", lista_ordenada)
print("Lista original:", lista)
print("Índice do maior valor:", indice_maior)
print("Índice do menor valor:", indice_menor)


# ========================
# Questão 2
# ========================
print("\n=== Questão 2 ===")
num_elementos = random.randint(5, 20)
elementos = [random.randint(1, 10) for _ in range(num_elementos)]
soma_valores = sum(elementos)
media_valores = soma_valores / len(elementos)

print(f"Número de elementos: {num_elementos}")
print("Lista de elementos:", elementos)
print("Soma dos valores:", soma_valores)
print("Média dos valores:", round(media_valores, 2))


# ========================
# Questão 3
# ========================
print("\n=== Questão 3 ===")
lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]
interseccao = sorted(list(set(lista1) & set(lista2)))

print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Interseção:", interseccao)

for valor in interseccao:
    count1 = lista1.count(valor)
    count2 = lista2.count(valor)
    print(f"{valor}: (lista1={count1}, lista2={count2})")


# ========================
# Questão 4
# ========================
print("\n=== Questão 4 ===")
n1 = int(input("Digite a quantidade de elementos da lista 1: "))
lista1_user = [int(input(f"Digite o {i+1}º elemento da lista 1: ")) for i in range(n1)]

n2 = int(input("Digite a quantidade de elementos da lista 2: "))
lista2_user = [int(input(f"Digite o {i+1}º elemento da lista 2: ")) for i in range(n2)]

# Intercalar elementos
lista_intercalada = []
i = 0
while i < n1 or i < n2:
    if i < n1:
        lista_intercalada.append(lista1_user[i])
    if i < n2:
        lista_intercalada.append(lista2_user[i])
    i += 1

print("Lista intercalada:", lista_intercalada)
