import re

# for header
# time_reg [ matches [0-12] + (0|1 * \s) + PM|AM|pm|am (12hr clock) ,
#           matches 24hr clock

time_reg = [
    r'(([0-9]|[0-1][0-9]|[2][0-3]):([0-5][0-9])(\s{0,1})(AM|PM|am|pm|aM|Am|pM|Pm{2,2})$)|(^([0-9]|[1][0-9]|[2][0-3])(\s{0,1})(AM|PM|am|pm|aM|Am|pM|Pm{2,2}))',
    r'([0-1][0-9]|[2][0-3]):([0-5][0-9])']

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


def find_times(text):
    times = []
    for expr in time_reg:
        extract = re.findall(expr, text)
        if extract:
            times.append(extract)
    return times
