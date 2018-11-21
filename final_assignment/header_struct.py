class Header:

    def __init__(self, untagged_header):
        self.speaker = None
        self.start_time = None
        self.end_time = None
        self.location = None
        self.date = None
        self.untagged_header = untagged_header
        self.times = []
        self.dates = []

    def __str__(self) -> str:
        return super().__str__()

    def get_untagged_header(self):
        return self.untagged_header

    def set_start_time(self, time):
        self.start_time = time

    def set_end_time(self, time):
        self.end_time = time

    def set_date(self, date):
        self.date = date

    def analyse_times(self):
        import final_assignment.regex_tagger as rtagger
        import final_assignment.seminar_data_extractor as extractor

        times_found = rtagger.find_times(extractor.flatten(self.get_untagged_header()))
        print("TIMES FOUND:" + str(times_found))
        current_lowest = (25, 61)
        for t in times_found:
            time = t[0]
            if int(time[0]) < current_lowest[0]:
                current_lowest = time
            elif int(time[0]) == current_lowest[0]:
                if int(time[1]) < current_lowest[1]:
                    current_lowest = time
        self.start_time = current_lowest

        print("START TIME:: " + str(self.start_time))
