# Aula 6.4 - Compreensão de Listas

# Questão 1
# a) Todos os números pares entre 20 e 50
pares_20_50 = [x for x in range(20, 51) if x % 2 == 0]
print("Pares entre 20 e 50:", pares_20_50)

# b) Quadrados dos valores da lista [1,2,3,4,5,6,7,8,9]
quadrados = [x**2 for x in [1,2,3,4,5,6,7,8,9]]
print("Quadrados:", quadrados)

# c) Números entre 1 e 100 divisíveis por 7
div_7 = [x for x in range(1, 101) if x % 7 == 0]
print("Divisíveis por 7:", div_7)

# d) 'par' ou 'ímpar' para números de 0 a 30 (passo 3)
paridade = ["par" if x % 2 == 0 else "ímpar" for x in range(0, 30, 3)]
print("Paridade:", paridade)


# Questão 2
frase = input("Digite uma frase: ")
vogais = sorted([letra for letra in frase if letra.lower() in "aeiou"])
consoantes = [letra for letra in frase if letra.isalpha() and letra.lower() not in "aeiou"]
print("Vogais:", vogais)
print("Consoantes:", consoantes)


# Questão 3
horas_trabalhadas = [40, 37, 45, 40, 40, 48]
ganho_por_hora = 20
hora_extra = 25
pagamentos = [ganho_por_hora * min(h, 40) + hora_extra * max(0, h - 40) for h in horas_trabalhadas]
print("Pagamentos:", pagamentos)


# Questão 4
alunos = ["Maria", "Jose", "Carla", "Sol"]
notas = [35, 50, 20, 80]
aprovados = [alunos[i] for i in range(len(notas)) if notas[i] >= 60]
print("Aprovados:", aprovados)
