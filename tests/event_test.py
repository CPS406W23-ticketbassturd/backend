import sys
from datetime import datetime
sys.path.append('../')

from ticketbassturdbackend import csv_reader
from ticketbassturdbackend import event 

event_csv = csv_reader.csvReader('DB/events.csv')

class Event_test:

    def __init__(self):
        self = self

    @classmethod
    def test_from_id(cls):
        if (event.Event.from_id(-1) == None and event.Event.from_id(1) == event.Event(1,1,'Basketball Game','You will never be ballin','03/27/2023',0,10,50)):
            return True
        else:
            return False
    
    @classmethod
    def test_match_name(cls):
        if event.Event.match_name('base') != None:
            return True
        else:
            return False
    
    def test_to_db_event(cls):
        if event.Event.to_db_event():
            return True
        else:
            return False

    def test_update_event(cls):
        if event.Event.update_event():
            return True
        else:
            return False
    
    def test_delete_event(cls):
        if event.Event.delete_event():
            return True
        else:
            return False

    def test_date_valid(cls):
        if event.Event.date_valid('03/27/2023') == True or event.Event.date_valid('03/27/2023') == False:
            return True
        else:
            return False

    def test_at_capacity(cls):
        if event.Event.at_capacity() == True or event.Event.at_capacity() == False:
            return True
        else:
            return False