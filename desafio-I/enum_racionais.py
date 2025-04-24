# Algoritmo: Correspondência entre os Naturais e os Racionais Positivos.
# Entrada: n (número natural que indica a posição do n-ésimo número racional)
# Saída: n-ésimo número racional p / q

print("_"*40 + "\n Algoritmo de enumeração de racionais positivos \n" + "_"*40)
posicao_desejada = int(input("Insira a n-ésima posição desejada: "))

def ehPar(numero):
  return numero % 2 == 0

contador = 1 # posição inicial na tabela
p = 1 # posição inicial da linha
q = 1 # posição inicial da coluna

while contador < posicao_desejada:
  if p == 1 and not(ehPar(q)): # se p é 1 e q é impar, mova-se para a direita
    q += 1
    contador += 1
  elif p == 1 and ehPar(q): # se p é 1 e q é par
    while not(q == 1) and contador != posicao_desejada: # enquanto q diferente 1 e contador diferente da posicao desejada, mova-se na diagonal inferior esquerda
      p += 1
      q -= 1
      contador += 1
  elif ehPar(p) and q == 1: # se p é par e q = 1, então mova-se uma linha abaixo
    p += 1
    contador += 1
  elif not(ehPar(p)) and q == 1: # se p é impar e q é 1
    while not(p == 1) and contador != posicao_desejada: # enquanto p é diferente de 1 e q nao e impar ou contador diferente da posicao desejada, mova-se na diagonal superior direita
      p -= 1
      q += 1
      contador += 1

if posicao_desejada == contador: # se posicao desejada é igual a contador
  print("Resultado \n" + "_"*40)
  print(f"{p}/{q}")