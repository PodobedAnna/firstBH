# пользователь вводит предложение, заменить все пробелы на '-' двумя способами
sentence = input('введите предложение: ')
sentence=sentence.replace(' ','-')
print(sentence)
# второй способ
text=input('введите текст:')
text2=text.split(' ')
text3='-'.join(text2)
print(text3)