numero_secreto = 42
tentativas = 3
rodada = 1


while(rodada <= tentativas):
  print("Tentativa {} de {} ".format(rodada, tentativas))
  chute_str = input("Digite o seu numero: ")
  print("Voce digitou  o numero: ", chute_str)
  chute = int(chute_str)

  acertou = numero_secreto == chute
  maior   = chute > numero_secreto
  menor   = chute < numero_secreto


  if (acertou):
      print("Voce acertou!")
      break
  else:
    if(maior):
      print("Voce errou! O seu chute foi maior que o numero secreto")
    elif(menor):
      print("Voce errou! O seu chute foi menor que o numero secreto")
  rodada = rodada + 1

print("Fim de jogo")

