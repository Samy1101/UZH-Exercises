# add imports, if necessary

from public.exchange_rates import EXCHANGE_RATES


def convert(amount, from_currency, to_currency):
    inverted = False
    valid_keys = list(EXCHANGE_RATES.keys())

    if type(amount) != int and type(amount) != float:
        raise Warning("Please provide a valid amount")

    if type(from_currency) != str or type(to_currency) != str:
        raise Warning("Please provide a string")

    if not from_currency or not to_currency:
        raise Warning("Do not provide an empty string")

    if from_currency not in valid_keys or to_currency not in valid_keys:
        raise Warning("No exchange rate available")

    sub_keys = list(EXCHANGE_RATES[from_currency].keys())

    if to_currency not in sub_keys:
        inverted = True
        if from_currency not in EXCHANGE_RATES[to_currency]:
            raise Warning("No exchangerate available")

    if not inverted:
        real_amount = EXCHANGE_RATES[from_currency][to_currency] * amount

    if inverted:
        real_amount = amount / EXCHANGE_RATES[to_currency][from_currency]

    return real_amount


if __name__ == '__main__':
        print(convert(100, "EUR", "CAD"))
