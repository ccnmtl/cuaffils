import unittest
from cuaffils import (
    generate_wind_string,
    generate_pamacea_string,
    generate_course_directory_string)

SIMPLE_TEST_FIELDS = dict(
    term='fall',
    year=2014,
    section_number='001',
    course_prefix_letter='N',
    course_number=6610,
    department_id='NURS'
)

class GenerateWindStringTest(unittest.TestCase):
    def test_basic(self):
        s = 't3.y2014.s001.cN6610.NURS.st.course:columbia.edu'
        self.assertEqual(generate_wind_string(**SIMPLE_TEST_FIELDS), s)


class GeneratePamaceaStringTest(unittest.TestCase):
    def test_basic(self):
        s = 'CUcourse_NURSN6610_001_2014_3'
        self.assertEqual(generate_pamacea_string(**SIMPLE_TEST_FIELDS), s)


class GenerateCourseDirectoryStringTest(unittest.TestCase):
    def test_basic(self):
        s = '20143NURS6610N001'
        self.assertEqual(generate_course_directory_string(**SIMPLE_TEST_FIELDS), s)
