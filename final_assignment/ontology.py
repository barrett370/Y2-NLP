import gensim

model = gensim.models.KeyedVectors.load("../data/g_news_model.model")


def sim_list(topic, words, key):  # todo should this sum the similarities?
    global score
    scores = []
    for item in words:
        for word in topic.split(" "):
            score = 0
            try:
                score += model.similarity(item, word.lower())
            except:  # Word not in vocabulary
                pass
        if score is not 0:
            scores.append((key, score))
    return scores


class Ontology:
    def __init__(self):
        self.ontology = {'top': {'science': {'computer science': {
            'robotics': {'topic_words': ['java', 'robotics', 'robots', 'automation', 'exploration'], 'talks': []},
            'artificial intelligence': {'topic_words': ['ai', 'bayes', 'artificial intelligence', 'bayesian'],
                                        'talks': []},
            'functional programming': {'topic_words': ['ocaml', 'haskell', 'clojure', 'lambda calculus', 'coq', 'agda'],
                                       'talks': []},
            'vision': {'topic_words': ['roberts', 'sobel', 'convolve', 'camera', 'matlab'], 'talks': []},
            'natural language processing': {'topic_words': [], 'talks': []},
            'n/a': {'topic_words': [], 'talks': []}}}}}  # overwritten by save file if present
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
        global max_score_item
        scores = [(sim_list(topic, self.traversal_info[key]['topic_words'], key))
                  for key in self.traversal_info.keys()]

        flat_scores = []
        for l in scores:
            for t in l:
                flat_scores.append(t)
        print(file_name + str(flat_scores))
        if not flat_scores:
            for key in self.traversal_info.keys():
                score = 0
                for word in self.traversal_info[key]['topic_words']:
                    if word in topic:
                        score += 1
                scores.append((key, score))
                try:
                    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
                    max_score_item = sorted_scores[0]
                except:
                    max_score_item = "n/a"
        else:
            summed_scores = []
            for tag in self.traversal_info.keys():
                sum_score = 0
                for score in flat_scores:
                    if score[0] is tag:
                        sum_score += score[1]
                summed_scores.append((tag, sum_score))
            flat_scores = summed_scores
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

    def save_pop(self):

        f = open("../data/ontology/ontology_pop_save.txt", "w+")
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

# pop_ont()
