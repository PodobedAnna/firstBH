# Сделать калькулятор: у пользователя
# спрашивается число, потом действие и второе
# число
numb1 = int(input())
action = input()
numb2 = int(input())
if action == '+':
    print(numb1 + numb2)
elif action == '-':
    print(numb1 - numb2)
elif action == '*':
    print(numb1 * numb2)
elif action == '/':
    print(numb1 / numb2)