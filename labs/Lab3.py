# from nltk.corpus import WordListCorpusReader
#
#

#
# def into():
#     import nltk
#
#     from nltk.corpus import brown, treebank
#
#     brown.words()
#
#     treebank.words()
#
#     print(len(treebank.tagged_sents()))
#
#     ##2. as the total number of tagged sentences in the treebank corpus is 3914 this is therefore a 77:23 split
#
#     train_sents = treebank.tagged_sents()[:3000]
#
#     test_sents = treebank.tagged_sents()[3000:]
#
#     from nltk.tag import DefaultTagger
#
#     tagger = DefaultTagger('NN')
#
#     print(tagger.tag_sents([['Hello', '.'], ['My', 'name', 'is', 'Steve']]))
#
#     print(tagger.evaluate(test_sents))
#
#     from nltk.tag import UnigramTagger
#
#     print("uni")
#     unigram_tagger = UnigramTagger(train_sents)
#
#     print(unigram_tagger.evaluate(test_sents))
#     print(unigram_tagger.evaluate(train_sents))
#
#     unigram_tagger2 = UnigramTagger(train_sents, cutoff=3)
#
#     print(unigram_tagger2.evaluate(test_sents))
#
#     from nltk.tag import BigramTagger
#
#     print("bi")
#     bigram_tagger = BigramTagger(train_sents)
#
#     print(bigram_tagger.evaluate(test_sents))
#     print(bigram_tagger.evaluate(train_sents))
#
#     bigram_tagger2 = BigramTagger(train_sents, cutoff=3)
#     print(bigram_tagger2.evaluate(test_sents))
#
#     from nltk.tag import TrigramTagger
#
#     print("tri")
#     trigram_tagger = TrigramTagger(train_sents)
#
#     print(trigram_tagger.evaluate(test_sents))
#     print(trigram_tagger.evaluate(train_sents))
#
#     trigram_tagger2 = TrigramTagger(train_sents, cutoff=3)
#     print(trigram_tagger2.evaluate(test_sents))
#
#     print("brill")
#
#     import brill_tagger_wrapper
#
#     brill_tagger = brill_tagger_wrapper.train_brill_tagger(trigram_tagger, train_sents)
#     print(brill_tagger.evaluate(test_sents))
#
#     print("backoff")
#     bt = backoff_tagger(train_sents, [UnigramTagger, BigramTagger, TrigramTagger], DefaultTagger('NN'))
#
#     print(bt.evaluate(test_sents))
#
from labs import seminar_data_parser


def generatefileids():
    fileids = []
    for i in range(301, 486):
        fileids.append(str(i) + ".txt")
    return fileids


class tagger():
    def __init__(self):
        from nltk import UnigramTagger
        from nltk import BigramTagger
        from nltk import TrigramTagger
        from nltk import DefaultTagger
        # print(len(brown.tagged_sents()))
        # train_sents = brown.tagged_sents()[:50000]
        # self.test_sents = brown.tagged_sents()[50000:]
        train_sents = seminar_data_parser.get_tagged()
        print(train_sents)

        self.bt = self.backoff_tagger(train_sents, [UnigramTagger, BigramTagger, TrigramTagger], DefaultTagger('NN'))

    def backoff_tagger(self, train_sentences, tagger_classes, backoff=None):
        for cls in tagger_classes:
            backoff = cls(train_sentences, backoff=backoff)
        return backoff

    def tag(self, words):
        # print(self.bt.evaluate(self.test_sents))
        #
        # import seminar_data_parser
        # words = seminar_data_parser.parse_data()
        return self.bt.tag(words)




# main()
# into()
