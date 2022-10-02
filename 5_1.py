N = int(input('количество: '))
M = int(input('кратность: '))
K = int(input('миним: '))
numbs = []
while N:
    if not K % M:
        numbs.append(K)
        N -= 1
    K += 1
print(numbs)