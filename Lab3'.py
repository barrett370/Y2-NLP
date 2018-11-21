from multiprocessing import Queue, Process

from nltk.corpus import brown

import Lab3
import seminar_data_parser

t = Lab3.tagger()
# /t.__init__()

words = seminar_data_parser.get_untagged()

tagged = t.tag(words)
for each in tagged:
    print(each)

# q = Queue()
# l = len(words)
# p1 = Process(target=t.tag, args=(q, words[:(l / 4)]))
# p2 = Process(target=t.tag, args=(q, words[(l / 4) + 1:(2 * l) / 4]))
# p3 = Process(target=t.tag, args=(q, words[((2 * l) / 4) + 1:(3 * l) / 4]))
# p4 = Process(target=t.tag, args=(q, words[((3 * l) / 4) + 1:l]))
# p1.start()
# p2.start()
# p3.start()
# p4.start()
# r1 = q.get()
# r2 = q.get()
# r3 = q.get()
# r4 = q.get()
# print(r1 + r2 + r3 + r4)
