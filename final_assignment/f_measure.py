# todo check count FN
import re

import nltk


def generate_file_ids(s, e):
    ret = []
    for i in range(s, e):
        ret.append(str(i) + ".txt")
    return ret


def extract_tags(line):
    tags = [("<sentence>", "</sentence>"), ("<paragraph>", "</paragraph>"), ("<speaker>", "</speaker>"),
            ("<location>", "</location>"), ("<stime>", "</stime>"), ("<etime>", "</etime>")]
    tagged_items = []
    for tag in tags:
        r = f"{tag[0]}.*?{tag[1]}"
        tagged_items.append(re.findall(r, line))
    import final_assignment.misc_functions as m
    m.flatten_list(tagged_items)
    ret = []
    for each in tagged_items:
        for item in each:
            ret.append(item)
    return ret


def count_TP(generated, reference):
    tp = 0
    fp = 0
    fn = 0
    false_negatives = []
    false_positivies = []
    # for line_g, line_r in zip(generated, reference):
    tagged_items_g = extract_tags(generated)
    tagged_items_r = extract_tags(reference)
    fil_g = []
    for each in tagged_items_g:
        if each:
            fil_g.append(each)
    fil_r = []
    for each in tagged_items_r:
        if each:
            fil_r.append(each)
    tagged_items_g = fil_g
    tagged_items_r = fil_r

    for item in tagged_items_g:
        if item in tagged_items_r:
            tp += 1
        else:
            fp += 1
            false_positivies.append(item)
    for item in tagged_items_r:
        if item not in tagged_items_g:
            fn += 1
            false_negatives.append(item)

    # print(f"FP: {false_positivies} \n FN: {false_negatives}")
    return tp, fp, fn


def calc_TP_FP(file_id):
    path = f"../data/seminar_testdata/test_tagged/{file_id}"
    email_r = nltk.data.load(path, format='text')
    email_r = re.sub("\n\n", "", email_r).split("\n")
    path = f"../data/generated/{file_id}"
    email_g = nltk.data.load(path, format='text')
    email_g = email_g.split("\n")
    import final_assignment.misc_functions as m
    email_g_string = m.concat(email_g).replace(" ", "")
    email_r_string = m.concat(email_r).replace(" ", "")
    return count_TP(email_g_string, email_r_string)


def f_measure():
    # Precision(P) = TP / (TP + FP)
    # Recall (R) = TP / (TP + FN)
    # F = 1/((a)(1/P) + (1-a)(1/R))
    #       a is importance of recall over precision
    ids = generate_file_ids(301, 485)
    fs = []
    for _id in ids:
        tp, fp, fn = calc_TP_FP(_id)
        p = tp / (tp + fp)
        r = tp / (tp + fn)
        a = 0.5
        try:
            f = 1 / (a * (1 / p) + (1 - a) * (1 / r))
        except:
            f = 0
        # print(tp,fp,fn)
        fs.append((f, _id))
        print(f, _id)
    import statistics as s
    average = sum([pair[0] for pair in fs]) / (485 - 301)
    mode = s.mode(pair[0] for pair in fs)
    maximum = max(
        pair[0] for pair in fs)
    minimum = min(pair[0] for pair in fs)
    print(f"""Average f_measure = {average} Maximum = {maximum} Minimum = {minimum} Modal value = {mode}""")
    import matplotlib.pyplot as plt
    ys, xs = zip(*fs)
    plt.scatter(x=xs, y=ys, marker="x")

    # plt.axhline(y=average,xmin="300.txt",xmax="348.txt")
    plt.hlines(y=average, xmin="300.txt", xmax="485.txt", linestyles='dotted', label="average")
    plt.plot("400.txt", average, color="red", label="Average")
    plt.plot("490.txt", maximum, color="red", label="max")
    plt.show()


f_measure()
