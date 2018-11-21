import re

import final_assignment.seminar_data_extractor as extractor
import final_assignment.tokenize_and_tag as tagger
#
# print(extractor.get_tagged())
# print(extractor.get_untagged())
#
# print(extractor.get_untagged_abstract())
# print(type(extractor.get_untagged_abstract()))
# print(len(extractor.get_untagged_abstract()))
# for each in extractor.get_untagged_abstract():
#     print(each)
# tokenizer = tagger.Tagger()
# # print(tokenizer.tag(extractor.get_untagged_abstract()))
#
# for line in extractor.get_untagged_abstract():
#
#     word_line = line.split(" ")
#     try:
#         word_line.remove("\t")
#     except:
#         pass
#     words = []
#     for word in word_line:
#         words.append(re.sub('[^A-Za-z0-9]+', '', word))
#     try:
#         words.remove('')
#     except:
#         pass
#
#     # print(words)
#     print(tokenizer.tag(words))
import final_assignment.regex_tagger as rtagger

emails = extractor.get_untagged()
print(len(emails))
for header in emails:
    dates_found = rtagger.find_dates(extractor.flatten(header.get_header().get_untagged_header()))
    try:
        header.get_header().set_date(dates_found[0])
    except:
        header.get_header().set_date(None)
    print(dates_found)

    header.get_header().analyse_times()

    # times_found = rtagger.find_times(extractor.flatten(header.get_header().get_untagged_header()))
    # header.times = times_found
    # header.dates = dates_found
