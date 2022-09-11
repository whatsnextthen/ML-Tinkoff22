import re
import numpy as np

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
word = input()
length = int(input())
word = word.lower()
generate(word, length)
