from csv_reader import csvReader

venue_csv = csvReader('DB/venue.csv')

class Venue:
    def __init__(self, venue_id, name, description, address, max_capacity):
        self.venue_id = venue_id
        self.name = name
        self.description = description
        self.address = address
        self.max_capacity = max_capacity

    @classmethod
    def from_id(cls, venue_id):
        """
        Constructs a workable venue object from an ID, does validation

        :param venue_id: ID of venue to construct
        :return:    Venue, if venue valid
                    None, if venue invalid
        """
        # Get and make sure venue ID points to real venue
        db_venue = DB_Venue.from_id(venue_id)
        if not db_venue:
            return None

        # GENERATE VENUE OBJ ----------------------
        # Make sure all arguments can be converted without errors
        try:
            mem_max_capacity = int(db_venue.max_capacity)
        except ValueError:
            return None

        return Venue(venue_id, db_venue.name, db_venue.description, db_venue.address, mem_max_capacity)

    def to_db_venue(self):
        """
        Construct a DB_venue representation of this venue object
        :return: the DB_venue
        """

        return DB_Venue([self.venue_id, self.name, self.description, self.address, self.max_capacity])

    def update_venue(self):
        """
        Updates this venue in the venue CSV
        :return:
        """
        db_venue = self.to_db_venue()
        db_venue.save_venue()

    def delete_venue(self):
        """
        Deletes this venue in the CSV
        :return:
        """
        DB_Venue.delete_venue(self.venue_id)


class DB_Venue:
    """
    DB_Venue is the Database representation of a venue
    mainly used as an intermediate state between DB query and usable fields
    """

    def __init__(self, query):
        """
        Parses a DB query into easily handleable fields

        :param query: query from which to procure entries
        """
        self.query = query
        self.venue_id = query[0]
        self.name = query[1]
        self.description = query[2]
        self.address = query[3]
        self.max_capacity = query[4]

    @classmethod
    def from_id(cls, venue_id):
        """
        Converts an ID into the DB rep. of an venue

        :param venue_id: ID of venue
        :return:    DB_venue, if ID valid
                    None, if ID invalid
        """
        found_venue = venue_csv.find_id_match(venue_id)
        if not found_venue:
            return None
        return DB_Venue(found_venue)

    @classmethod
    def delete_venue(cls, venue_id):
        """
        Deletes an venue from the venue CSV\

        :param venue_id: ID of venue to delete
        :return:
        """
        venue_csv.delete_id_match(venue_id)

    def save_venue(self):
        """
        Updates or appends venue to CSV
        :return:
        """
        venue_csv.write_entry_id_match(self.venue_id, self.query)

