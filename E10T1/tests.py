from unittest import TestCase
from public.currency_converter import convert
from public.bank_account import BankAccount

# You need to add missing imports to make the test work!


class PrivateFunctionalTestSuite(TestCase):

    def test_0_convert(self):
        actual = convert(1.0, "EUR", "CHF")
        expected = 1.10
        self.assertAlmostEqual(expected, actual, delta=0.0001)
        
    def test_1_basic_banking(self):
        sut = BankAccount("CHF")
        sut.deposit(100.0, "CHF")
        sut.withdraw(10.0, "EUR")
        actual = sut.get_balance()
        expected = 89.0
        self.assertAlmostEqual(expected, actual, delta=0.0001)

    def test_2_invalid_convert_amount(self):
        with self.assertRaises(Warning):
            convert("", "CHF", "GBP")

    def test_3_convert_invalid_keys(self):
        with self.assertRaises(Warning):
            convert(50, "THB", "CHF")

    def test_4_covert_invalid_sub_keys(self):
        with self.assertRaises(Warning):
            convert(50, "CHF", "")

    def test_5_banking_invalid_currency(self):
        with self.assertRaises(Warning):
            BankAccount("")

    def test_6_banking_invalid_deposit_amount(self):

        b = BankAccount()

        with self.assertRaises(Warning):
            b.deposit(-200)

    def test_7_banking_invalid_withdraw_amount(self):
        b = BankAccount()

        with self.assertRaises(Warning):
            b.withdraw(-200)

    def test_8_banking_invalid_deposit_currency(self):
        b = BankAccount()

        with self.assertRaises(Warning):
            b.deposit(200, "")

    def test_9_banking_invalid_withdraw_currency(self):
        b = BankAccount()

        with self.assertRaises(Warning):
            b.withdraw(200, "")

    def test_10_convert_EUR_CAD(self):
        actual = convert(1.0, "EUR", "CAD")
        expected = 1.462
        self.assertAlmostEqual(expected, actual, delta=0.0001)

    # This current test suite only contains one very basic test case. By now,
    # you have some experience in writing test cases. We strongly encourage
    # you to implement further test cases. The additional tests can be run via
    # 'Test&Run' in ACCESS. These tests won't affect the grading of your solution
    # directly, but they can help you with identifying relevant corner cases
    # that you have to consider in your implementation.
