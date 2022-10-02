# Код Морзе для представления цифр и букв использует тире и точки. Напишите
# функцию для кодирования текстового сообщения в соответствии с кодом Морзе.

morse = {
    'a': '•—', 'b': '—•••',
         'c': '—•—•', 'd': '—••',
         'e': '•', 'f': '••—•',
         'g': '——•', 'h': '••••',
         'i': '••', 'j': '•———',
         'k': '—•—', 'l': '•—••',
         'm': '——', 'n': '—•',
         'o': '———', 'p': '•——•',
         'q': '——•—', 'r': '•—•',
         's': '•••', 't': '—',
         'u': '••—', 'v': '•••—',
         'w': '•——', 'x': '—••—',
         'y': '—•——', 'z': '——••'
         }

# def Morse(s):
#     a = ''
#     for i in s.upper():
#         if i in morse.keys(): a += morse[i] + ' '
#         if i == ' ': a += ' / '  # Слова разделяются слэшем t
#     return a
#
# def get_key(val, dct):  # Функция возвращает ключ словаря по значению
#     for key, value in dct.items():
#         if val == value: return key
#
# def MorseTxt(s):
#     a, s = '', s.split()
#     for i in s:
#         if i in morse.values(): a += get_key(i, morse)
#         if i == '/': a += ' '
#     return a
#
#
# a = input('enter text ')
# print(Morse(a))
# print(MorseTxt(Morse(a)))


result = []
a = input()
for word in a.split()
    word2 = []
    for i in word
        word2.append(morze[i])
    result.append(' '.join(word2))
print('\t'.join(result))
