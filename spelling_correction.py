import re
from collections import Counter


def words(text): return re.findall(r'\w+', text.lower())


WORDS = Counter(words(open('data/big.txt').read()))


def denom(dictionary):
    acc = 0
    for value in dictionary.values():
        acc += value
    return acc


def P(word):
    return WORDS[word] / denom(WORDS)


print(P('the'))

print(P('computer'))


def edits1(word):
    permutations = []
    for i in range(len(word)):
        for j in range(97, 123):
            temp = list(word)
            temp[i] = chr(j)
            permutations.append("".join(temp))
            temp2 = list(word)
            temp2.insert(i, chr(j))
            permutations.append("".join(temp2))

        if i <= len(word):
            temp3 = list(word)
            temp3[i] = ""
            permutations.append("".join(temp3))
    for j in range(97, 123):
        temp4 = list(word)
        temp4.append(chr(j))
        permutations.append("".join(temp4))
    temp = list(word)
    for i in range(len(temp)):
        for j in range(len(temp)):
            if i != j:
                t = temp[i]
                temp[i] = temp[j]
                temp[j] = t
                permutations.append("".join(temp))

    return permutations


print(len(edits1('cat')))
print(edits1('cat'))
