import gensim


def sim_list(topic, words, key):  # todo should this sum the similarities?
    scores = []
    model = gensim.models.KeyedVectors.load("../data/g_news_model.model")
    for word in words:
        try:
            scores.append((key, model.similarity(topic, word)))
        except:  # Word not in vocabulary
            scores.append((key, 0))

    return scores


class Ontology:
    def __init__(self):
        self.ontology = {'top': {'science': {
            'computer science': {'robotics': {'topic_words': ['java', 'robotics', 'robots', 'automation'], 'talks': []},
                                 'artificial intelligence': {'topic_words': ['ai', 'bayes', 'artificial intelligence']},
                                 }}}}
        try:
            self.load()
        except FileNotFoundError:
            pass
        print(self.ontology)
        self.traversal_info = dict()
        self.traverse()
        # print(self.traversal_info)

    def __str__(self) -> str:
        return f"Ontology: {self.ontology} \n Traversal_info: {self.traversal_info}"

    def traverse(self, location=None, key=None):
        if location is None:
            location = self.ontology
        keys = location.keys()
        if 'topic_words' in keys:
            self.traversal_info[key] = location
            return
        else:
            for key in keys:
                self.traverse(location[key], key)
            return

    def add_to(self, topic, file_name):
        # scores =  \
        #         [
        #             (dist_measure(topic, self.traversal_info[key][‘topic_words’],
        #             key)
        #             for key in self.traversal_info.keys()
        #         ]
        scores = [(sim_list(topic, self.traversal_info[key]['topic_words'], key))
                  for key in self.traversal_info.keys()]
        flat_scores = []
        for l in scores:
            for t in l:
                flat_scores.append(t)
        # sorted_scores = flat_scores.sort(key=lambda x: x[1], reverse=True)
        sorted_scores = sorted(flat_scores, key=lambda x: x[1], reverse=True)
        max_score_item = sorted_scores[0][0]
        self.traversal_info[max_score_item]['talks'].append(file_name)

    def add_topics_interactive(self):
        # or do this manually.

        # print("Topic: " + topic)

        input_class = input("Enter Class:")
        input_words = input("Class words:")
        self.traversal_info[input_class.rstrip()]['topic_words'] += input_words.rstrip().split(', ')
        print(self)
        return

    def save(self):

        f = open("../data/ontology/ontology_save.txt", "w+")
        f.write(str(self.ontology))
        f.close()

    def load(self):
        f = open("../data/ontology/ontology_save.txt", "r")
        self.ontology = eval(f.read())


def pop_ont():
    ont = Ontology()
    while True:
        cont = input("continue? y/n")
        if cont is "y":
            ont.add_topics_interactive()
        else:
            ont.save()
            break


#
# ontology = Ontology()
# ontology.add_to("AN ASYNCHRONOUS TEAM SOLUTION TO SCHEDULING STEEL PLANTS IN DIRECT HOT CHARGE MODE", "testfile")
# print(ontology.traversal_info)

pop_ont()
