import numpy as np

print("FREQUENCIA")

n = int(input("Numero de linhas: "))
m = int(input("Numero de colunas: "))

mat = np.arange(n*m).reshape(n,m)

col = np.array(['a']*m)

for i in range(m):
	print("Coluna ", i+1)
	col[i] = input()

p = input("Deseja preencher por linha ou coluna?")

if (p=="l") or (p=="linha"):
	for i in range(n):
		print("Linha ", i+1)
		for j in range(m):
			print(col[j])
			mat[i][j] = input()

elif (p=="c") or (p=="coluna"):
	for j in range(m):
		print(col[j])
		for i in range(n):
			print("Linha ", i+1)
			mat[i][j] = input()
else:
	print("Entrada invalida")

for i in range(m):
	print(col[i], end='	')
print()

for i in range(n):
	for j in range(m):
		print(mat[i][j], end='	   ')
	print()
