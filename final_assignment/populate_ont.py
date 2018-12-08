def add_topics_interactive(self, topic, file_name):
    # or do this manually.

    print("Topic: " + topic)
    print(self.print())  ## define this.
    input_class = input("Enter Class:")
    input_words = input("Class words:")
    self.traverse[input_class.rstrip()]['topic_words'] += input_words.rsrip().split(', ')

    return
