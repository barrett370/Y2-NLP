import final_assignment.regex_tagger as rtagger
from final_assignment import training_entity_extraction as tee
from final_assignment.misc_functions import twelve_to_twenty_four, formal_date_format


class Header:

    def __init__(self, untagged_header):
        self.speaker = None
        self.start_time = None
        self.end_time = None
        self.location = None
        self.date = None
        self.untagged_header = untagged_header
        self.tagged_header = None
        self.times = []
        self.dates = []

    def __str__(self) -> str:

        tagged_header = '\n'.join(map(str, self.tagged_header))

        return f"""Header Structure, Info: \n Speaker: {str(self.speaker)} \n Start time: {str(
            self.start_time)} \n End time: {str(self.end_time)
        }\n Location: {str(self.location)} \n Date: {str(self.date)}   \n Untagged Header: {self.untagged_header} \n 
        Tagged Header: \n {tagged_header}"""

    def set_tagged_header(self, text):
        self.tagged_header = text

    def analyse(self):
        self.analyse_times()
        self.analyse_dates()
        self.analyse_speakers()
        self.analyse_locations()

    def get_untagged_header(self):
        return self.untagged_header

    def set_start_time(self, time):
        self.start_time = time

    def set_end_time(self, time):
        self.end_time = time

    def set_date(self, date):
        self.date = date

    def get_date(self):
        return self.date

    def get_times(self):
        return self.start_time, self.end_time

    def get_location(self):
        return self.location

    def get_speaker(self):
        return self.speaker

    def analyse_times(self):

        times_found = rtagger.find_times_with_tag(self.get_untagged_header())
        formal_times = []
        for time in times_found:
            formal_times.append(twelve_to_twenty_four(time))
        if len(formal_times) == 1:  # only start time present
            self.set_start_time(str(formal_times[0][0]) + ":" + str(formal_times[0][1]))
        else:  # decide which is start / which is end
            current_lowest = (25, 61)
            for time in formal_times:
                if int(time[0]) < int(current_lowest[0]):
                    current_lowest = time
                elif int(time[0]) == int(current_lowest[0]):
                    if int(time[1]) < int(current_lowest[1]):
                        current_lowest = time
            self.start_time = str(current_lowest[0]) + ":" + str(current_lowest[1])

            current_highest = (00, 00)
            for time in formal_times:
                if int(time[0]) > int(current_highest[0]):
                    current_highest = time
                elif int(time[0]) == int(current_highest[0]):
                    if int(time[1]) > int(current_highest[1]):
                        current_highest = time
            self.end_time = str(current_highest[0]) + ":" + str(current_highest[1])

    def analyse_dates(self):
        dates_found = rtagger.find_dates_with_tag(self.get_untagged_header())
        dates_normalised = []
        for x in dates_found:
            dates_normalised.append(formal_date_format(x))
        sorted_dates = sorted(dates_normalised, key=lambda d: map(int, d[0].split('-')))

        try:
            self.set_date(sorted_dates[0][0])
        except:
            pass

    def analyse_speakers(self):
        speakers, _ = tee.extract_entities()
        speaker = rtagger.find_speakers_with_tag(self.get_untagged_header(), speakers)
        import re
        speaker_r = None
        if speaker is not None:
            speaker_r = re.sub(r'[^\w\s]', '', speaker)
        self.speaker = speaker_r

    def analyse_locations(self):
        _, locations = tee.extract_entities()
        location = rtagger.find_locations_with_tag(self.get_untagged_header(), locations)
        self.location = location
# todo improve name extraction to work around titles, middle names etc.
