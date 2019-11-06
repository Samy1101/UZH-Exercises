from unittest import TestCase
from public.script import sort


# Implement this test suite. Make sure that you define test
# methods and that each method _directly_ includes an assertion
# in the body, or -otherwise- the grading will mark the test
# suite as invalid.
class SortTests(TestCase):

    def test_is_new_list(self):
        list = [2, 3, 1]
        checker = sort(list)
        self.assertNotEqual(checker, list)

    def test_list_empty(self):
        actual = sort([])
        expected = []
        self.assertEqual(expected, actual)

    def test_None(self):
        actual = sort(None)
        expected = None
        self.assertEqual(expected, actual)

    def test_list_int(self):
        actual = sort([5, 3, 1, 2, 4])
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(expected, actual)

    def test_list_str(self):
        actual = sort(["b", "c", "a", "d"])
        expected = ["a", "b", "c", "d"]
        self.assertEqual(expected, actual)

