class Venue:
    def __init__(self, venue_id, name, description, address, max_capacity):
        self.venue_id = venue_id
        self.name = name
        self.description = description
        self.address = address
        self.max_capacity = max_capacity

    @classmethod
    def from_id(cls, venue_id):
        # TODO: Generate venue from query w/ ID
        return Venue(venue_id, None, None, None, None)