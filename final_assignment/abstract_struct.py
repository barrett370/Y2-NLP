class Abstract:

    def __init__(self, abstract):
        self.abstract = abstract

    def get_untagged_abstract(self):
        return self.abstract

    def analyse(self, header):  # only bothers finding data for tags that haven't been found in the header
        if header.get_date() is None:
            self.analyse_date()
        if header.get_location() is None:
            self.analyse_location()
        stime, etime = header.get_times()
        if stime is None:
            self.analyse_time()
        if etime is None:
            self.analyse_time()
        if header.get_speaker() is None:
            self.analyse_speaker()

    def analyse_location(self):
        pass

    def analyse_speaker(self):
        pass

    def analyse_time(self):
        pass

    def analyse_date(self):
        pass
