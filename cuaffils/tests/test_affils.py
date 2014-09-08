import unittest
from cuaffils import (
    generate_wind_string,
    generate_pamacea_string,
    generate_course_directory_string,

    parse_wind_string,
    parse_pamacea_string,
    parse_course_directory_string,

    InvalidWindString,
    InvalidPamaceaString,
    InvalidCourseDirString,
)

TEST_CASES = [
    dict(
        fields=dict(
            term='fall',
            year=2014,
            section_number='001',
            course_prefix_letter='N',
            course_number=6610,
            department_id='NURS'
            ),
        wind='t3.y2014.s001.cN6610.NURS.st.course:columbia.edu',
        pamacea='CUcourse_NURSN6610_001_2014_3',
        course_dir='20143NURS6610N001'
    ),

    dict(
        fields=dict(
            term='spring',
            year=2010,
            section_number='010',
            course_prefix_letter='F',
            course_number=1234,
            department_id='EENG'
            ),
        wind='t1.y2010.s010.cF1234.EENG.st.course:columbia.edu',
        pamacea='CUcourse_EENGF1234_010_2010_1',
        course_dir='20101EENG1234F010'
    ),
]

class GenerateWindStringTest(unittest.TestCase):
    def test_basic(self):
        for c in TEST_CASES:
            fields = c['fields']
            s = c['wind']
            self.assertEqual(generate_wind_string(**fields), s)


class GeneratePamaceaStringTest(unittest.TestCase):
    def test_basic(self):
        for c in TEST_CASES:
            fields = c['fields']
            s = c['pamacea']
            self.assertEqual(generate_pamacea_string(**fields), s)


class GenerateCourseDirectoryStringTest(unittest.TestCase):
    def test_basic(self):
        for c in TEST_CASES:
            fields = c['fields']
            s = c['course_dir']
            self.assertEqual(generate_course_directory_string(**fields), s)


class ParseWindStringTest(unittest.TestCase):
    def test_basic(self):
        for c in TEST_CASES:
            fields = c['fields']
            s = c['wind']
            r = parse_wind_string(s)
            for k in fields.keys():
                self.assertEqual(r[k], fields[k])


class ParsePamaceaStringTest(unittest.TestCase):
    def test_basic(self):
        for c in TEST_CASES:
            fields = c['fields']
            s = c['pamacea']
            r = parse_pamacea_string(s)
            for k in fields.keys():
                self.assertEqual(r[k], fields[k])


class ParseCourseDirectoryStringTest(unittest.TestCase):
    def test_basic(self):
        for c in TEST_CASES:
            fields = c['fields']
            s = c['course_dir']
            r = parse_course_directory_string(s)
            for k in fields.keys():
                self.assertEqual(r[k], fields[k])


class InvalidStringsTests(unittest.TestCase):
    def test_wind(self):
        s = "i am not valid as anything"
        self.assertRaises(InvalidWindString, parse_wind_string, s)

    def test_pamacea(self):
        s = "i am not valid as anything"
        self.assertRaises(InvalidPamaceaString, parse_pamacea_string, s)

    def test_coursedir(self):
        s = "i am not valid as anything"
        self.assertRaises(InvalidCourseDirString, parse_course_directory_string, s)
