class Ontology:
    def __init__(self):
        self.ontology = {
            'Top': {
                'arts': {
                    'history': {'topic_words': ['history'],
                                'talks': []}},
                'science': {
                    'computer science': {'topic_words': ['computer science', 'robotics'], 'talks': []}
                }}}
        self.traversal_info = dict()
        self.traverse()
        # print(self.traversal_info)

    def traverse(self, location=None, key=None):
        if location is None:
            location = self.ontology
        keys = location.keys()
        if 'topic_words' in keys:
            self.traversal_info[key] = location[key]
            return
        for key in keys:
            self.traverse(location[key], key)

        return

    def add_topics_interactive(self, topic, file_name):
        pass

    def add_to(self, topic, file_name):
        pass


ont = Ontology()
