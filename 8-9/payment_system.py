class Payment:
    def pay(self):
        print("Processing payment")
class CashPayment(Payment):
    def pay(self):
        print("Payment made using cash")
class CardPayment(Payment):
    def pay(self):
        print("Payment made using credit card")

payments = [CashPayment(), CardPayment()]
for p in payments:
    p.pay()
#MGM