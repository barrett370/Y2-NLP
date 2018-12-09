import re
from nltk.sem import relextract
from nltk.corpus import ieer

IN = re.compile(r'.*\bin\b(?!\b.+ing\b)')

for fileid in ieer.fileids():
    for doc in ieer.parsed_docs(fileid):
        for rel in relextract.extract_rels('ORG', 'LOC', doc, corpus='ieer', pattern=IN):

            ret = relextract.rtuple(rel)
            print(ret)

