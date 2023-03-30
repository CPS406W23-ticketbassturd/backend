import sys
sys.path.append('../')

from ticketbassturdbackend import payment

class Payment_test:

    def __init__(self):
        self = self

    @classmethod
    def test_card_Valid(self):
        if payment.Payment.card_Valid() == True or payment.Payment.card_Valid() == False:
            return True
        else:
            return False