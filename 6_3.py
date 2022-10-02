# Дан список чисел и на вход поступает число N, необходимо сместить список на
# указанное число
s = input('Введите список чисел через пробел: ')
n = int(input('На сколько сдвиг? - '))
def func(l, n):
    return l[n:] + l[:n]
    l = list(map(int, s.split()))

    while len(l)<n:
        a = list(map(x[i] + n, l))
        return a

print(func(s,n))

