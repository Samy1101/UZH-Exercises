from unittest import TestCase
from E9T1.script import Knight, Rogue, Mage


class TestBattle(TestCase):

    def test_basic_attack(self):
        sut = Knight("Arthur", 3)
        actual = sut.get_health()
        expected = (150, 150)
        self.assertEqual(expected, actual)

    def test_knight_attack(self):
        k = Knight("Arthur", 3)
        r = Rogue("Shades", 3)
        k.attack(r)
        actual = r.get_health()[0]
        expected = 150 - round(0.8 * (3 * 10 + 0))
        self.assertEqual(expected, actual)

    def test_knight_defense(self):
        k = Knight("Arthur", 3)
        r = Rogue("Shades", 3)
        r.attack(k)
        actual = k.get_health()[0]
        expected = 150 - round(0.75 * (3 * 10))
        self.assertEqual(expected, actual)

    def test_rogue_attack(self):
        k = Knight("Arthur", 3)
        r = Rogue("Shades", 3)
        r.attack(k)
        actual = k.get_health()[0]
        expected = 150 - round(0.75 * (3 * 10))
        self.assertEqual(expected, actual)

    def test_rogue_defense(self):
        k = Knight("Arthur", 3)
        r = Rogue("Shades", 3)
        k.attack(r)
        actual = r.get_health()[0]
        expected = 150 - round(0.8 * (3 * 10))
        self.assertEqual(expected, actual)

    def test_mage_attack(self):
        m = Mage("Gandal", 3)
        r = Rogue("Shades", 3)
        m.attack(r)
        actual = r.get_health()[0]
        expected = 150 - round(1.25 * (3 * 10))
        self.assertEqual(expected, actual)

    def test_mage_defense(self):
        m = Mage("Gandal", 3)
        r = Rogue("Shades", 3)
        r.attack(m)
        actual = m.get_health()[0]
        expected = 150 - round(1.5 * (3 * 10))
        self.assertEqual(expected, actual)



    # This current test suite only contains very basic test cases. By now,
    # you have some experience in writing test cases. We strongly encourage
    # you to implement further test cases. The additional tests can be run via
    # 'Test&Run' in ACCESS. These tests won't affect the grading of your solution
    # directly, but they can help you with identifying relevant corner cases
    # that you have to consider in your implementation.
