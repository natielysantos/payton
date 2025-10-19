# 5.2-Funções_Customizadas_Lambda-Exercícios.py

# 1. Função fatorial
def fatorial(n):
    """Retorna o fatorial de n."""
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# Programa principal - Fatorial
numero = 5  # exemplo de teste
print(f"Fatorial de {numero} é {fatorial(numero)}")


# 2. Função soma_quadrados
def soma_quadrados(lista):
    """Retorna a soma dos quadrados dos elementos de uma lista."""
    return sum(x**2 for x in lista)

# Programa principal - Soma dos quadrados
valores = [1, 2, 3, 4]
print(f"Soma dos quadrados de {valores} é {soma_quadrados(valores)}")


# 3. Função soma_digitos
def soma_digitos(n):
    """Retorna a soma dos dígitos de um número inteiro."""
    return sum(int(digito) for digito in str(abs(n)))

# Programa principal - Soma dos dígitos
numero2 = 12345
print(f"Soma dos dígitos de {numero2} é {soma_digitos(numero2)}")
