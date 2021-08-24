# 23/08/2021
# Erro na submissão

# N = Tamanho da Matriz
# F = Força da Erupção
N, F = [int(i) for i in input().split()]
i = 0

area = []

while i < N:
    areaStr = input()
    linha = []
    j = 0
    while j < N:
        linha.append(areaStr[j])
        j += 1
    area.append(linha)

    i += 1

# Verificar se o ponto inicial foi invadido

if int(area[0][0]) <= F:
    area[0][0] = "*"

    # Percorrer a área para achar outras invasões
    # De cima pra baixo, da esquerda pra direita
    i = 0

    while i < N:
        j = 0
        while j < N:
            if i != 0:  # Senão for a linha de cima
                if int(area[i][j] == "*"):
                    # Verificando valor acima
                    if area[i - 1][j] != "*":
                        if int(area[i - 1][j]) <= F:
                            area[i - 1][j] = "*"
            if i != N - 1:  # Se não for a última linha
                if int(area[i][j] == "*"):
                    # Verificando valor abaixo
                    if area[i + 1][j] != "*":
                        if int(area[i + 1][j]) <= F:
                            area[i + 1][j] = "*"
            if j != N - 1:  # Se não for o último valor da linha
                if int(area[i][j] == "*"):
                    # Verificando valor da direita
                    if area[i][j + 1] != "*":
                        if int(area[i][j + 1]) <= F:
                            area[i][j + 1] = "*"
            if j != 0:  # Se não for o primeiro valor da linha
                if int(area[i][j] == "*"):
                    # Verificando valor da esquerda
                    if area[i][j - 1] != "*":
                        if int(area[i][j - 1]) <= F:
                            area[i][j - 1] = "*"

            j += 1
        i += 1

    # Percorrer a área para achar outras invasões
    # De baixo pra cima, da direita pra esquerda
    i = N - 1

    while i >= 0:
        j = N - 1
        while j >= 0:
            if i != 0:  # Senão for a linha de cima
                if int(area[i][j] == "*"):
                    # Verificando valor acima
                    if area[i - 1][j] != "*":
                        if int(area[i - 1][j]) <= F:
                            area[i - 1][j] = "*"
            if i != N - 1:  # Se não for a última linha
                if int(area[i][j] == "*"):
                    # Verificando valor abaixo
                    if area[i + 1][j] != "*":
                        if int(area[i + 1][j]) <= F:
                            area[i + 1][j] = "*"
            if j != N - 1:  # Se não for o último valor da linha
                if int(area[i][j] == "*"):
                    # Verificando valor da direita
                    if area[i][j + 1] != "*":
                        if int(area[i][j + 1]) <= F:
                            area[i][j + 1] = "*"
            if j != 0:  # Se não for o primeiro valor da linha
                if int(area[i][j] == "*"):
                    # Verificando valor da esquerda
                    if area[i][j - 1] != "*":
                        if int(area[i][j - 1]) <= F:
                            area[i][j - 1] = "*"

            j -= 1
        i -= 1

result = ""

for i in area:
    for j in i:
        result += j
    print(result)
    result = ""
