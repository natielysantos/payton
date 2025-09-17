def questao1():
    # Q1 - Soma par ou ímpar
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    soma = num1 + num2

    if soma % 2 == 0:
        print(f"A soma {soma} é Par.")
    else:
        print(f"A soma {soma} é Ímpar.")


def questao2():
    # Q2 - Sistema de classificação de filmes
    avaliacao = int(input("Digite a avaliação do filme (1 a 5): "))

    if avaliacao == 5:
        print("Excelente!")
    elif avaliacao == 4:
        print("Muito Bom!")
    elif avaliacao == 3:
        print("Bom!")
    elif avaliacao == 2:
        print("Regular.")
    elif avaliacao == 1:
        print("Ruim.")
    else:
        print("Avaliação inválida! Digite um número de 1 a 5.")


def questao3():
    # Q3 - Verificação de ano bissexto
    ano = int(input("Digite um ano: "))

    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print("Bissexto")
    else:
        print("Não Bissexto")


def questao4():
    # Q4 - Sistema de cálculo de frete
    distancia = float(input("Digite a distância da entrega (km): "))
    peso = float(input("Digite o peso do pacote (kg): "))

    # Calcula valor base do frete por faixa de distância
    if distancia <= 100:
        preco = peso * 1.0
    elif distancia <= 300:
        preco = peso * 1.5
    else:
        preco = peso * 2.0

    # Taxa extra para pacotes com peso > 10kg
    if peso > 10:
        preco += 10

    print(f"O valor do frete é R${preco:.2f}")


# -------------------------------
# Programa Principal com Menu
# -------------------------------
while True:
    print("\n===== MENU DE QUESTÕES =====")
    print("1 - Soma Par ou Ímpar")
    print("2 - Classificação de filmes")
    print("3 - Verificação de ano bissexto")
    print("4 - Cálculo de frete expresso")
    print("0 - Sair")
    print("============================")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        questao1()
    elif opcao == "2":
        questao2()
    elif opcao == "3":
        questao3()
    elif opcao == "4":
        questao4()
    elif opcao == "0":
        print("Saindo do programa... Até logo!")
        break
    else:
        print("Opção inválida! Tente novamente.")
