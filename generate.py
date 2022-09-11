import re
import numpy as np

from train import prob

def generate(first_word, length):
    word = first_word
    for i in range(length):
        a = []
        P = [] # probability
        for x, y in prob[word]:
          a.append(x)
          P.append(y)
        if (len(a) == 0):
            print("Error")
            return
        next = (np.random.choice(a, 1, P))
        print(*next, end = " ")
        word = next[0]

#Вводим слово и длину которую хотим получить
word = "#@"
while word not in prob.keys():
  word = input('Введите слово с которого хотите начать предложение ')
  if (word not in prob.keys()):
    print('Вашего слова нет в моей модели, к сожалению. Пожалуйста, введите другое слово ')

length1 = int(input('Введите количество слов в предложении '))
print(word, end = ' ')
word = word.lower()
generate(word, length1)
