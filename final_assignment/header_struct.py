from final_assignment import seminar_data_extractor as extractor
import final_assignment.regex_tagger as rtagger


def twelve_to_twenty_four(time_am_pm):
    # remove spaces
    time = []
    for each in time_am_pm:
        if each != '':
            if each != ' ':
                if each != ':':
                    time.append(each)

    if time.__contains__('PM'):
        hour = str(int(time[0]) + 12)
    else:
        hour = time[0]
    ret = [hour]
    if time[1] != ':':
        ret.append(time[1])
    else:
        ret.append(time[2])
    return ret[0], ret[1]


def formal_date_format(dates_list):
    dates_ret = []
    months = {'Jan': '1', 'Feb': '2', 'Mar': '3', 'Apr': '4', 'May': '5', 'Jun': '6', 'Jul': '7', 'Aug': '8',
              'Sep': '9', 'Oct': '10',
              'Nov': '11', 'Dec': '12'}
    print(months['Jan'])
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
        return 'Header Struct, Info: \n Speaker: ' + str(self.speaker) + '\n Start time: ' + str(
            self.start_time) + '\n End time: ' + str(self.end_time) \
               + '\n Location: ' + str(self.location) + '\n Date: ' + str(self.date) + '\n \n '

    def get_untagged_header(self):
        return self.untagged_header

    def set_start_time(self, time):
        self.start_time = time

    def set_end_time(self, time):
        self.end_time = time

    def set_date(self, date):
        self.date = date

    def analyse_times(self):

        times_found = rtagger.find_times(extractor.flatten(self.get_untagged_header()))

        check_for = ['PM', 'AM', 'Am', 'Pm', 'aM', 'pM', 'am', 'pm']
        parsed_times = []
        for times in times_found:
            for each in times:
                for element in check_for:
                    if each.__contains__(element):
                        each = twelve_to_twenty_four(each)
                        break
                parsed_times.append(each)
        current_lowest = (25, 61)
        times_found = parsed_times
        for time in times_found:

            if int(time[0]) < int(current_lowest[0]):
                current_lowest = time
            elif int(time[0]) == int(current_lowest[0]):
                if int(time[1]) < int(current_lowest[1]):
                    current_lowest = time
        self.start_time = current_lowest

        current_highest = (00, 00)
        for time in times_found:
            if int(time[0]) > int(current_highest[0]):
                current_highest = time
            elif int(time[0]) == int(current_highest[0]):
                if int(time[1]) > int(current_highest[1]):
                    current_highest = time
        self.end_time = current_highest

    def analyse_dates(self):
        dates_found = rtagger.find_dates(extractor.flatten(self.get_untagged_header()))
        dates_normalised = []
        for x in dates_found:
            dates_normalised.append(formal_date_format(x))
        sorted_dates = sorted(dates_normalised, key=lambda d: map(int, d[0].split('-')))
        self.set_date(sorted_dates[0][0])
