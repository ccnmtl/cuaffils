[![Build Status](https://travis-ci.org/ccnmtl/cuaffils.svg?branch=master)](https://travis-ci.org/ccnmtl/cuaffils)

Simple library for generating and parsing CU affil
strings (as returned by WIND/CAS).

## Basic Example

Generating:

    >>> from cuaffils import generate_wind_string
    >>> d = dict(
    >>>    term='fall',
    >>>    year=2014,
    >>>    section_number='001',
    >>>    course_prefix_letter='n',
    >>>    course_number=6610,
    >>>    department_id='nurs'
    >>> )
    >>> print(generate_wind_string(**d))
    t3.y2014.s001.cn6610.nurs.st.course:columbia.edu
    >>> print(generate_ldap_string(**d))
    CUcourse_NURSN6610_001_2008_3
    >>> print(generate_course_directory_string(**d))
    20083NURS6610N001

Parsing:

    >>> from cuaffils import parse_wind_string
    >>> d = parse_wind_string('t3.y2014.s001.cn6610.nurs.st.course:columbia.edu')
    >>> print(d['term'])
    fall
    >>> print(d['department_id'])
    nurs
    ... etc ..
    >>> from cuaffils import parse_ldap_string
    >>> d = parse_ldap_string('CUcourse_NURSN6610_001_2008_3')
    ... same dict as response ...
    >>> from cuaffils import parse_course_directory_string
    >>> d = parse_course_directory_string('20083NURS6610N001')
    ... same dict as response ...

You get the idea.

API is still up for changes. Will release a 1.0 when I'm comfortable
that it won't change much.

This library aims to be the central point for handling CU affils
strings in whatever "standard" format they need to be handled in. Sort
of a babelfish for the different ways that they are represented
and ingested by different systems at the university. It should be
simple, complete, easy to use, and well tested.

If you encounter another format in use at CU, let us know and
we'll (attempt to) add support for it.

If you find a course affil string in some format that differs from
what this library produces, please file an issue. All of the parsing
code here is the result of years of reverse engineering un-documented
formats by our staff. We do our best, but we haven't encountered every
edge case yet.

## Exceptions

There are exceptions that get raised if you try to parse invalid
strings:

    >>> from cuaffils import parse_wind_string
    >>> parse_wind_string("i am not valid")
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "cuaffils/affils.py", line 43, in parse_wind_string
        raise InvalidWindString
    cuaffils.affils.InvalidWindString

There are also `InvalidLDAPString`, and `InvalidCourseDirString`
as expected.

## Testing

Run the tests with:

    $ python setup.py test
