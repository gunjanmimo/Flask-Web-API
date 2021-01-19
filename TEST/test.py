import requests

base = "http://127.0.0.1:5000/"


# response = requests.get(base + "/ProcessPayment")
# print(response.json())


# test endpoint:  check api behaviour for different request
def test_invalid_endPoint(endPoint):
    response = requests.get(base + endPoint)
    if response.status_code == 404:
        print("Invalid test: Passed")
    else:
        print("Invalid test: Failed")

# test invalid envdpoint sequence
def test_invalid_endPoint_Sequence(endPoint):
    response = requests.get(base + endPoint)
    if response.status_code != 200:
        print("Invalid test: Passed")
    else:
        print("Invalid test: Failed")

# test invalid CreditCardNumber
def test_invalid_CreditCardNumber(endPoint):
    response = requests.get(base + endPoint)
    if response.status_code != 200:
        print("Invalid test: Passed")
    else:
        print("Invalid test: Failed")

# test invalid CardHolder
def test_invalid_CardHolder(endPoint):
    response = requests.get(base + endPoint)
    if response.status_code != 200:
        print("Invalid test: Passed")
    else:
        print("Invalid test: Failed")

# test invalid ExpirationDate
def test_invalid_ExpirationDate(endPoint):
    response = requests.get(base + endPoint)
    if response.status_code != 200:
        print("Invalid test: Passed")
    else:
        print("Invalid test: Failed")

# test invalid SecurityCode
def test_invalid_SecurityCode(endPoint):
    response = requests.get(base + endPoint)
    if response.status_code != 200:
        print("Invalid test: Passed")
    else:
        print("Invalid test: Failed")

# test invalid Amount
def test_invalid_Amount(endPoint):
    response = requests.get(base + endPoint)
    if response.status_code != 200:
        print("Invalid test: Passed")
    else:
        print("Invalid test: Failed")

# test valid payment
def test_validPayment(endPoint):
    response = requests.get(base + endPoint)
    if response.status_code == 200:
        print("Valid Payment Test: Passed")
    else:
        print("Valid Payment Test: Failed")


# invalid endpoint testing
print("\n" + "-" * 10 + "Invalid End Point Test" + "-" * 10)
test_invalid_endPoint("/payment")
print("-" * 25 + "\n")

# invalid endpoint sequence testing
print("\n" + "-" * 10 + "Invalid endpoint sequence Test" + "-" * 10)
test_invalid_endPoint("/10-23/333/Gunjan/ProcessPayment/20.8/0525362587961578")
test_invalid_endPoint("/9123-4567-8912-3456/John/12-23/134/4564.8/ProcessPayment")
print("-" * 25 + "\n")

# invalid CreditCardNumber testing
print("\n" + "-" * 10 + "Invalid CreditCardNumber Test" + "-" * 10)
test_invalid_CreditCardNumber("/ProcessPayment/0525362587961578/Gunjan/10-23/333/20.8")
test_invalid_CreditCardNumber("/ProcessPayment/5123456789123456/John/10-23/333/45.8")
print("-" * 25 + "\n")

# invalid CardHolder testing
print("\n" + "-" * 10 + "Invalid CardHolder Test" + "-" * 10)
test_invalid_CardHolder("/ProcessPayment/3123456789123456/mi34ke23/10-23/333/100.8")
test_invalid_CardHolder("/ProcessPayment/3123456789123456/231/10-23/333/900.8")
print("-" * 25 + "\n")

# invalid ExpirationDate testing
print("\n" + "-" * 10 + "Invalid ExpirationDate Test" + "-" * 10)
test_invalid_CardHolder("/ProcessPayment/3123456789123456/Gunjan/10-13/333/600.8")
test_invalid_CardHolder("/ProcessPayment/3123456789123456/John/12-20/333/12.8")
print("-" * 25 + "\n")

# invalid SecurityCode testing
print("\n" + "-" * 10 + "Invalid SecurityCode Test" + "-" * 10)
test_invalid_CardHolder("/ProcessPayment/3123456789123456/Gunjan/10-22/ABC/5000.34")
test_invalid_CardHolder("/ProcessPayment/3123456789123456/John/11-23/3A3/34.8")
print("-" * 25 + "\n")

# invalid Amount testing
print("\n" + "-" * 10 + "Invalid Amount Test" + "-" * 10)
test_invalid_CardHolder("/ProcessPayment/3123456789123456/Gunjan/10-22/1234/john")
test_invalid_CardHolder("/ProcessPayment/3123456789123456/John/11-23/3333/gunjan")
print("-" * 25 + "\n")

# valid endpoint
print("\n" + "-" * 10 + "Valid Payment Test" + "-" * 10)
test_validPayment("/ProcessPayment/3123456789123456/Gunjan/10-21/333/564.8")
test_validPayment("/ProcessPayment/9123-4567-8912-3456/John/12-23/134/4564.8")
print("-" * 25 + "\n")
