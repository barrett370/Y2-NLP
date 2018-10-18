import nltk
from nltk.tag import brill, brill_trainer
from nltk.tag import UnigramTagger
from nltk.corpus import treebank


# make sure you've got some train_sents!

def train_brill_tagger(initial_tagger, train_sents, **kwargs):
	templates = [
		brill.Template(brill.Pos([-1])),
		brill.Template(brill.Pos([1])),
		brill.Template(brill.Pos([-2])),
		brill.Template(brill.Pos([2])),
		brill.Template(brill.Pos([-2, -1])),
		brill.Template(brill.Pos([1, 2])),
		brill.Template(brill.Pos([-3, -2, -1])),
		brill.Template(brill.Pos([1, 2, 3])),
		brill.Template(brill.Pos([-1]), brill.Pos([1])),
		brill.Template(brill.Word([-1])),
		brill.Template(brill.Word([1])),
		brill.Template(brill.Word([-2])),
		brill.Template(brill.Word([2])),
		brill.Template(brill.Word([-2, -1])),
		brill.Template(brill.Word([1, 2])),
		brill.Template(brill.Word([-3, -2, -1])),
		brill.Template(brill.Word([1, 2, 3])),
		brill.Template(brill.Word([-1]), brill.Word([1])),
	]
	
	trainer = brill_trainer.BrillTaggerTrainer(initial_tagger, templates, deterministic=True)
	return trainer.train(train_sents, **kwargs)
train_sents = treebank.tagged_sents()[:3000]
test_sents = treebank.tagged_sents()[3000:]
unigram_tagger = UnigramTagger(train_sents) 
brill_tagger = train_brill_tagger(unigram_tagger, train_sents)
