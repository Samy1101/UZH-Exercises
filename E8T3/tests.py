from unittest import TestCase
from E8T3.script import Fridge


class PublicTestSuite(TestCase):

    def test_example(self):
        f = Fridge()
        # put an item into the fridge
        f.store((191112, "Butter"))
        self.assertEquals(1, len(f))
        # take it out again
        item = f.take((191112, "Butter"))
        self.assertEquals(0, len(f))
        # is it the right item?
        self.assertEquals((191112, "Butter"), item)

    def test_multiple_items(self):
        f = Fridge()

        f.store((191112, "Butter"))
        self.assertEquals(1, len(f))
        f.store((191112, "Butter"))
        self.assertEquals(2, len(f))
        item = f.take((191112, "Butter"))
        self.assertEquals(1, len(f))
        self.assertEquals((191112, "Butter"), item)
        item = f.take((191112, "Butter"))
        self.assertEquals(0, len(f))
        self.assertEquals((191112, "Butter"), item)

    def test_is_iterable(self):
        f = Fridge()
        actual = []
        expected = [(191112, "Butter"), (191113, "Butter")]

        f.store((191112, "Butter"))
        f.store((191113, "Butter"))

        for i in f:
            actual.append(i)

        self.assertEqual(expected, actual)

    def test_is_len(self):
        f = Fridge()
        f.store((191112, "Butter"))
        expected = 1
        actual = len(f)
        self.assertEqual(expected, actual)

    def test_take_before(self):
        f = Fridge()
        f.store((191112, "Butter"))
        f.store((191113, "Butter"))

        expected = [(191112, "Butter")]
        actual = f.take_before(191113)

        self.assertEqual(expected, actual)
        self.assertEqual(1, len(f))

    def test_take_before_None(self):
        f = Fridge()
        f.store((191112, "Butter"))
        expected = []
        actual = f.take_before(191110)

        self.assertEqual(expected, actual)

    def test_find_item(self):
        f = Fridge()
        f.store((191112, "Butter"))
        f.store((191113, "Butter"))
        f.store((191112, "Milk"))

        expected = (191112, "Butter")
        actual = f.find("Butter")

        self.assertEqual(expected, actual)

    def test_find_None(self):
        f = Fridge()

        expected = None
        actual = f.find("Butter")

        self.assertEqual(expected, actual)

    # This current test suite only contains one very basic test case. By now,
    # you have some experience in writing test cases. We strongly ecncourage
    # you to implement further test cases. The additional tests can be run via
    # 'Test&Run' in ACCESS. These tests won't affect the grading of your solution
    # directly, but they can help you with identifying relevant corner cases
    # that you have to consider in your implementation.
