def flatten_to_string(l):
    ret = ""
    for each in l:
        if type(l) == list:
            ret += " " + flatten_to_string(each)
        else:
            ret += each
    return ret