from flask import Flask
from flask_restful import Api, Resource, reqparse
from APPLICATION.invalidAbort import dataAbort

app = Flask(__name__)
api = Api(app)


def paymentGateway(Amount):
    if Amount <= 20:
        return f"Paid: {Amount} though Gateway: CheapPaymentGateway"
    elif 21 <= Amount <= 500:
        return f"Paid: {Amount} though Gateway: ExpensivePaymentGateway"
    else:
        return f"Paid: {Amount} though Gateway: PremiumPaymentGateway"


class Payment(Resource):
    def get(self, CreditCardNumber, CardHolder, ExpirationDate, SecurityCode, Amount):
        dataAbort(CreditCardNumber, CardHolder, ExpirationDate, SecurityCode, Amount)
        print(paymentGateway(Amount))
        return 200


api.add_resource(Payment,
                 "/ProcessPayment/<string:CreditCardNumber>/<string:CardHolder>/<string:ExpirationDate>/<string:SecurityCode>/<float:Amount>")

if __name__ == "__main__":
    app.run(debug=True)
