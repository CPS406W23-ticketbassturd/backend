import uuid
from venue import Venue
from csv_reader import csvReader
from datetime import datetime

event_csv = csvReader('DB/events.csv')

class Event:
    """
    Event is the working representation of an event
    All fields are verified and ready to be used
    """
    def __init__(self, event_id, name, description, date, venue, min_age, num_attendees, price):
        self.event_id = event_id
        self.name = name
        self.description = description
        self.date = date
        self.venue = venue
        self.min_age = min_age
        self.num_attendees = num_attendees
        self.price = price

    @classmethod
    def create_event(cls, name, description, date, venue_id, min_age, price):
        event = event_csv.find_field_match(2, name)
        if event:
            return None
        venue = Venue.from_id(venue_id)
        if not venue:
            return None
        try:
            mem_date = datetime.strptime(date, '%m-%d-%Y')
        except ValueError:
            return None
        event = Event(str(uuid.uuid4()), name, description, mem_date, venue, min_age, 0, price)
        event.update_event()
        return event.event_id

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
        # Make sure all arguments can be converted without errors
        try:
            mem_date = datetime.strptime(db_event.date, '%m-%d-%Y')
            mem_min_age = int(db_event.min_age)
            mem_num_attendees = int(db_event.num_attendees)
            mem_price = int(db_event.price)
        except ValueError:
            return None

        return Event(event_id, db_event.name, db_event.description,
                     mem_date, mem_venue, mem_min_age, mem_num_attendees, mem_price)

    @classmethod
    def match_name(cls, name):
        matches = []
        for match in event_csv.fuzzy_field_match(2, name):
            matches.append(DB_Event.from_id(match[0]).to_dict())
        return matches

    def to_db_event(self):
        """
        Construct a DB_Event representation of this Event object
        :return: the DB_Event
        """
        date_str = datetime.strftime(self.date, '%m-%d-%Y')
        return DB_Event([self.event_id, self.venue.venue_id, self.name, self.description,
                         date_str, self.min_age, self.num_attendees, self.price])

    def update_event(self):
        """
        Updates this event in the event CSV
        :return:
        """
        db_event = self.to_db_event()
        db_event.save_event()

    def delete_event(self):
        """
        Deletes this event in the CSV
        :return:
        """
        DB_Event.delete_event(self.event_id)

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
        self.query = query
        self.event_id = query[0]
        self.venue_id = query[1]
        self.name = query[2]
        self.description = query[3]
        self.date = query[4]
        self.min_age = query[5]
        self.num_attendees = query[6]
        self.price = query[7]

    @classmethod
    def from_id(cls, event_id):
        """
        Converts an ID into the DB rep. of an event

        :param event_id: ID of event
        :return:    DB_Event, if ID valid
                    None, if ID invalid
        """
        found_event = event_csv.find_id_match(event_id)
        if not found_event:
            return None
        return DB_Event(found_event)

    @classmethod
    def delete_event(cls, event_id):
        """
        Deletes an event from the event CSV\

        :param event_id: ID of event to delete
        :return:
        """
        event_csv.delete_id_match(event_id)

    def save_event(self):
        """
        Updates or appends event to CSV
        :return:
        """
        event_csv.write_entry_id_match(self.event_id, self.query)

    def to_dict(self):
        return {
            "event_id": self.event_id,
            "venue_id": self.venue_id,
            "name": self.name,
            "description": self.description,
            "date": self.date,
            "min_age": self.min_age,
            "num_attendees": self.num_attendees,
            "price": self.price
        }

