Simple library for generating and parsing CU affil
strings (as returned by WIND/CAS).

Doing documentation-driven development here.

Generating:

    >>> from cuaffils import generate_wind_string
    >>> d = dict(
    >>>     term='fall',
		>>> 		year=2014,
		>>> 		section_number='001',
		>>> 		course_prefix_letter='N',
		>>> 		course_number=6610,
		>>> 		department_id='NURS'
		>>> )
    >>> print(generate_wind_string(**d))
    t3.y2014.s001.cN6610.NURS.st.course:columbia.edu
    >>> print(generate_pamacea_string(**d))
    CUcourse_NURSN6610_001_2008_3
    >>> print(generate_course_directory_string(**d))
    20083NURS6610N001

Parsing:

    >>> from cuaffils import parse_wind_string
    >>> d = parse_wind_string('t3.y2014.s001.cN6610.NURS.st.course:columbia.edu')
    >>> print(d['term'])
    fall
    >>> print(d['department_id'])
    NURS
    ... etc ..
    >>> from cuaffils import parse_pamacea_string
    >>> d = parse_pamacea_string('CUcourse_NURSN6610_001_2008_3')
    ... same dict as response ...
    >>> from cuaffils import parse_course_directory_string
    >>> d = parse_course_directory_string('20083NURS6610N001')
    >>> same dict as response ...
