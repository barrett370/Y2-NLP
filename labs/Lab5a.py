from nltk.corpus import wordnet, semcor

init_option = input("Would you like to use user input or SemCor? (u/s) ")
if init_option == "u":
    word = input("Enter word")
    '''
        Provide all senses of that word along with the meanings. 
        Provide all the immediate hypernyms of the word
        Provide all the immediate hyponyms of the word. 
        Provide a list of the hypernym closure (this is the hypernym of the hypernym of the ...) 
    '''
    synsets = wordnet.synsets(word)

    for synset in synsets:
        print(">>>> " + str(synset))
        print(">>>>>> definition: " + synset.definition())
        print(">>>>>> " + "hypernyms: " + str(synset.hypernyms()))
        print(">>>>>> " + "hyponyms: " + str(synset.hyponyms()))
        hypo = lambda s: s.hyponyms()
        print(">>>>>> Hypernym closure: ")
        print(list(synset.closure(hypo, depth=1)))



elif init_option == "s":

    sc_tagged = semcor.tagged_sents()[0:100]
    sc = semcor.sents()[0:100]
    sc_defs = []
    for i in range(len(sc_tagged)):
        # print(sc_tagged[i])
        line_defs = []
        for j in range(len(sc_tagged[i])):
            word = sc[i][j]
            word_tagged = sc_tagged[i][j]
            try:
                definition = wordnet.synsets(word)[0].definition()
                line_defs.append([word_tagged, definition])
            except:
                definition = "N/A"
        print(line_defs)
        sc_defs.append(line_defs)

else:
    print("Error: Not a valid option")
