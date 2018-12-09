# import nltk
# from nltk.corpus import WordListCorpusReader
#

#
# print(reader.words())
from nltk import WordNetLemmatizer
from nltk.corpus import names, WordListCorpusReader
from nltk.tokenize import word_tokenize

local_names = names.words()

print(names.fileids())

male_names = names.words('male.txt')
female_names = names.words('female.txt')

print('Sam' in male_names)

from nltk.stem.porter import *

stemmer = PorterStemmer()

print(stemmer.stem('running'))

wnl = WordNetLemmatizer()

print(wnl.lemmatize('dogs'))

reader = WordListCorpusReader('data/', ['computerscience.txt'])
print(len(reader.words()))
words = list(map(lambda x: word_tokenize(x), reader.words()))
lemmitised_words = []
stemmed_words = []
print(len(words))

flattened_list = [y for x in words for y in x]
print(len(flattened_list))

for word in flattened_list:
    lemmitised_words.append(wnl.lemmatize(word))
    stemmed_words.append(stemmer.stem(word))

print(lemmitised_words, '\n\n\n', stemmed_words)

# date_re = [r'^\d{2}[/-\s]\']
