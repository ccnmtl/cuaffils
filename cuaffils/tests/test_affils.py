import unittest
from cuaffils import (
    generate_wind_string,
    generate_pamacea_string,
    generate_course_directory_string)

SIMPLE_TEST_FIELDS = dict(
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
        course_dir='20143NURS6610N001'),
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
