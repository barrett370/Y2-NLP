def concat(l):
    ret = ""
    for each in l:
        if type(l) == list:
            ret += " " + concat(each)
        else:
            ret += each
    return ret


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