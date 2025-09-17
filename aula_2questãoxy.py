def questao1():
    # Q1 - Juliana e Cris só entram se ambas forem maiores de idade (>17)
    idade_juliana = int(input("Digite a idade de Juliana: "))
    idade_cris = int(input("Digite a idade de Cris: "))

    podem_entrar = idade_juliana > 17 and idade_cris > 17
    print(podem_entrar)


def questao2():
    # Q2 - Pelo menos uma maior de idade pode entrar
    idade_juliana = int(input("Digite a idade de Juliana: "))
    idade_cris = int(input("Digite a idade de Cris: "))

    podem_entrar = idade_juliana > 17 or idade_cris > 17
    print(podem_entrar)


def questao3():
    # Q3 - Clube de jogos de tabuleiro
    idade = int(input("Digite sua idade: "))
    jogou3 = input("Já jogou pelo menos 3 jogos de tabuleiro? (True/False): ")
    jogou3 = jogou3 == "True"  # transforma a entrada em booleano
    vitorias = int(input("Quantos jogos já venceu? "))

    apto = (16 <= idade <= 18) and jogou3 and (vitorias >= 1)
    print("Apto para ingressar no clube de jogos de tabuleiro:", apto)


def questao4():
    # Q4 - Validação da ficha de RPG
    classe = input("Escolha a classe (guerreiro, mago ou arqueiro): ").lower()
    forca = int(input("Digite os pontos de força (de 1 a 20): "))
    magia = int(input("Digite os pontos de magia (de 1 a 20): "))

    if classe == "guerreiro":
        valido = forca >= 15 and magia <= 10
    elif classe == "mago":
        valido = forca <= 10 and magia >= 15
    elif classe == "arqueiro":
        valido = (forca > 5 and magia > 5) and (forca <= 15 and magia <= 15)
    else:
        valido = False

    print("Pontos de atributo consistentes com a classe escolhida:", valido)


def questao5():
    # Q5 - Verificação de aposentadoria
    genero = input("Digite seu gênero (M/F): ").upper()
    idade = int(input("Digite sua idade: "))
    tempo_servico = int(input("Digite seu tempo de serviço (anos): "))

    if (genero == "F" and idade > 60) or (genero == "M" and idade > 65):
        pode_aposentar = True
    elif tempo_servico >= 30:
        pode_aposentar = True
    elif idade >= 60 and tempo_servico >= 25:
        pode_aposentar = True
    else:
        pode_aposentar = False

    print(pode_aposentar)


# -------------------------------
# Programa Principal com Menu
# -------------------------------
while True:
    print("\n===== MENU DE QUESTÕES =====")
    print("1 - Juliana e Cris (ambos maiores de idade)")
    print("2 - Juliana e Cris (pelo menos um maior de idade)")
    print("3 - Clube juvenil de jogos de tabuleiro")
    print("4 - Validação de ficha de RPG")
    print("5 - Verificação de aposentadoria")
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
    elif opcao == "5":
        questao5()
    elif opcao == "0":
        print("Saindo do programa... Até logo!")
        break
    else:
        print("Opção inválida! Tente novamente.")
