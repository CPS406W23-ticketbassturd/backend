from venue import Venue
from csv_reader import csvReader
from datetime import datetime

event_csv = csvReader('events.csv')

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
        # Make sure all arguments can be converted without errors
        try:
            mem_date = datetime.strptime(db_event.date, '%m/%d/%Y')
        except ValueError:
            return None

        return Event(event_id, db_event.name, db_event.description,
                     mem_date, mem_venue, db_event.min_age, db_event.num_attendees)

    def to_db_event(self):
        """
        Construct a DB_Event representation of this Event object
        :return: the DB_Event
        """
        date_str = datetime.strftime(self.date, '%m/%d/%Y')
        return DB_Event([self.event_id, self.venue.venue_id, self.name, self.description,
                         date_str, self.min_age, self.num_attendees])

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

    @classmethod
    def from_id(cls, event_id):
        """
        Converts an ID into the DB rep. of an event

        :param event_id: ID of event
        :return:    DB_Event, if ID valid
                    None, if ID invalid
        """
        found_event = event_csv.find_id_match(event_id)
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

