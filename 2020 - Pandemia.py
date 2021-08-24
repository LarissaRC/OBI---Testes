# 23/08/2021
# Erro na submissão

# N = Total de amigos
# M = Total de dias de reunião
N, M = [int(i) for i in input().split()]

# I = Número do amigo infectado
# R = Dia em que o amigo foi infectado
I, R = [int(i) for i in input().split()]

i = 0
amigos = []
while i < N:
    if i + 1 == I:  # Se for o amigo infectado...
        amigos.append(-1)
    else:
        amigos.append(i+1)
    i += 1

infoDias = []

i = 0
while i < M:
    sessao = []
    sessao = ([int(j) for j in input().split()])

    if i + 1 >= R:  # A partir do dia da infecção...
        j = 1
        while j <= sessao[0]:
            amigo = sessao[j]
            if amigo not in amigos:  # Se o amigo for infectado (-1)
                k = 1
                while k < sessao[0]:
                    l = 0
                    while l < len(amigos):
                        if amigos[l] == sessao[k]:
                            amigos[l] = -1
                        l += 1
                    k += 1

            j += 1

    i += 1

total = 0
i = 0
while i < len(amigos):
    if amigos[i] == -1:
        total += 1
    i += 1

print(total)