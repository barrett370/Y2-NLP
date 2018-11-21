import final_assignment.seminar_data_extractor as extractor

import re


def setify(xs):
    ret = []
    for x in xs:
        if not ret.__contains__(x):
            ret.append(x)
    return ret


def strip_tags(l):
    ret = []
    for entry in l:
        if "</sentence>" in entry:
            ret.append(entry[:entry.index("</sentence>"):])
        else:
            ret.append(entry)
    return ret


def extract_entities():
    """

    :rtype: speakers, locations
    """
    locations = []
    speakers = []
    tagged_data = extractor.get_tagged_EE()
    location_re = r'<location>(.*?)</location>'
    speaker_re = r'<speaker>(.*?)</speaker>'
    flat_data = extractor.flatten(tagged_data)
    locations.append(re.findall(location_re, flat_data))
    speakers.append(re.findall(speaker_re, flat_data))
    locations_set = setify(locations[0])
    speakers_set = setify(speakers[0])
    locations_final = strip_tags(locations_set)
    return speakers_set, locations_final
