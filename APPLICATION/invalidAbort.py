from flask_restful import abort
import datetime
from APPLICATION.paymentValidation import *


def abortInvalid_CreditCardNumber(CreditCardNumber):
    if not valid_CreditCardNumber(CreditCardNumber):
        abort(400, message="put a valid CreditCardNumber")


def abortInvalid_CardHolder(CardHolder):
    if not valid_CardHolderName(CardHolder):
        abort(400, message="put a valid Name")


def abortInvalid_ExpirationDate(ExpirationDate):
    if not valid_ExpirationDate(ExpirationDate):
        abort(400, message="put a valid ExpirationDate")


def abortInvalid_SecurityCode(SecurityCode):
    if not valid_SecurityCode(SecurityCode): abort(400, message="put a valid SecurityCode")


def abortInvalid_Amount(Amount):
    if not valid_Amount(Amount): abort(400, message="put a valid Amount")


def dataAbort(CreditCardNumber, CardHolder, ExpirationDate, SecurityCode, Amount):
    abortInvalid_CreditCardNumber(CreditCardNumber)
    abortInvalid_CardHolder(CardHolder)
    abortInvalid_ExpirationDate(ExpirationDate)
    abortInvalid_SecurityCode(SecurityCode)
    abortInvalid_Amount(Amount)
