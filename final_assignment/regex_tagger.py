import re

# time_reg = [
#     r'([0-9]|[0-1][0-9]|[2][0-3])(:|\s)([0-5][0-9])(\s{0,1})(AM|PM|am|pm|aM|Am|pM|Pm{2,2})|(([0][0-9]|[1][0-9]|[2][0-3])(\s{0,1})(AM|PM|am|pm|aM|Am|pM|Pm{2,2}))$',
#     r'([0-1][0-9]|[2][0-3]):([0-5][0-9])',
#     r'([0-9]|[0-1][0-9]|[2][0-3])(:|\s)([0-5][0-9])$']
from final_assignment.misc_functions import flatten_list

# for header
# time_reg [ matches [0-12] + (0|1 * \s) + PM|AM|pm|am (12hr clock) ,
#           matches 24hr clock

time_reg = r'([0-9]|[0-1][0-9]|[2][0-3])(:|\s)([0-5][0-9])(\s{0,1})(AM|PM|am|pm|aM|Am|pM|Pm{2,2})|([0][0-9]|[1][0-9]|[2][0-3])(\s{0,1})(AM|PM|am|pm|aM|Am|pM|Pm{2,2})$|([0-1][0-9]|[2][0-3]):([0-5][0-9])|([0-9]|[0-1][0-9]|[2][0-3])(:|\s)([0-5][0-9])|([0-12]\s{0,1}(AM|PM|am|pm|aM|Am|pM|Pm|p[.]m[.]{2}))|[0-9]\s(p.m.|a.m.)'

# dates_reg [ matches 01/01/2001 | 1/1/2001 | 01/1/01,
# matches DD-Month-YY            #
dates_reg = [r'(([1-9])|(0[1-9])|(1[0-2]))\/((0[1-9])|([1-31]))\/((\d{2})|(\d{4}))',
             r'([0-3][0-9]|[0-9])-((?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Sept|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?))-([0-9][0-9])']

sentence_reg = r'[A-Z][^\.!?]*'


def extract_topic_tag(text):
    for line in text:
        if line.__contains__("Topic:"):
            topic_line = line.split("Topic")[1]  # todo include multi-lines (until new tag starts)
        elif line.__contains__("Type:"):
            type_line = line.split("Type:")[1]
    return topic_line, type_line


def find_sentences(para):
    ret = re.findall(sentence_reg, para)
    filters = ["", " ", "\t", "\n"]
    filtered_ret = []
    for each in ret:
        if each not in filters:
            filtered_ret.append(each)
    ret = filtered_ret
    tagged_ret = []
    for each in ret:
        tagged_ret.append(f"<sentence>{each}</sentence>")
    ret = tagged_ret
    import final_assignment.misc_functions as m

    return m.concat(ret)


def find_paras(text):
    poss_paras = re.split(r'\n\n', text)
    primary_filters = [' ', '-- ', '']
    f_poss_paras = []
    for para in poss_paras:
        if not primary_filters.__contains__(para):
            f_poss_paras.append(para)
    filters = ["WHEN:", "WHERE:", "SPEAKER", "TITLE:", "WHO:", "HOST"]
    filtered_paras = f_poss_paras
    for f in filters:
        filtered_paras = (list(filter(lambda x: f not in x, filtered_paras)))

    return filtered_paras


def find_dates(text):
    dates = []
    for expr in dates_reg:
        extract = re.findall(expr, text)
        if extract:
            dates.append(extract)

    return dates


def find_times(text):
    # find_times_with_tag(text)
    times = []
    extract = re.findall(time_reg, text)
    if extract:
        times.append(extract)
    try:
        ret = sorted(times, key=lambda x: len(x), reverse=True)
        return flatten_list(ret[0])
    except:
        return []


def find_times_with_tag(text):
    ret = []
    for line in text:
        if line.__contains__("Time:"):
            ret.append(find_times(line))
    return flatten_list(ret[0])
    # r = r"(Time:(.*$))"
    #
    # print(re.findall(r, text, re.MULTILINE))


def find_dates_with_tag(text):
    ret = []
    for line in text:
        # line = line.lower()
        if line.__contains__("Date:"):
            ret.append(find_dates(line))
        elif line.__contains__("Dates:"):
            ret.append(find_dates(line))
        elif line.__contains__("When:"):
            ret.append(find_dates(line))
        elif line.__contains__("WHEN:"):
            ret.append(find_dates(line))
        elif line.__contains__("DATE:"):
            ret.append(find_dates(line))
        elif line.__contains__("DATES:"):
            ret.append(find_dates(line))

    return flatten_list(ret[0])


def find_locations(text, locations):
    locations_occurring = []
    for location in locations:
        if text.__contains__(location):
            locations_occurring.append((location, text.count(location)))
    names_occurring_sorted = sorted(locations_occurring, key=lambda x: x[1])
    if locations_occurring:
        return names_occurring_sorted[0]
    else:
        return None


def find_speakers(text, speakers):
    names_occurring = []
    for speaker in speakers:
        if text.__contains__(speaker):
            names_occurring.append((speaker, text.count(speaker)))
    names_occurring_sorted = sorted(names_occurring, key=lambda x: x[1])
    if names_occurring:
        return names_occurring_sorted[0]
    else:
        return None


def find_speakers_with_tag(text, speakers):
    ret = []
    flag = None
    for line in text:
        if line.__contains__("Who:"):
            flag = "w"
            ret.append(line)
        elif line.__contains__("Speaker:"):
            flag = "w"
            ret.append(line)
        elif line.__contains__("SPEAKER:"):
            flag = "w"
            ret.append(line)
        elif line.__contains__("WHO:"):
            flag = "w"
            ret.append(line)

    if flag == "w":
        title_list = ['dr.', 'dr', 'mr', 'professor', 'mr.', 'mrs.', 'mrs', 'ms.', 'ms']
        ret_list = ret[0].split(" ")
        t = []
        for each in ret_list:
            if each != '':
                t.append(each)
        ret_list = t
        ret_list = ret_list[1:]
        if title_list.__contains__(str.lower(ret_list[0])):
            return ret_list[0] + " " + ret_list[1] + " " + ret_list[2]
        else:
            return ret_list[0] + " " + ret_list[1]
    else:
        return find_speakers(text, speakers)


def find_locations_with_tag(text, locations):
    ret = []
    for line in text:
        if line.__contains__("Location:"):
            ret.append(line)
        elif line.__contains__("Place:"):
            ret.append(line)
    try:
        ret_list = ret[0].split(" ")
        t = []
        for each in ret_list:
            if each != '':
                t.append(each)
        ret_list = t
        ret_list = ret_list[1:]
        ret = ""
        for each in ret_list:
            ret += " " + each
        return ret
    except:
        return find_locations(text, locations)
