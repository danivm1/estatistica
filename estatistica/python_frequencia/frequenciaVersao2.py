import numpy as np
import os

os.system('cls' if os.name =='nt' else 'clear')

print("FREQUENCIA")

# criando tabela de dados

n = int(input("Numero de linhas: "))

col = np.arange(n)

# nomes das colunas

colName = input("Qual o nome da coluna?\n")

# preenchendo a tabela de dados

for i in range(n):
    dado = colName + " " + str(i+1) + ": "
    col[i] = int(input(dado))

# TABELA DE FRENQUENCIAS

# ni (contagem)
while(1):
    print('Qual o intervalo de linhas para calcular ni? De 1 à ', n)
    ni_lim_inf = int(input("Limite inferior: "))
    ni_lim_sup = int(input("Limite superior: "))

    if ni_lim_inf <= ni_lim_sup:
        break

colFreq = verifyValues(col, ni_lim_inf, ni_lim_sup)







# printa o nome da coluna

print(colName)

# printa a tabela de dados

for i in range(n):
	print(col[i])