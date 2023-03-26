class Ticket:
    def __init__(self, event, price):
        # TODO: Input type validation
        self.event = event
        self.price = price

    @classmethod
    def fromID(cls, ticket_id):
        #TODO: Generate ticket from query w/ ID
        return Ticket(None, None)

    def is_valid(self, date):
        #TODO: Check against event date for validity
        return True