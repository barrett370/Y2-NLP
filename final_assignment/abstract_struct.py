import final_assignment.regex_tagger as rtagger
import final_assignment.training_entity_extraction as tee
from final_assignment.misc_functions import twelve_to_twenty_four


class Abstract:

    def __init__(self, abstract):
        self.untagged_abstract = abstract
        self.tagged_abstract = None
        self.paras = None
        self.sents = None

    def get_untagged_abstract(self):
        return self.untagged_abstract

    def __str__(self) -> str:
        tagged_abstract = '\n'.join(map(str, self.tagged_abstract)) + "\n"

        return f"Tagged: \n {tagged_abstract} \n "

    def analyse(self, header):  # only bothers finding data for tags that haven't been found in the header
        if header.get_date() is None:
            self.analyse_date()
        if header.get_location() is None:
            location = self.analyse_location()
            if location is not None:
                header.location = location
                # print("Changed location " + str(header.location))
        # stime, etime = header.get_times()
        if header.start_time is None:
            stime = self.analyse_time(header)[0]
            if stime is not None:
                header.start_time = stime
                # print("Changed stime " + str(header.start_time))
        if header.end_time is None:
            etime = self.analyse_time(header)[1]
            if etime is not None:
                header.end_time = etime
                # print("Changed etime " + str(header.end_time))

        if header.speaker is None:
            speaker = self.analyse_speaker()
            if speaker is not None:
                header.speaker = speaker
                # print("Changed Speaker " + str(header.speaker))

    def analyse_paras(self):
        self.paras = rtagger.find_paras(self.untagged_abstract)

    def analyse_sents(self):
        self.sents = rtagger.find_sentences(self.paras)

    def analyse_location(self):

        _, locations = tee.extract_entities()
        try:
            return rtagger.find_locations(self.untagged_abstract, locations)[0]
        except:
            return None

    def analyse_speaker(self):
        speakers, _ = tee.extract_entities()
        speaker = rtagger.find_speakers_with_tag(self.get_untagged_abstract(), speakers)
        if speaker:
            speaker = speaker[0]
        import re
        speaker_r = None
        if speaker is not None:
            speaker_r = re.sub(r'[^\w\s]', '', speaker)
        return speaker_r

    def analyse_time(self, header):
        end_time = None
        times_found = rtagger.find_times_with_tag(header.get_untagged_header())
        formal_times = []
        for time in times_found:
            formal_times.append(twelve_to_twenty_four(time))
        if len(formal_times) == 1:  # only start time present
            start_time = (str(formal_times[0][0]) + ":" + str(formal_times[0][1]))
        else:  # decide which is start / which is end
            current_lowest = (25, 61)
            for time in formal_times:
                if int(time[0]) < int(current_lowest[0]):
                    current_lowest = time
                elif int(time[0]) == int(current_lowest[0]):
                    if int(time[1]) < int(current_lowest[1]):
                        current_lowest = time
            start_time = str(current_lowest[0]) + ":" + str(current_lowest[1])

            current_highest = (00, 00)
            for time in formal_times:
                if int(time[0]) > int(current_highest[0]):
                    current_highest = time
                elif int(time[0]) == int(current_highest[0]):
                    if int(time[1]) > int(current_highest[1]):
                        current_highest = time
            end_time = str(current_highest[0]) + ":" + str(current_highest[1])
        return start_time, end_time

    def analyse_date(self):
        pass
