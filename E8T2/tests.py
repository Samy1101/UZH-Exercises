from unittest import TestCase
from E8T2.script import Publication


class PublicTestSuite(TestCase):

    def test_example(self):
        a = Publication(["A"], "B", 1234)
        b = Publication(["A"], "B", 1234)
        self.assertEqual(a, b)

    def test_string(self):
        p = Publication(["Duvall", "Matyas", "Glover"], "Continuous Integration", 2007)
        s = "Publication([\"Duvall\", \"Matyas\", \"Glover\"], \"Continuous Integration\", 2007)"
        self.assertEqual(s, str(p))

    def test_repr(self):
        p = Publication(["Duvall", "Matyas", "Glover"], "Continuous Integration", 2007)
        s = ['Publication(["Duvall", "Matyas", "Glover"], "Continuous Integration", 2007)']
        self.assertEquals(s, [str(p)])

    def test_eq_different(self):
        p = Publication(["Duvall", "Matyas", "Glover"], "Continuous Integration", 2007)
        s = (1, 2, 3)
        self.assertEqual(p==s, False)

    def test_eq_same(self):
        p = Publication(["Duvall", "Matyas", "Glover"], "Continuous Integration", 2007)
        s = Publication(["Duvall", "Matyas", "Glover"], "Continuous Integration", 2007)
        self.assertEqual(p==s, True)

    def test_get(self):
        p = Publication(["Duvall", "Matyas", "Glover"], "Continuous Integration", 2007)

        a = p.get_authors()
        b = p.get_authors()

        self.assertEqual(b, a)

    # This current test suite only contains one very basic test case. By now,
    # you have some experience in writing test cases. We strongly ecncourage
    # you to implement further test cases. The additional tests can be run via
    # 'Test&Run' in ACCESS. These tests won't affect the grading of your solution
    # directly, but they can help you with identifying relevant corner cases
    # that you have to consider in your implementation.
