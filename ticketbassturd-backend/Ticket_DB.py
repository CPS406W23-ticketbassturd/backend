import csv
from Event_DB import Events
from datetime import date

class Ticket:
    def __init__(self, ticket_id, event, price, date):
        self.ticket_id = ticket_id
        self.event = event
        self.price = price
        self.date = date

    # takes a date string in the format YYYY-MM-DD and checks if it's a valid date
    @staticmethod
    def is_valid_date(date_string):
        try:
            year, month, day = map(int, date_string.split('-'))
            date(year, month, day)
            return True
        except ValueError:
            return False

    # takes a Ticket object and appends it to the tickets.csv file
    @classmethod
    def add_ticket(cls, ticket):
        with open('tickets.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([ticket.ticket_id, ticket.event.event_id, ticket.price, ticket.date.strftime('%Y-%m-%d')])
    
    # takes a ticket_id and deletes the corresponding row from the tickets.csv file
    @classmethod
    def delete_ticket(cls, ticket_id):
        with open('tickets.csv', mode='r') as file:
            reader = csv.reader(file)
            rows = [row for row in reader if row[0] != ticket_id]
        with open('tickets.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            for row in rows:
                writer.writerow(row)
    
    # takes an Event object and returns a list of Ticket objects for that event by reading the tickets.csv file and filtering rows based on the event id
    @classmethod
    def get_tickets_for_event(cls, event):
        with open('tickets.csv', mode='r') as file:
            reader = csv.reader(file)
            tickets = []
            for row in reader:
                if row[1] == event.event_id:
                    ticket = cls(row[0], event, row[2], date.fromisoformat(row[3]))
                    tickets.append(ticket)
        return tickets
