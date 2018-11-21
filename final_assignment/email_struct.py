class Email:
    def __init__(self, header, abstract):
        self.header = header
        self.abstract = abstract

    def get_header(self):
        return self.header

    def get_abstract(self):
        return self.abstract
