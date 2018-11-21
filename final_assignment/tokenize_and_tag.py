def backoff_tagger(train_sentences, tagger_classes, backoff=None):
    for cls in tagger_classes:
        backoff = cls(train_sentences, backoff=backoff)
    return backoff


class Tagger:
    def __init__(self):
        from nltk import UnigramTagger
        from nltk import BigramTagger
        from nltk import TrigramTagger
        from nltk import DefaultTagger
        from nltk.corpus import brown
        train_sentences = brown.tagged_sents()[:50000]
        self.bt = backoff_tagger(train_sentences, [UnigramTagger, BigramTagger, TrigramTagger], DefaultTagger('NN'))

    def tag(self, words):
        return self.bt.tag(words)
