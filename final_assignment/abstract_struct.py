import final_assignment.regex_tagger as rtagger
from final_assignment.misc_functions import twelve_to_twenty_four


class Abstract:

    def __init__(self, abstract):
        self.untagged_abstract = abstract
        self.tagged_abstract = None
        self.paras = None
        self.sents = None

    def get_untagged_abstract(self):
        return self.untagged_abstract

    def __str__(self) -> str:
        tagged_abstract = '\n'.join(map(str, self.tagged_abstract))

        return f"Tagged: \n {tagged_abstract} \n "

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
        self.analyse_paras()
        self.analyse_sents()

    def analyse_paras(self):
        self.paras = rtagger.find_paras(self.untagged_abstract)

    def analyse_sents(self):
        self.sents = rtagger.find_sentences(self.paras)

    def analyse_location(self):
        pass

    def analyse_speaker(self):
        pass

    def analyse_time(self):
        times_found = []
        for line in self.get_untagged_abstract():
            times_found.append(rtagger.find_times(line))
        print(times_found)
        parsed_times = []
        for each in times_found:
            if each != None:
                print(self.get_untagged_abstract())
                parsed_times.append(twelve_to_twenty_four(each[0]))

    def analyse_date(self):
        pass
