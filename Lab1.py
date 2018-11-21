import re
from collections import Counter


def words(text): return re.findall(r'\w+', text.lower())


WORDS = Counter(words(open('data/big.txt').read()))


def denominator(dictionary):
    acc = 0
    for value in dictionary.values():
        acc += value
    return acc


def P(word):
    return WORDS[word] / denominator(WORDS)


print(P('the'))
print(P('and'))
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
        for j in range(len(word)):
            if i != j:
                temp5 = list(word)
                t = temp5[i]
                temp5[i] = temp5[j]
                temp5[j] = t
                permutations.append("".join(temp5))
        if i <= len(word):
            temp3 = list(word)
            temp3[i] = ""
            permutations.append("".join(temp3))
    for j in range(97, 123):
        temp4 = list(word)
        temp4.append(chr(j))
        permutations.append("".join(temp4))

    return permutations


print(len(edits1('cat')))
print(edits1('cat'))


def edits2(word):
    permutations = edits1(word)
    ret = []
    for each in permutations:
        ret += edits1(each)

    return ret


print(edits2('cat'))
print(len(edits2('cat')))


def rem_dup(words):
    acc = []
    for word in words:
        if not acc.__contains__(word):
            acc.append(word)
    return acc


print(len(rem_dup(edits1('cat'))))
print(rem_dup(edits1('cat')))


def check_dict(words):
    acc = []
    for word in words:
        if WORDS[word] != 0:
            acc.append(word)
    return acc


print(check_dict(edits1('cat')))


def candidates(word):
    corrections = []
    corrections += edits1(word)
    corrections += edits2(word)
    # print(len(corrections))
    corrections2 = check_dict(corrections)
    # print(len(corrections2))
    return corrections2


print("\n\n\n")
print(candidates('ca'))
print("CanLEN"+ str(len(candidates('cat'))))

def predict(word):
    possible_corrections = candidates(word)
    possible_corrections.sort(key=lambda x: P(x), reverse=True)
    return possible_corrections[0]


print(predict('cimputer'))
print(P('ba'))