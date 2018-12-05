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
import final_assignment.seminar_data_extractor as extractor

emails = extractor.get_untagged()
for email in emails:
    # email.get_header().analyse()
    # print(email.get_header())
    # print(str(email.get_abstract().get_untagged_abstract()))
    # print(email.get_header().find_possible_speakers())
    # print(email.get_abstract())
    import final_assignment.regex_tagger as rt
    import final_assignment.misc_functions as m

    # print(rt.find_sentences(rt.find_paras(m.concat(email.get_abstract().get_untagged_abstract()))))
    email.tag_all()
    print(email)
    # email.get_abstract().analyse(email.get_header())
