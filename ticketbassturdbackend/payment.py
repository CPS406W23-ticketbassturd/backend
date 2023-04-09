from datetime import datetime
import random


class Payment:

    def __init__(self, cardNum, nameOnCard, expMonth, expYear, cvvNum):
        self.cardNum = cardNum
        self.nameOnCard = nameOnCard
        self.expMonth = expMonth
        self.expYear = expYear
        self.cvvNum = cvvNum

    def card_Valid(self):
        if len(str(self.cardNum)) != 16 or not str(self.cardNum).isdigit() or not all(i.isalpha() for i in self.nameOnCard.split(" ")):
            print("1")
            return False
        if not str(self.expMonth).isdigit() or not (1 <= int(self.expMonth) <= 12):
            print("2")
            return False
        if not str(self.expYear).isdigit() or (int(self.expYear) < datetime.now().year):
            print("3")
            return False
        if (int(self.expYear) == datetime.now().year and int(self.expMonth) < datetime.now().month):
            print("4")
            return False
        if len(str(self.cvvNum)) != 3 or not str(self.cvvNum).isdigit() or len(self.nameOnCard.split(" ")) < 2:
            print(f"Invalid card data: cardNum: {self.cardNum}, nameOnCard: {self.nameOnCard}, expMonth: {self.expMonth}, expYear: {self.expYear}, cvvNum: {self.cvvNum}")
            return False
        def confirm_payment():
            x = random.random()
            if x < 0.2:
                print('random chance of fail')
                return False
            return True
        if (confirm_payment()):
            print("Thank You For Your Payment!")
            return True
        else:
            print("Card Declined!")
            return False

