# Algoritmo: VALIDAÇÃO DE CPF.
# Entrada: CPF com 11 dígitos
# Saída: CPF Válido ou CPF Não Válido

print("Algoritmo de validação de CPF \n")
cpf = list(input("Insira o seu CPF(apenas digitos): "))

caracteres_invalidos = ['-', '.']
cpf = [caractere for caractere in cpf if caractere not in caracteres_invalidos]

# verificacao 0:
verificacao_0 = len(cpf) == 11 and cpf.count(cpf[0]) != 11
s1 = 0

for i in range(9):
  s1 += (10 - i) * int(cpf[i])

resto_1 = s1 % 11
verificacao_1 = False

# verificacao 1:
if resto_1 < 2:
  verificacao_1 = int(cpf[-2]) == 0

if resto_1 >= 2:
  verificacao_1 = int(cpf[-2]) == (11-resto_1)

s2 = 0
for j in range(10):
  s2 += (11-j) * int(cpf[j])

resto_2 = s2 % 11

# Verificacao 2:
if resto_2 < 2:
  verificacao_2 = int(cpf[-1]) == 0

if resto_2 >= 2:
  verificacao_2 = int(cpf[-1]) == (11-resto_2)

print("_" * 40)
if (verificacao_0 and verificacao_1 and verificacao_2) == True:
  print("CPF Válido")
else: 
  print("CPF Inválido")
print("_" * 40)

# -------------------------------------------------------------------------                      

#     Com as seguintes restrições:
#        -  cpfs com os 11 dígitos iguais são invalidos (-10)
#        -  os 9 primeiros dígitos podem ser qualquer número de 0 a 9
#        -  Os 2 últimos dígitos são calculados com base nos 9 anteriores

#     Considerando os 9 primeiros dígitos e usando o princípio multiplicativo, 
#     teremos 10**9 = 1,000,000,000 combinações possíveis
#       - para cada uma dessas combinações, o algoritmo calcula os dois ultimos números
#         (somente 1 CPF completo é gerado para cada sequência dessa inicial válida na verificacao_1)
#       - por outro lado, temos 10 CPFs que não estão incluídos nessa conta que são os com 11
#         dígitos iguais
# ===========================================================
# Portanto, com as restrições desse algoritmo, são possíveis
#     total - restricoes
#     1,000,000,000 - 10
#   ->  999,999,990 combinações de CPF diferentes
# ===========================================================
# -------------------------------------------------------------------------                      