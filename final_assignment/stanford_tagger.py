from nltk import StanfordNERTagger
from nltk.tokenize import word_tokenize


class StanfordTagger:
    def __init__(self):
        self.st = StanfordNERTagger("/home/sam/apps/stanford-ner-2018-10-16/classifiers/english.all.3class.distsim.crf.ser.gz",
                               "/home/sam/apps/stanford-ner-2018-10-16/stanford-ner.jar", encoding='utf-8')

    def classify(self,text):
        tokenized_text = word_tokenize(text)
        classified_text = self.st.tag(tokenized_text)
        return classified_text
