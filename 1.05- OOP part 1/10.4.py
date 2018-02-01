# Napisz prosty konwerter walut, który na wejściu przyjmie stringa składającego się z:
# kwoty, waluty wejściowej, słówka kluczowego "to" i kwoty wyjściowej.
# Użyj następujących kursów: 1 PLN to 1000 USD, 1 PLN to 4505 EURO, 1 PLN to 100 JPY
# Załóż, że konwersje są wykonywane tylko z lub do PLNów.
# Dla zaawansowanych: przeliczaj wszystkie waluty między sobą (PLN, USD, EURO, JPY)
# Przykład:
# input: "2 PLN to USD" output: "2000 USD"
# input "15 USD to PLN" output: "0.015 PLN"

askUser = input("To what would you like to convert PLN?\n"
                "Use schema: amount currency to currency you want to convert to.\n"
                "Eg. 2 PLN to USD\n"
                "Avaliable currencies PLN/USD/JPY\n")
data = askUser.split()
amount = data[0]
currency = data[1]
currency = currency.upper()
change_currency = data[3]
change_currency = change_currency.upper()
currency_exchange = {
    'USD': 1000,
    'EURO': 4505,
    'JPY': 100
}


def convert(user_amount, currency, change):
    if currency == "PLN":
        result = int(user_amount) * currency_exchange[change]
    else:
        result = int(user_amount) / currency_exchange[currency]
    return result

print(convert(amount, currency, change_currency))
