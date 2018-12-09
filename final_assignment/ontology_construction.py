import multiprocessing as mp

import final_assignment.ontology as o
import final_assignment.seminar_data_extractor as extractor

emails = extractor.get_untagged()


def tag(e):
    return e.tag_all()


with mp.Pool() as pool:
    emails = pool.map(tag, emails)
    print("finished tagging")

ontology = o.Ontology()
for email in emails:
    # email.tag_all()
    ontology.add_to(email.get_header().topic, email.fileid)


print(ontology)
ontology.save_pop()
