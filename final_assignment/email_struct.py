class Email:
    def __init__(self, header, abstract):
        self.header = header
        self.abstract = abstract

    def get_header(self):
        return self.header

    def get_abstract(self):
        return self.abstract

    def tag_all(self):
        self.tag_header()

    def tag_header(self):
        self.header.analyse()
        print(self.header)
        import re
        tagged_header = self.header.untagged_header
        for line in tagged_header():
        # todo implement tagger
            try:
                re.sub("(" + self.header.speaker + ")", f"<speaker>{self.header.get_speaker()}</speaker", line)
                re.sub(r'(' + str(self.header.start_time) + ")", f"<stime>{self.header.start_time}</stime>", line)
                re.sub(r'(' + str(self.header.end_time) + ")", f"<etime>{self.header.end_time}</etime>", line)
                re.sub(r'(' + str(self.header.date) + ")", f"<date>{self.header.date}</date>", line)
                re.sub(r'(' + str(self.header.location) + ")", f"<location>{self.header.location}</location>", line)
            except:
                pass

        print(self.header.get_untagged_header())
