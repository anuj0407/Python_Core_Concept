'''
Duck typing is a programming style that does not look at the type of an object to determine if it can be used for a particular purpose.
Instead, it looks at the methods and properties of the object to determine if it can be used in a certain way.
This allows for more flexible and dynamic code, as objects of different types can be used interchangeably as long as they have the necessary methods and properties.
'''

#diffrent classes
class UPI:
    def __init__(self, upi_id):
        self.upi_id = upi_id

    def payment(self, amount): # same method name in all classes to achieve duck typing
        print(f"Processing UPI payment of {amount} using UPI ID: {self.upi_id}")

class CreditCard:
    def __init__(self, card_number):
        self.card_number = card_number

    def payment(self, amount):
        print(f"Processing credit card payment of {amount} using card number: {self.card_number}")

class GiftCard:
    def __init__(self, gift_card_code):
        self.gift_card_code = gift_card_code

    def payment(self, amount):
        print(f"Processing gift card payment of {amount} using gift card code: {self.gift_card_code}")

#function to process payment
def process_payment(payment_method, amount): # passing the object as an argument to the function
    payment_method.payment(amount)

# user interaction
print("------Welcome to the Payment Gateway!------")
upi_payment = UPI("anuj@upi")
credit_card_payment = CreditCard("1234-5678-9012-3456")
gift_card_payment = GiftCard("GIFT12345")

process_payment(upi_payment, 1000)
process_payment(credit_card_payment, 2000)
process_payment(gift_card_payment, 500)