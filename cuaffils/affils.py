import re
TERMS = ['spring', 'summer', 'fall']

def generate_wind_string(**kwargs):
    fields = kwargs
    fields['term'] = TERMS.index(fields['term']) + 1
    return (
        "t%(term)d.y%(year)04d.s%(section_number)s.c"
        "%(course_prefix_letter)s%(course_number)04d.%(department_id)s"
        ".st.course:columbia.edu" % fields)


def parse_wind_string(s):
    pattern = re.compile(
        r"""
        t #starts with t (which stands for term)
        ([1-3]) #number 1,2, or 3 in group 0 'term'.
        .y #.y comes next for year
        (\d{4}) #exactly four digits in group 1 'year'.
        .s
        (\d{3}) #exactly three digits in group 2 'section'.
        .c
        (\D) #exactly one letter in group 3 'prefix'.
        (\d{4}) #exactly four digits in group 4 'course_number'.
        .
        (\D{4}) #exactly four letters in group 5 'department_code'.
        #the rest of the string does not matter.
        """, re.VERBOSE)

    t = pattern.search(s).groups()
    return dict(
        term=TERMS[int(t[0]) - 1],
        year=int(t[1]),
        section_number=t[2],
        course_prefix_letter=t[3],
        course_number=int(t[4]),
        department_id=t[5],
        )


def generate_pamacea_string(**kwargs):
    fields = kwargs
    fields['term'] = TERMS.index(fields['term']) + 1
    return (
        "CUcourse_%(department_id)s"
        "%(course_prefix_letter)s"
        "%(course_number)04d_"
        "%(section_number)s_"
        "%(year)04d_%(term)d" % fields)


def parse_pamacea_string():
    pass


def generate_course_directory_string(**kwargs):
    fields = kwargs
    fields['term'] = TERMS.index(fields['term']) + 1
    return (
        "%(year)04d"
        "%(term)d"
        "%(department_id)s"
        "%(course_number)04d"
        "%(course_prefix_letter)s"
        "%(section_number)s" % fields)


def parse_course_directory_string():
    pass
