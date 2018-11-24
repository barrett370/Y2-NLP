import re

# for header
# time_reg [ matches [0-12] + (0|1 * \s) + PM|AM|pm|am (12hr clock) ,
#           matches 24hr clock

# time_reg = [
#     r'([0-9]|[0-1][0-9]|[2][0-3])(:|\s)([0-5][0-9])(\s{0,1})(AM|PM|am|pm|aM|Am|pM|Pm{2,2})|(([0][0-9]|[1][0-9]|[2][0-3])(\s{0,1})(AM|PM|am|pm|aM|Am|pM|Pm{2,2}))$',
#     r'([0-1][0-9]|[2][0-3]):([0-5][0-9])',
#     r'([0-9]|[0-1][0-9]|[2][0-3])(:|\s)([0-5][0-9])$']
time_reg = r'([0-9]|[0-1][0-9]|[2][0-3])(:|\s)([0-5][0-9])(\s{0,1})(AM|PM|am|pm|aM|Am|pM|Pm{2,2})|([0][0-9]|[1][0-9]|[2][0-3])(\s{0,1})(AM|PM|am|pm|aM|Am|pM|Pm{2,2})$|([0-1][0-9]|[2][0-3]):([0-5][0-9])|([0-9]|[0-1][0-9]|[2][0-3])(:|\s)([0-5][0-9])|([0-12]\s{0,1}(AM|PM|am|pm|aM|Am|pM|Pm|p[.]m[.]{2}))|[0-9]\s(p.m.|a.m.)'

# dates_reg [ matches 01/01/2001 | 1/1/2001 | 01/1/01,
# matches DD-Month-YY            #
dates_reg = [r'(([1-9])|(0[1-9])|(1[0-2]))\/((0[1-9])|([1-31]))\/((\d{2})|(\d{4}))',
             r'([0-3][0-9]|[0-9])-((?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Sept|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?))-([0-9][0-9])']


def find_dates(text):
    dates = []
    for expr in dates_reg:
        extract = re.findall(expr, text)
        if extract:
            dates.append(extract)

    return dates


def flatten_list(l):
    """
    function to take regex results of multiple regex and combine them into a single array
    :param l: list to be flattened
    """
    ret = []
    for each in l:
        if type(each) == list:
            ret.append(flatten_list(each))
        else:
            ret.append(each)
    return ret


def find_times(text):
    # find_times_with_tag(text)
    times = []
    extract = re.findall(time_reg, text)
    if extract:
        times.append(extract)

    return flatten_list(times[0])


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
        if line.__contains__("Date:"):
            ret.append(find_dates(line))
        elif line.__contains__("Dates:"):
            ret.append(find_dates(line))

    return flatten_list(ret[0])


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


# def remove_spaces(string):
#     string_list = list(string)
#     ret_string = ""
#     for char in string_list:
#         if char != '\t':
#             ret_string += char
#     return ret_string


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
        return None
