import nltk
from nltk.corpus import WordListCorpusReader


def generate_file_ids_untagged():
    file_ids = []
    for i in range(301, 486):
        file_ids.append(str(i) + ".txt")
    return file_ids


def generate_file_ids_tagged():
    file_ids = []
    for i in range(0, 300):
        file_ids.append(str(i) + ".txt")
    return file_ids



def get_untagged():
    reader = WordListCorpusReader('data/seminars_untagged/untagged', generate_file_ids_untagged())
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

def get_tagged():
    reader = WordListCorpusReader('data/seminars_training/training', generate_file_ids_tagged())
    words = []
    # print(reader.words())    reader = WordListCorpusReader('data/seminars_untagged/untagged', generate_file_ids_untagged())

    # def append_each(words_to_append, l):
    #     for word in words_to_append:
    #         l.append(word)w
    #     return l
    #
    # for each in reader.words():
    #     try:
    #         words = words.append(each)
    #     except:
    #         pass
    # words = list(filter(None, words))
    # words = words[words.index("Abstract"):]
    return reader.words()


# print(parse_data())