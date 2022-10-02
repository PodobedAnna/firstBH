# Без использования collections, написать программу, которая будет
# создавать словарь для подсчитывания количества вхождений каждой
# буквы в текст введенный с клавиатуры

text=input('введите текст: ')
text2 = set(text)
text_dict = dict.fromkeys(text2, 0)
for text2 in text:
    text_dict [text2] += 1
print(text_dict)
