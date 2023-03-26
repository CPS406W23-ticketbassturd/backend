from venue import Venue
import datetime

class Event:
    """
    Event is the working representation of an event
    All fields are verified and ready to be used
    """
    def __init__(self, event_id, name, description, date, venue, min_age, num_attendees):
        self.event_id = event_id
        self.name = name
        self.description = description
        self.date = date
        self.venue = venue
        self.min_age = min_age
        self.num_attendees = num_attendees

    @classmethod
    def from_id(cls, event_id):
        """
        Constructs a workable event object from an ID, does validation

        :param event_id: ID of event to construct
        :return:    Event, if event valid
                    None, if event invalid
        """
        # Get and make sure event ID points to real event
        db_event = DB_Event.from_id(event_id)
        if not db_event:
            # TODO: Handle invalid venue ID (event suspended until manual intervention)
            return None

        # Get and make sure DB_Events venue_id points to a real venue
        mem_venue = Venue.from_id(db_event.venue_id)
        if not mem_venue:
            return None

        # GENERATE EVENT OBJ ----------------------

        # TODO: LUCAS - parse date string into datetime representation
        mem_date = db_event.date
        return Event(event_id, db_event.name, db_event.description,
                     mem_date, mem_venue, db_event.min_age, db_event.num_attendees)

    def date_valid(self, date):
        """
        Checks that event has not already transpired

        :param date: date to check event validity
        :return:     True/False
        """
        return date <= self.date

    def at_capacity(self):
        """
        Checks if event has reached maximum capacity
        :return: True/False
        """
        return self.num_attendees >= self.venue.max_capacity

class DB_Event:
    """
    DB_Event is the Database representation of an event
    mainly used as an intermediate state between DB query and usable fields
    """

    def __init__(self, query):
        """
        Parses a DB query into easily handleable fields

        :param query: query from which to procure entries
        """
        # TODO: Parse query
        self.event_id = None
        self.venue_id = None
        self.event_id = None
        self.name = None
        self.description = None
        self.date = None
        self.min_age = None
        self.num_attendees = None

    @classmethod
    def from_id(cls, event_id):
        """
        Converts an ID into the DB rep. of an event

        :param event_id: ID of event
        :return:    DB_Event, if ID valid
                    None, if ID invalid
        """
        #TODO: Check if ID exists in DB
        id_valid = True
        if not id_valid:
            return None
        # TODO: Get Query
        query = ""
        return DB_Event(query)
