import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhacao!")
print("*********************************")

numero_secreto = random.randrange(1,101)
tentativas = 0
pontos = 1000

print("Qual nivel de dificulade voce prefere?", numero_secreto)
print("(1)Facil\n(2)Medio\n(3)Dificil")

nivel = int(input("Escolha: "))

if(nivel == 1):
  tentativas = 20
elif (nivel == 2):
  tentativas = 10
else:
  tentativas = 5

for rodada in range(1, tentativas + 1):
  print("Tentativa {} de {} ".format(rodada, tentativas))
  chute_str = input("Digite o seu numero: ")
  print("Voce digitou  o numero: ", chute_str)
  chute = int(chute_str)

  if (chute < 1 or chute > 100):
    print("Voce deve digitar um numero entre 1 e 100!")
    continue

  acertou = numero_secreto == chute
  maior   = chute > numero_secreto
  menor   = chute < numero_secreto

  if (acertou):
      print("Voce acertou e fez {} pontos!".format(pontos))
      break
  else:
    if(maior):
      print("Voce errou! O seu chute foi maior que o numero secreto")
    elif(menor):
      print("Voce errou! O seu chute foi menor que o numero secreto")
    pontos_perdidos = abs(numero_secreto - chute) #abs() função "absoluto" - transforma o número negativo em positivo, desconsidera seu sinal
    pontos = pontos - pontos_perdidos
    if (rodada == tentativas):
        print("O numero secreto era {}. Voce fez {} pontos".format(numero_secreto, pontos))
  

print("Fim de jogo")

