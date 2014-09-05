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
        t
        ([1-3]) # number 1,2, or 3 in 'term'.
        .y
        (\d{4}) # exactly four digits in 'year'.
        .s
        (\d{3}) # exactly three digits in 'section'.
        .c
        (\D)    # exactly one letter in 'prefix'.
        (\d{4}) # exactly four digits in 'course_number'.
        .
        (\D{4}) # exactly four letters in 'department_code'.
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


def parse_pamacea_string(s):
    pattern = re.compile(
        r"""
        CUcourse_
        (\D{4}) # exactly four letters in 'department_code'.
        (\D)    # exactly one letter in 'prefix'.
        (\d{4}) # exactly four digits in 'course_number'.
        _
        (\d{3}) # exactly three digits in 'section'.
        _
        (\d{4}) # exactly four digits 'year'.
        _
        ([1-3]) # number 1,2, or 3 in 'term'.
        """, re.VERBOSE)

    t = pattern.search(s).groups()
    return dict(
        term=TERMS[int(t[5]) - 1],
        year=int(t[4]),
        section_number=t[3],
        course_prefix_letter=t[1],
        course_number=int(t[2]),
        department_id=t[0],
        )



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
