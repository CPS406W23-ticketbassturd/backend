from event import Event
from csv_reader import csvReader
from datetime import datetime

ticket_csv = csvReader('DB/tickets.csv')


class Ticket:
    def __init__(self, ticket_id, event, price):
        self.ticket_id = ticket_id
        self.event = event
        self.price = price

    @classmethod
    def from_id(cls, ticket_id):
        """
        Constructs a workable ticket object from an ID, does validation

        :param ticket_id: ID of ticket to construct
        :return:    Ticket, if ticket valid
                    None, if ticket invalid
        """
        # Get and make sure ticket ID points to real ticket
        db_ticket = DB_Ticket.from_id(ticket_id)
        if not db_ticket:
            return None

        # Get and make sure DB_Tickets event_id points to a real event
        mem_event = Event.from_id(db_ticket.event_id)
        if not mem_event:
            return None

        # GENERATE TICKET OBJ ----------------------
        # Make sure all arguments can be converted without errors
        try:
            mem_price = int(db_ticket.price)
        except ValueError:
            return None

        return Ticket(ticket_id, db_ticket.event_id, mem_price)

    def to_db_ticket(self):
        """
        Construct a DB_Ticket representation of this Ticket object
        :return: the DB_Ticket
        """
        return DB_Ticket([self.ticket_id, self.event.event_id, self.price])

    def update_ticket(self):
        """
        Updates this ticket in the ticket CSV
        :return:
        """
        db_ticket = self.to_db_ticket()
        db_ticket.save_ticket()

    def delete_ticket(self):
        """
        Deletes this ticket in the CSV
        :return:
        """
        DB_Ticket.delete_ticket(self.ticket_id)

    def date_valid(self, date):
        """
        Checks that ticket has not already transpired

        :param date: date to check ticket validity
        :return:     True/False
        """
        return self.event.date_valid()


class DB_Ticket:
    """
    DB_Ticket is the Database representation of a ticket
    mainly used as an intermediate state between DB query and usable fields
    """

    def __init__(self, query):
        """
        Parses a DB query into easily handleable fields

        :param query: query from which to procure entries
        """
        self.query = query
        self.ticket_id = query[0]
        self.event_id = query[1]
        self.price = query[2]

    @classmethod
    def from_id(cls, ticket_id):
        """
        Converts an ID into the DB rep. of a ticket

        :param ticket_id: ID of ticket
        :return:    DB_Ticket, if ID valid
                    None, if ID invalid
        """
        found_ticket = ticket_csv.find_id_match(ticket_id)
        if not found_ticket:
            return None
        return DB_Ticket(found_ticket)

    @classmethod
    def delete_ticket(cls, ticket_id):
        """
        Deletes a ticket from the ticket CSV\

        :param ticket_id: ID of ticket to delete
        :return:
        """
        ticket_csv.delete_id_match(ticket_id)

    def save_ticket(self):
        """
        Updates or appends ticket to CSV
        :return:
        """
        ticket_csv.write_entry_id_match(self.ticket_id, self.query)
