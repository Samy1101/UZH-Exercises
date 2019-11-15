from unittest import TestCase
from E8T1.script import ProfanityFilter


class PublicTestSuite(TestCase):

    def test_example(self):
        f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
        msg = "abc defghi mastard jklmno"
        actual = f.filter(msg)
        expected = "abc defghi ?#$?#$? jklmno"
        self.assertEquals(expected, actual)

    def test_substring(self):
        f = ProfanityFilter(["tes"], "1234")
        msg = "hello tes"
        actual = f.filter(msg)
        expected = "hello 123"
        self.assertEqual(expected, actual)

    def test_extended_template(self):
        f = ProfanityFilter(["test"], "12")
        msg = "hello test"
        actual = f.filter(msg)
        expected = "hello 1212"
        self.assertEqual(expected, actual)

    def test_case_insensitive(self):
        f = ProfanityFilter(["test"], "1234")
        msg = "hello test Test"
        actual = f.filter(msg)
        expected = "hello 1234 1234"
        self.assertEqual(expected, actual)

    def test_subword_keys(self):
        f = ProfanityFilter(["test", "protest"], "1234")
        msg = "the test of the protest"
        actual = f.filter(msg)
        expected = "the 1234 of the 1234123"
        self.assertEqual(expected, actual)

    def test_subword_msg(self):
        f = ProfanityFilter(["test"], "1234")
        msg = "the protest"
        actual = f.filter(msg)
        expected = "the pro1234"
        self.assertEqual(expected, actual)

    # This current test suite only contains one very basic test case. By now,
    # you have some experience in writing test cases. We strongly ecncourage
    # you to implement further test cases. The additional tests can be run via
    # 'Test&Run' in ACCESS. These tests won't affect the grading of your solution
    # directly, but they can help you with identifying relevant corner cases
    # that you have to consider in your implementation.
