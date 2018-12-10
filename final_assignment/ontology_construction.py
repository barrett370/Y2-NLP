import multiprocessing as mp

import final_assignment.ontology as o
import final_assignment.seminar_data_extractor as extractor

emails = extractor.get_untagged()
ontology = o.Ontology()


def tag(e):
    return e.tag_all()


with mp.Pool() as pool:
    emails = pool.map(tag, emails)
    print("finished tagging")


def ext():
    # ret_h = []
    # ret_f = []
    ret = []
    for email in emails:
        ret.append((email.get_header().topic,email.fileid))
        # ret_f.append(email.fileid)
    return ret
import itertools

def add_helper(args):
    return ontology.add_to(*args)

with mp.Pool() as pool:
    l = ext()
    pool.map(add_helper, l)
# for email in emails:
#     # email.tag_all()
#     ontology.add_to(email.get_header().topic, email.fileid)


print(ontology)
ontology.save_pop()
