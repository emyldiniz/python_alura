numero_secreto = 42
tentativas = 3

for rodada in range(1, tentativas + 1):
    print("Tentativa {} de {} ".format(rodada, tentativas))
    chute_str = input("Digite o seu numero: ")
    print("Voce digitou  o numero: ", chute_str)
    chute = int(chute_str)

    if (chute < 1 or chute > 100):
      print("Você deve digitar um número entre 1 e 100!")
      continue # executa a proxima instrução

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Voce acertou!")
        break # se verdadeira, executa somente essa instrução
    else:
        if (maior):
            print("Voce errou! O seu chute foi maior que o numero secreto")
        elif (menor):
            print("Voce errou! O seu chute foi menor que o numero secreto")

print("Fim de jogo")
