import numpy as np
import os

os.system('cls' if os.name =='nt' else 'clear')

print("FREQUENCIA")

# criando tabela de dados

n = int(input("Numero de linhas: "))
m = int(input("Numero de colunas: "))

mat = np.arange(n*m).reshape(n,m)

# nomes das colunas

col = np.array(['aaaaaaaaaa']*m)


for i in range(m):
	print("Coluna ", i+1)
	col[i] = input()

# preenchendo a tabela de dados

while(1):
	p = input("Deseja preencher por linha ou coluna?")
	if (p=="l") or (p=="linha"):
		for i in range(n):
			print("Linha ", i+1)
			for j in range(m):
				print(col[j])
				mat[i][j] = input()
		break

	elif (p=="c") or (p=="coluna"):
		for j in range(m):
			print(col[j])
			for i in range(n):
				print("Linha ", i+1)
				mat[i][j] = input()
		break
	else:
		print("Entrada invalida")

# TABELA DE FRENQUENCIAS

# ni
print('Qual o intervalo de linhas para calcular ni? De 1 à ', n)
ni_intervalo = int(input())
ni_param = int(input("Qual coluna?")) # criar for para citar as colunas com seus nomes









# printa os nomes das colunas

for i in range(m):
	print(col[i], end='	')
print()

# printa a tabela de dados

for i in range(n):
	for j in range(m):
		print(mat[i][j], end='       ')
	print()