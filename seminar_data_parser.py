import nltk
from nltk.corpus import WordListCorpusReader


def generate_file_ids():
    file_ids = []
    for i in range(301, 486):
        file_ids.append(str(i) + ".txt")
    return file_ids


def parse_data():
    reader = WordListCorpusReader('data/seminars_untagged/untagged', generate_file_ids())
    words = []

    def append_each(words_to_append, l):
        for word in words_to_append:
            l.append(word)
        return l

    for each in reader.words():
        words = append_each(each.split(" "), words)

    words = list(filter(None, words))
    words = words[words.index("Abstract"):]
    return words



print(parse_data())