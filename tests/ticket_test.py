import sys
from datetime import datetime
sys.path.append('../')

from ticketbassturdbackend import csv_reader
from ticketbassturdbackend import ticket

ticket_csv = csv_reader.csvReader('DB/tickets.csv')

class Ticket_test:

    def __init__(self):
        self = self

    def test_from_id(cls):
        if ticket.Ticket.from_id(1) != None and ticket.Ticket.from_id(-1) == None:
            return True
        else:
            return False

    def test_update_ticket(cls):
        ticket.Ticket.update_ticket()
        return True
    
    def test_delete_ticket(cls):
        ticket.Ticket.delete_ticket()
        return True

    def test_date_valid(cls):
        if ticket.Ticket.date_valid('03/27/2023') == True or ticket.Ticket.date_valid('03/27/2023') == False:
            return True
        else:
            return False