# import nltk
#

def gender_features(word):
    return {'last_letter': word[-1]}


from nltk.corpus import names

labeled_names = ([(name, 'male') for name in names.words('male.txt')] + [(name, 'female') for name in
                                                                         names.words('female.txt')])
import random

random.shuffle(labeled_names)
#
featuresets = [(gender_features(n), gender) for (n, gender) in labeled_names]
print(featuresets)
train_set, test_set = featuresets[500:], featuresets[:500]
# classifier = nltk.NaiveBayesClassifier.train(train_set)
#
# print(classifier.classify(gender_features('Neo')))
import nltk

import final_assignment.seminar_data_extractor as extractor

emails = extractor.get_untagged()
import final_assignment.regex_tagger as rtagger

pairs = []
for email in emails:
    pairs.append(rtagger.extract_topic_tag(email.get_header().get_untagged_header()))


# for pair in pairs:
#     print(pair)
def type_feature(pair):
    return {"topic": pair[1]}


labeled_topics = ([(type_feature(pair[1]), pair[1]) for pair in pairs])

print(len(pairs))

train_set, test_set = labeled_topics[:100], labeled_topics[100:]

classifier = nltk.NaiveBayesClassifier.train(train_set)

for pair in test_set:
    print(classifier.classify(pair[0]))
