import csv
from datetime import datetime
from Venue_DB import Venue

class Events:
    def __init__(self):
        self.events_db = 'events.csv'
        self.venue_db = 'venue.csv'

    # also checks if the venue exists, if the date is valid, and if the event exceeds the venue capacity
    def add_event(self, account_id, name, description, num_attendees, date, venue_id):
        with open(self.venue_db, 'r') as venue_file:
            reader = csv.reader(venue_file)
            for row in reader:
                if row[0] == venue_id:
                    venue = Venue(*row)
                    break
            else:
                return "Venue not found"

        if not self.is_valid_date(date):
            return "Invalid date"

        if num_attendees > venue.max_capacity:
            return "Event exceeds venue capacity"

        event_id = self.get_next_event_id()
        new_event = [str(event_id), str(account_id), name, description, str(num_attendees), date.strftime('%m/%d/%Y'), str(venue_id)]

        with open(self.events_db, 'a', newline='') as events_file:
            writer = csv.writer(events_file)
            writer.writerow(new_event)

        return event_id

    def delete_event(self, event_id):
        events = self.get_all_events()
        event_deleted = False
        with open(self.events_db, 'w', newline='') as events_file:
            writer = csv.writer(events_file)
            for event in events:
                if event[0] == str(event_id):
                    event_deleted = True
                    continue
                writer.writerow(event)

        return event_deleted

    def is_valid_date(self, date_string):
        try:
            date = datetime.strptime(date_string, '%m/%d/%Y')
            return date >= datetime.now()
        except ValueError:
            return False

    def has_reached_capacity(self, event_id):
        events = self.get_all_events()
        for event in events:
            if event[0] == str(event_id):
                return int(event[4]) >= Venue(event[6]).max_capacity
        return False

    def get_all_events(self):
        with open(self.events_db, 'r') as events_file:
            reader = csv.reader(events_file)
            return list(reader)

    def get_next_event_id(self):
        events = self.get_all_events()
        if not events:
            return 1
        return int(events[-1][0]) + 1