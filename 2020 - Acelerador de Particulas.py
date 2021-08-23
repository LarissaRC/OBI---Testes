# 23/08/2021
# Submissão aceita

a = int(input())

if a <= 8:
    if a == 6:
        print(1)
    elif a == 7:
        print(2)
    elif a == 8:
        print(3)
else:
    a -= 3
    b = a % 8
    if b == 3:
        print(1)
    elif b == 4:
        print(2)
    elif b == 5:
        print(3)