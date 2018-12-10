# todo check count FN
import random

import nltk


def generate_file_ids(s, e):
    ret = []
    for i in range(s, e):
        ret.append(str(i) + ".txt")
    return ret


import re


def strip_other_tags(tags, line, excl):
    for tag in tags:
        # if tag != excl:
        line = re.sub(f'{tag[1]}', '', re.sub(f'{tag[0]}', '', line))
    return line


def extract_tags(line):
    tags = [("<sentence>", "</sentence>"), ("<paragraph>", "</paragraph>"), ("<speaker>", "</speaker>"),
            ("<location>", "</location>"), ("<stime>", "</stime>"), ("<etime>", "</etime>")]
    # tags = [("<speaker>", "</speaker>"),
    #         ("<location>", "</location>"), ("<stime>", "</stime>"), ("<etime>", "</etime>")]
    # tags = [("<speaker","</speaker>")]
    # tags = [("<location>", "</location>")]
    # tags = [("<stime>", "</stime>"), ("<etime>", "</etime>")]
    tagged_items = []
    for tag in tags:
        r = f"{tag[0]}.*?{tag[1]}"
        l = re.findall(r, line, re.DOTALL)
        for each in l:
            tagged_items.append(strip_other_tags(tags, each, tag))
    import final_assignment.misc_functions as m
    m.flatten_list(tagged_items)
    ret = []
    for each in tagged_items:
        for item in each:
            ret.append(item)
    de_tagged = []
    # for each in ret:
    #     de_tagged.append(strip_other_tags(tags, each))

    return tagged_items


def count_all(generated, reference):
    tp_g = 0
    fp = 0
    tp_r = 0
    false_negatives = []
    false_positives = []
    true_positives = []
    # for line_g, line_r in zip(generated, reference):
    tagged_items_g = list(set(extract_tags(generated)))

    tagged_items_r = list(set(extract_tags(reference)))
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
            tp_g += 1
            true_positives.append(item)
        else:
            fp += 1
            false_positives.append(item)

    for item in tagged_items_r:
        if item not in tagged_items_g:
            tp_r += 1
            false_negatives.append(item)

    # print(f"FP: {false_positives} \n FN: {false_negatives}")
    return tp_g + 1, len(tagged_items_g) + 1, len(tagged_items_r) + 1


def calc_TP_FP(file_id):
    path = f"/home/sam/nltk_data/corpora/seminar_test_data/test_tagged/{file_id}"
    email_r = nltk.data.load(path, format='text')
    email_r = re.sub("\n\n", "", email_r).split("\n")
    path = f"../data/generated/{file_id}"
    email_g = nltk.data.load(path, format='text')
    email_g = email_g.split("\n")
    import final_assignment.misc_functions as m
    email_g_string = m.concat(email_g).replace(" ", "")
    email_r_string = m.concat(email_r).replace(" ", "")
    email_g_string.replace("<date>", "").replace("</date>", "")
    return count_all(email_g_string, email_r_string)


def interpret(fs, title, sorted_flag):
    import statistics as s
    # import scipy.stats as s
    average = sum([pair[0] for pair in fs]) / (len(fs))
    try:
        mode = s.mode(pair[0] for pair in fs)
    except:
        strip_fs = [pair[0] for pair in fs]
        mode = sorted(strip_fs, key=strip_fs.count, reverse=True)[0]

    import matplotlib.pyplot as plt
    if not sorted_flag:
        random.shuffle(fs)
    ys, xs = zip(*fs)
    fig = plt.figure()
    plot = fig.add_subplot(1, 1, 1)
    av = plot.axhline(y=average, color='r', linestyle='dotted', label="Mean")
    mod = plot.axhline(y=mode, color='b', linestyle='dotted', label="Modal")
    plot.legend((av, mod), ('Mean = ' + str(average)[:4], 'Mode = ' + str(mode)[:4]))
    plot.scatter(x=xs, y=ys, marker="x")
    plot.set_title(title)
    plot.set_ylabel("F Measure")
    plot.set_xlabel("File")
    fig.savefig(f"../data/generated/plots/{title}")

    plt.show()


if __name__ == '__main__':

    # def f_measure():
    # Precision(P) = TP / (TP + FP)
    # Recall (R) = TP / (TP + FN)
    # F = 1/((a)(1/P) + (1-a)(1/R))
    #       a is importance of recall over precision
    ids = generate_file_ids(301, 484)
    fs = []
    pr = []
    ps = []
    rs = []
    banned = ["328.txt",
              "344.txt",
              "377.txt",
              "398.txt",
              "407.txt",
              "410.txt",
              "415.txt",
              "440.txt",
              "443.txt",
              "444.txt",
              "445.txt",
              "446.txt",
              "447.txt",
              "450.txt",
              "463.txt",
              "472.txt",
              "474.txt",
              "476.txt"]
    banned = []
    for _id in ids:
        if _id not in banned:
            tp_g, c_g, tp_r = calc_TP_FP(_id)

            try:
                p = tp_g / c_g
            except:
                p = 0
            try:
                r = tp_g / tp_r
            except:
                r = 0

            try:

                f = 2 * ((p * r) / (p + r))
            except:
                print(f)
                f = 0
            if f is 0:
                print(_id)
            # print(tp,fp,fn)
            fs.append((f, _id))
            pr.append(((p * r), (p + r)))
            ps.append(p)
            rs.append(r)
        # print(f"For {_id} Precision  = {p}, \n Recall = {r} \n F measure = {f}")
        # print(f, _id)
    print(ps)
    print(rs)
    sorted_fs = sorted(fs, key=lambda x: x[0])
    # sorted_fs = fs.sort(key=lambda x : x[0])
    sorted_pr = sorted(pr, key=lambda x: x[0])
    # interpret(sorted_pr, "Precision*Recall against Precision+Recall", True)

    interpret(sorted_fs, "Sorted all values", True)
    interpret(sorted_fs[3:], "Sorted minus outliers", True)
    interpret(sorted_fs[3:], "Unsorted minus outliers", False)
    interpret(sorted_fs, "Unsorted all values", False)
    import statistics as s

    mean_f = sum([pair[0] for pair in fs]) / (len(fs))
    try:
        mode_f = s.mode(pair[0] for pair in fs)
    except s.StatisticsError:
        strip_fs = [pair[0] for pair in fs]
        mode_f = sorted(strip_fs, key=strip_fs.count, reverse=True)[0]

    maximum_f = max(
        pair[0] for pair in fs)
    minimum_f = min(pair[0] for pair in fs)

    mean_p = sum([item for item in ps]) / (len(pr))
    try:
        mode_p = s.mode(item for item in ps)
    except s.StatisticsError:
        # strip_ps = [pair[0] for pair in ps]
        mode_p = sorted(ps, key=ps.count, reverse=True)[0]

    maximum_p = max(
        item for item in ps)
    minimum_p = min(item for item in ps)

    mean_r = sum([item for item in rs]) / (len(rs))
    try:
        mode_r = s.mode(item for item in rs)
    except s.StatisticsError:
        # strip_rs = [pair[0] for pair in rs]
        mode_r = sorted(rs, key=rs.count, reverse=True)[0]

    maximum_r = max(
        item for item in rs)
    minimum_r = min(item for item in rs)
    print(
        f"""Mean f_measure = {mean_f} Maximum = {maximum_f} Minimum = {minimum_f} Modal value = {mode_f} \n 
            Mean Precision = {mean_p} Maximum = {maximum_p} Minimum = {minimum_p} Modal Value = {mode_p}
            Mean Recall = {mean_r} Maximum = {maximum_r} Minimum = {minimum_r} Modal Value = {mode_r}""")
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D

    Axes3D
    ys, xs = zip(*fs)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(ps, rs, ys)
    ax.set_xlabel("Precision")

    ax.set_zlabel("F measure")
    ax.set_ylabel("Recall")
    ax.set_title("Precision against Recall against F measure")
    fig.savefig("../data/generated/plots/3d")
    plt.show()
