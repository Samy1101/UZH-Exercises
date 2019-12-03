# add imports, if necessary
from E10T1.exchange_rates import EXCHANGE_RATES
from E10T1.currency_converter import convert


class BankAccount:

    def __init__(self, currency="CHF"):

        if not self.__check_currency(currency)[0]:
            raise Warning("No exchange rate available")

        self._currency = currency
        self._deposit = 0

    @staticmethod
    def __check_currency(currency):

        """
        returns a tuple.
        First bool indicates whether the currency is valid
        second bool indicates whether you have to invert your calculations
        """

        if currency not in list(EXCHANGE_RATES.keys()):
            return False, False

        for i in EXCHANGE_RATES.keys():
            for j in EXCHANGE_RATES[i].keys():
                if j == currency:
                    return True, True

        return True, False

    def get_currency(self):
        return self._currency

    def get_balance(self):
        return self._deposit
        
    def deposit(self, amount, currency="CHF"):
        inverted = self.__check_currency(currency)[1]

        if not self.__check_currency(currency)[0]:
            raise Warning("no exchange rate available")

        if type(amount) != float and type(amount) != int:
            raise Warning("please provide float or int")

        if amount < 0:
            raise Warning("please provide a positive amount")

        if currency != self._currency:
            if not inverted:
                self._deposit += convert(amount, self._currency, currency)

            if inverted:
                self._deposit += convert(amount, currency, self._currency)

        else:
            self._deposit += amount

    def withdraw(self, amount, currency="CHF"):
        inverted = self.__check_currency(currency)[1]

        if not self.__check_currency(currency)[0]:
            raise Warning("no exchange rate available")

        if type(amount) != float and type(amount) != int:
            raise Warning("please provide float or int")

        if amount < 0:
            raise Warning("please provide a positive amount")

        if currency != self._currency:
            if not inverted:
                self._deposit -= convert(amount, self._currency, currency)

            if inverted:
                self._deposit -= convert(amount, currency, self._currency)
        else:
            self._deposit -= amount

        if self._deposit < 0:
            self._deposit += amount
            raise Warning("The bank balance can not go below 0")


if __name__ == '__main__':
    b = BankAccount()
    b.deposit(100, "JPY")
    b.withdraw(200, "JPY")
    print(b.get_balance())
