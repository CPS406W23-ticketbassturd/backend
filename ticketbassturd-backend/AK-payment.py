from datetime import datetime
import random
class payment:
    
    def __init__(self, cardNum, nameOnCard, expMonth, expYear, cvvNum):
        self.cardNum = cardNum
        self.nameOnCard = nameOnCard
        self.expMonth = expMonth
        self.expYear = expYear
        self.cvvNum = cvvNum
    
    def card_Valid(self):
        if len(self.cardNum) != 16 or not self.cardNum.isdigit() or not all(i.isalpha() for i in self.nameOnCard.split(" ")) \
        or not self.expMonth.isdigit() or not (1 <= int(self.expMonth) <= 12) \
        or not self.expYear.isdigit() or (int(self.expYear) < datetime.now().year) \
        or (int(self.expYear) == datetime.now().year and int(self.expMonth) < datetime.now().month) \
        or len(self.cvvNum) != 3 or not self.cvvNum.isdigit() or len(self.nameOnCard.split(" ")) < 2:
            print(f"Invalid card data: cardNum: {self.cardNum}, nameOnCard: {self.nameOnCard}, expMonth: {self.expMonth}, expYear: {self.expYear}, cvvNum: {self.cvvNum}")
            return False
        def confirm_payment():
            x = random.random()
            if x < 0.2:
                return False
            return True
        if (confirm_payment()): 
            print("Thank You For Your Payment!")
            return True
        else: 
            print("Card Declined!")
            return False
    
