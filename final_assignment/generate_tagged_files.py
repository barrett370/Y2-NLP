import final_assignment.seminar_data_extractor as extractor
import multiprocessing as mp

emails = extractor.get_untagged()


def tag(e):
    return e.tag_all()


if __name__ == '__main__':
    with mp.Pool() as pool:
        emails = pool.map(tag, emails)

    for email in emails:
        print(email)
        f = open(f"../data/generated/{str(email.fileid)}", "w+")
        tagged_header = '\n'.join(map(str, email.header.tagged_header))
        tagged_abstract = '\n'.join(map(str, email.abstract.tagged_abstract)) + "\n"

        f.write(str(tagged_header + "\n Abstract: \n" + str(tagged_abstract)))
