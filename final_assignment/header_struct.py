import final_assignment.regex_tagger as rtagger
from final_assignment import training_entity_extraction as tee


def twelve_to_twenty_four(time_am_pm):
    # remove spaces
    global hour
    time = []
    for each in time_am_pm:
        if each != '':
            if each != ' ':
                if each != ':':
                    time.append(each)
    pms = ['PM', 'pm', 'Pm', 'pM', 'p.m.', 'P.m.', 'p.m', 'P.M.', 'p.M.', 'P.m']
    for pm in pms:
        if time.__contains__(pm):
            if time[0] != '12':
                hour = str(int(time[0]) + 12)
                break
        else:
            hour = time[0]
    ret = [hour]
    if time[1] != ':':
        ret.append(time[1])
    else:
        ret.append(time[2])
    if 1 <= int(ret[0]) <= 7:  ## if hour is in range 1 -> 7 without PM denotion inferred that in afternoon
        ret[0] = int(ret[0]) + 12
    return ret[0], ret[1]


def formal_date_format(dates_list):
    dates_ret = []
    months = {'Jan': '1', 'Feb': '2', 'Mar': '3', 'Apr': '4', 'May': '5', 'Jun': '6', 'Jul': '7', 'Aug': '8',
              'Sep': '9', 'Oct': '10',
              'Nov': '11', 'Dec': '12'}
    for date in dates_list:
        ret = ""
        for element in date:
            try:
                ret += months[element] + '-'
            except:
                ret += element + '-'
        ret = ret[:-1]
        dates_ret.append(ret)
    return dates_ret


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
        return f"""Header Structure, Info: \n Speaker: {str(self.speaker)} \n Start time: {str(
            self.start_time)} \n End time: {str(self.end_time)
        }\n Location: {str(self.location)} \n Date: {str(self.date)}   \n """

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
        if len(formal_times) == 1:  ##only start time present
            self.set_start_time(formal_times[0])
        else:  ##decide which is start / which is end
            current_lowest = (25, 61)
            for time in formal_times:
                if int(time[0]) < int(current_lowest[0]):
                    current_lowest = time
                elif int(time[0]) == int(current_lowest[0]):
                    if int(time[1]) < int(current_lowest[1]):
                        current_lowest = time
            self.start_time = current_lowest

            current_highest = (00, 00)
            for time in formal_times:
                if int(time[0]) > int(current_highest[0]):
                    current_highest = time
                elif int(time[0]) == int(current_highest[0]):
                    if int(time[1]) > int(current_highest[1]):
                        current_highest = time
            self.end_time = current_highest

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
        self.speaker = speaker

    def analyse_locations(self):
        _, locations = tee.extract_entities()
        location = rtagger.find_locations_with_tag(self.get_untagged_header(), locations)
        self.location = location
