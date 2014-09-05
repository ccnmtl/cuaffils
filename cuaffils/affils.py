TERMS = ['spring', 'summer', 'fall']

def generate_wind_string(**kwargs):
    fields = kwargs
    fields['term'] = TERMS.index(fields['term']) + 1
    return (
        "t%(term)d.y%(year)04d.s%(section_number)s.c"
        "%(course_prefix_letter)s%(course_number)04d.%(department_id)s"
        ".st.course:columbia.edu" % fields)


def parse_wind_string():
    pass


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
