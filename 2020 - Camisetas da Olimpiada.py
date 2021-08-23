# 23/08/2021
# Submissão aceita

N = int(input()) # Número de premiados

T = [int(i) for i in input().split()] # Tamanho de cada participante

P = int(input()) # Camisas tamanho P produzidas
M = int(input()) # Camisas tamanho M produzidas

for i in T:
    if i == 1:
        P -= 1
    else:
        M -= 1

if P == 0 and M == 0:
    print("S")
else:
    print("N")