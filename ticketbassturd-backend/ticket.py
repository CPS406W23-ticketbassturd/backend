class Ticket:
    def __init__(self, event, price):
        self.event = event
        self.price = price

    @classmethod
    def fromID(cls, ticket_id):
        #TODO: Generate ticket from query w/ ID
        return Ticket(None, None)

    def date_valid(self, date):
        return self.event.date_valid(date)