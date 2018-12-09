import nltk

grammar1 = nltk.CFG.fromstring("""
 S -> NP VP
 VP -> V NP | V NP PP
 PP -> P NP
 PN -> "she" | "She" |"He" |"They" |"this"
 V -> "saw" | "ate" | "walked" | "eat" |"enjoyed" | "going" | "watches" | "went" |"like" | "watch" |"likes"  |"used" 
 NP -> "John" | "Mary" | "Bob" | Det N | Det N PP | PN  |Det Det N | "Smith" |"John."|  "Jane" |"Lee" |"Kim" |"Kim." |"December." |"Mary."
 Det -> "a" | "an" | "the" | "my" | "who" | "Did"  | "The" | "to" |"didn't" 
 N -> "man" | "dog" | "cat" | "telescope" | "park" | "fish" | "fork" | "movies." |"western" |"cinema" |"horror" |"child" |"child." |"telescope." |"telescopes" |"home" 
 P -> "in" | "on" | "by" | "with"  |"sometimes" |"Every" 
 """)

sent = "The cat ate the fish".split()

rd_parser = nltk.RecursiveDescentParser(grammar1)

# for tree in rd_parser.parse(sent):
#     print(tree)
#

#
# tokens = 'Michael likes children'.split()

#
# cp = load_parser('predef_grammar.fcfg', trace=2)
#
# for tree in cp.parse(tokens):
#     tree.draw()
#
#

sr_parser = nltk.ShiftReduceParser(grammar1, trace=2)
#
# sent = 'Mary saw a dog'.split()
#
# for tree in sr_parser.parse(sent):
#     tree.draw()

c_parser = nltk.ChartParser(grammar1, trace=2)

sents = open('sents', 'r')
from labs import Lab3

tagger = Lab3.tagger
tagger.__init__(tagger)
for sentence in sents.read().split("\n"):
    for tree in sr_parser.parse(sentence.split()):
        # print(tree)
        pass
    for tree in c_parser.parse(sentence.split()):
        print(tree)
        # tree.draw()

    print(tagger.tag(tagger, sentence.split()))
