from forex_python.converter import CurrencyRates, RatesNotAvailableError

def currency_converter():
    try:
        # Instantiate the converter
        converter = CurrencyRates()

        # Enter the amount to convert
        amount = int(input("Please enter the amount to convert: "))

        # Currency code of the amount to convert
        from_currency = input("Enter the currency code of the amount you are converting: ").upper()

        # Currency code of the amount to convert to
        to_currency = input("Enter the currency code you are converting to: ").upper()

        # Convert the amount
        converted_amount = converter.convert(from_currency, to_currency, amount)

        return f'The amount is {converted_amount:.2f} and the currency is {to_currency}'
    except RatesNotAvailableError:
        return "Currency rates are not available at the moment. Please try again later."

print(currency_converter())
