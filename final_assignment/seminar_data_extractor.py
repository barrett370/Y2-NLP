import nltk
from nltk.corpus import WordListCorpusReader

from final_assignment import email_struct, header_struct, abstract_struct


def generate_file_ids(s, e):
    ret = []
    for i in range(s, e):
        ret.append(str(i) + ".txt")
    return ret


def get_untagged():
    # ids = generate_file_ids(301, 485)
    # reader = WordListCorpusReader('../data/seminar_testdata/test_untagged', ids)

    ids = generate_file_ids(301, 485)
    base_path = "/home/sam/nltk_data/corpora/seminar_test_data/test_untagged"
    from os import listdir

    from os.path import isfile, join
    # files = [f for f in listdir(base_path) if isfile(join(base_path, f))]
    reader = WordListCorpusReader(base_path, ids)
    ret = []

    for file_id in ids:
        path = f"{base_path}/{file_id}"
        # path = f"../data/seminar_testdata/test_untagged/{id}"

        emails = reader.words(file_id)
        data = nltk.data.load(path, format='text')
        split_index = emails.index("Abstract: ")
        header = header_struct.Header(emails[:split_index])
        import final_assignment.misc_functions as m
        abstract = abstract_struct.Abstract(m.concat(data.split("Abstract:")[1]))
        emails = email_struct.Email(header, abstract, file_id)
        ret.append(emails)
    return ret


def get_untagged_abstract():
    emails = get_untagged()
    ret = []
    for email in emails:
        ret.append(email.get_abstract())

    return ret[0]


def get_tagged_POS():
    reader = WordListCorpusReader('../data/seminars_training/training', generate_file_ids(0, 300))
    return reader.words()


def get_tagged_EE():
    reader = WordListCorpusReader('../data/seminar_testdata/test_tagged', generate_file_ids(301, 485))
    return reader.words()


