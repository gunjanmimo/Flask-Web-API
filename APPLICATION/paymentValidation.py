import re
import datetime


def valid_CreditCardNumber(CreditCardNumber):
    pattern = '^[973][0-9]{15}|[973][0-9]{3}-[0-9]{4}-[0-9]{4}-[0-9]{4}$'
    valid = re.match(pattern, CreditCardNumber)
    return valid


def valid_CardHolderName(CardHolder):
    alpha_regex = "^[a-z A-Z]+$"
    if re.match(alpha_regex, CardHolder):
        return True
    else:
        False


def valid_ExpirationDate(ExpirationDate):
    return datetime.datetime.strptime(ExpirationDate, "%m-%y") > datetime.datetime.now()


def valid_SecurityCode(SecurityCode):
    if len(SecurityCode) == 3 and SecurityCode.isdigit():
        return True
    else:
        False


def valid_Amount(Amount):
    return isinstance(Amount, int) or isinstance(Amount, float)
