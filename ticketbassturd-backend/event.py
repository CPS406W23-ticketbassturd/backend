class Event:
    def __init__(self, name, description, date, venue, min_age, num_attendees):
        #TODO: Input type validation
        self.name = name
        self.description = description
        self.date = date
        self.venue = venue
        self.min_age = min_age
        self.num_attendees = num_attendees

    def is_valid(self, date):
        # TODO: date validity check
        return True

    def at_capacity(self):
        #TODO: venue capacity check
        return False