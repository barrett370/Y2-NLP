# import gensim
#
# # model = gensim.models.KeyedVectors.load_word2vec_format( '~/Documents/data/GoogleNews-vectors-negative300.bin', binary=True)
# # model.save("data/g_news_model.model")
#
#
# model = gensim.models.KeyedVectors.load("data/g_news_model.model")
# # print(model['run'])
# # print(model.similarity('woman', 'man'))
# print(model.most_similar(positive=['woman', 'king'], negative=['man']))
import gensim

import gensim.downloader as api
import gensim.models as m
info = api.info()  # show info about available models/datasets
# model = api.load("glove-twitter-200")  # download the model and return as object ready for use
# model = m.Word2Vec.load("data/conc_model.model")
model = gensim.models.KeyedVectors.load("data/conc_model.model")


print(model.most_similar("cat"))
# model.save("data/conc_model.model")
