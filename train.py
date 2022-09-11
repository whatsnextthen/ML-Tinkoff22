import re

d = {}
cnt = {}
prob = {}

def tokenize_text(text):
    t = re.sub(r'[^\w\s]', '', text.lower())
    new_t = t.split(' ')
    return new_t

def training(word):
    for i in range (0, len(word) - 1):
        if (word[i] not in d.keys()):
            d[word[i]] = []
        ind = len(d[word[i]]) - 1
        if (word[i + 1] not in d[word[i]]):
            if (len(d[word[i]]) == 0):
                cnt[word[i]] = {}
                cnt[word[i]][word[i + 1]] = 0
            if (word[i + 1] not in d[word[i]]):
                d[word[i]].append(word[i + 1])
            if word[i + 1] not in cnt[word[i]].keys():
                cnt[word[i]][word[i + 1]] = 0
            cnt[word[i]][word[i + 1]] += 1
        else:
            if word[i + 1] not in cnt[word[i]].keys():
                cnt[word[i]][word[i + 1]] = 0
            else:
                cnt[word[i]][word[i + 1]] += 1

def probability():
    for k in d.keys():
        for i in range (len(d[k])):
            if (k not in prob.keys()):
                prob[k] = []
            tot = len(d[k])
            word = d[k][i]
            has = cnt[k][word]
            P = has / tot
            prob[k].append((word, P))

with open('Data.txt', encoding='utf-8', mode='r') as f:
    text = f.read()
text = tokenize_text(text)
training(text)

probability()

