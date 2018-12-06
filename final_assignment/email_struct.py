import datetime
import re

import final_assignment.regex_tagger as rtagger


def generate_date_perms(norm_date):
    poss_dates = [datetime.datetime.strptime(norm_date, '%d-%m-%y').strftime('%B %d,%Y'),
                  datetime.datetime.strptime(norm_date, '%d-%m-%y').strftime('%b %d')]
    t = datetime.datetime.strptime(norm_date, '%d-%m-%y').strftime('%d-%b-%y')
    poss_dates.append(t)
    if t[0] == "0":
        poss_dates.append(t[1:])

    poss_dates.append(norm_date)
    return poss_dates


def generate_time_perms(norm_time):
    poss_times = [norm_time]
    t = datetime.datetime.strptime(norm_time, '%H:%M').strftime('%I:%M %p')
    poss_times.append(re.sub("PM", "pm", t))
    poss_times.append(re.sub("PM", "p.m.", t))
    poss_times.append(re.sub("PM", "p.m", t))
    poss_times.append(re.sub("AM", "am", t))
    poss_times.append(re.sub("AM", "a.m.", t))
    poss_times.append(re.sub("AM", "a.m", t))
    poss_times.append(t)

    if t[0] == "0":
        poss_times.append(t[1:])
    t = datetime.datetime.strptime(norm_time, '%H:%M').strftime('%I:%M%p')
    poss_times.append(t)
    poss_times.append(re.sub("PM", "pm", t))
    poss_times.append(re.sub("PM", "p.m.", t))
    poss_times.append(re.sub("PM", "p.m", t))
    poss_times.append(re.sub("AM", "am", t))
    poss_times.append(re.sub("AM", "a.m.", t))
    poss_times.append(re.sub("AM", "a.m", t))

    if t[0] == "0":
        poss_times.append(t[1:])
    t = datetime.datetime.strptime(norm_time, '%H:%M').strftime('%I:%M')
    poss_times.append(t)
    if t[0] == "0":
        poss_times.append(t[1:])
    return reversed(sorted(poss_times, key=len))


class Email:
    def __init__(self, header, abstract, fileid):
        self.header = header
        self.abstract = abstract
        self.fileid = fileid

    def get_header(self):
        return self.header

    def get_abstract(self):
        return self.abstract

    def tag_all(self):
        self.header.analyse()
        self.tag_header()
        self.tag_abstract()
        return self

    def tag_header(self):
        lines = self.header.get_untagged_header()
        tagged_header = self.tag_text(lines)
        self.header.set_tagged_header(tagged_header)

    def tag_abstract(self):

        # paras = rtagger.find_paras(self.abstract.get_untagged_abstract())
        # sents = rtagger.find_sentences(paras)

        lines = self.abstract.get_untagged_abstract().split("\n\n")

        lines_filtered = []
        filters = ['', ' ', '-- ']
        for line in lines:
            if line not in filters:
                lines_filtered.append(line)
        lines = lines_filtered
        para_lines = []
        tags = ["WHO:", "WHERE:", "WHEN:", "HOST", "TITLE:", "APPOINTMENT:", "Host:", "Appointment:", "Who:", "Where:",
                "DATE:", "TIME:", "PLACE:", "TOPIC:", "REMINDER:","SPEAKER"]

        for line in lines:
            if not any(ext in line.upper() for ext in tags):
                sents = rtagger.find_sentences(line)
                if sents != "":
                    para_lines.append(f"<paragraph>{sents}</paragraph>")
                else:
                    para_lines.append(f"<paragraph>{line}</paragraph>")
            else:
                para_lines.append(line)
        lines = para_lines
        tagged_abstract = self.tag_text(lines)

        self.abstract.tagged_abstract = tagged_abstract

    def tag_text(self, lines):
        tagged_text = []
        for line in lines:
            try:
                line = re.sub("(" + self.header.speaker + ")", f"<speaker>{self.header.get_speaker()}</speaker>", line)
            except:
                pass
            try:
                for time in generate_time_perms(self.header.start_time):
                    oline = line
                    line = re.sub(r'(' + str(time) + ")", f"<stime>{time}</stime>",
                                  line)
                    if oline != line:
                        break
            except:
                pass
            try:
                for time in generate_time_perms(self.header.end_time):
                    oline = line
                    line = re.sub(r'(' + str(time) + ")", f"<etime>{time}</etime>", line)
                    if oline != line:
                        break
            except:
                pass
            try:
                for date in generate_date_perms(self.header.date):
                    oline = line
                    line = re.sub(r'(' + str(date) + ")", f"<date>{str(date)}</date>", line)
                    if oline != line:
                        break
            except:
                pass
            try:
                line = re.sub(r'(' + str(self.header.location) + ")", f"<location>{self.header.location}</location>",
                              line)
            except:
                pass
            tagged_text.append(line)
        return tagged_text

    def __str__(self) -> str:
        return f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n ID: {self.fileid} \n Header: \n  {self.header} \n Abstract: \n {self.abstract}"
