import gensim

# model = gensim.models.KeyedVectors.load_word2vec_format( '~/Documents/data/GoogleNews-vectors-negative300.bin', binary=True)
# model.save("data/g_news_model.model")


model = gensim.models.KeyedVectors.load("data/g_news_model.model")
# print(model['run'])
# print(model.similarity('woman', 'man'))
print(model.most_similar(positive=['woman', 'king'], negative=['man']))
