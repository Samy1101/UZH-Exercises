from unittest import TestCase
from E7T2.script import move


# You are supposed to develop the functionality in a test-driven way.
# Think about relevant test cases and extend the following test suite
# until all requirements of the description are covered. The test suite
# will be run against various correct and incorrect implementations, so
# make sure that you only test the `move` function and stick strictly
# to its defined signature.
#
# Make sure that you define test methods and that each method
# _directly_ includes an assertion in the body, or -otherwise- the
# grading will mark the test suite as invalid.
class MoveTestSuite(TestCase):

    def test_move_not_possible(self):
        state = (
            "#####   ",
            "###    #",
            "#    o##",
            "   #####"
        )

        with self.assertRaises(Warning):
            move(state, "right")

    def test_invalid_characters(self):
        state = (
            "####x   ",
            "###    #",
            "#   o ##",
            "   #####"
        )

        with self.assertRaises(Warning):
            move(state, "right")

    def test_same_length(self):
        state = (
            "#####  ",
            "###    #",
            "#   o ##",
            "   #####"
        )

        with self.assertRaises(Warning):
            move(state, "right")

    def test_one_player(self):
        state = (
            "####o   ",
            "###    #",
            "#   o ##",
            "   #####"
        )

        with self.assertRaises(Warning):
            move(state, "right")

    def test_sensible_size(self):
        state = ()

        with self.assertRaises(Warning):
            move(state, "right")

    def test_exceed_up_down(self):
        state = (
            "#####o  ",
            "###    #",
            "#     ##",
            "   #####"
        )

        with self.assertRaises(Warning):
            move(state, "up")

    def test_exceed_left_right(self):
        state = (
            "#####  o",
            "###    #",
            "#     ##",
            "   #####"
        )

        with self.assertRaises(Warning):
            move(state, "right")

    def test_move_is_possible(self):
        state = (
            "#####   ",
            "###    #",
            "#   o ##",
            "   #####"
        )
        actual = move(state, "right")

        expected = (
            (
                "#####   ",
                "###    #",
                "#    o##",
                "   #####"
            ),
            ("left", "up")
        )
        self.assertEqual(expected, actual)

    def test_is_alphabetical_order(self):
        state = (
            "        ",
            "        ",
            "    o   ",
            "        "
        )

        actual = move(state, "up")

        expected = ((
            "        ",
            "    o   ",
            "        ",
            "        "
        ), ("down", "left", "right", "up")
        )

        self.assertEqual(expected, actual)

    def test_empty_strings(self):
        state = (
            "", "", "", ""
        )

        with self.assertRaises(Warning):
            move(state, "left")
