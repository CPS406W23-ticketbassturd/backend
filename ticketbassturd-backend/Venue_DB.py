import csv

class Venue:
    def __init__(self, venue_id, name, description, address, max_capacity):
        self.venue_id = venue_id
        self.name = name
        self.description = description
        self.address = address
        self.max_capacity = max_capacity

    # used to display the instance of the Venue class in a readable format
    def __repr__(self):
        return f"Venue(venue_id={self.venue_id}, name='{self.name}', description='{self.description}', address='{self.address}', max_capacity={self.max_capacity})"

    # from_csv_row and to_csv_row methods are used to convert the Venue instance to a list (CSV row) and vice versa
    @staticmethod
    def from_csv_row(row):
        venue_id, name, description, address, max_capacity = row
        return Venue(int(venue_id), name, description, address, int(max_capacity))

    @staticmethod
    def to_csv_row(venue):
        return [venue.venue_id, venue.name, venue.description, venue.address, venue.max_capacity]

    # load_all method loads all the venues from the venue.csv file and returns a list of Venue instances
    @classmethod
    def load_all(cls):
        venues = []
        with open('venue.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                venue = cls.from_csv_row(row)
                venues.append(venue)
        return venues

    # saves the list of Venue instances to the venue.csv file.
    @classmethod
    def save_all(cls, venues):
        with open('venue.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for venue in venues:
                row = cls.to_csv_row(venue)
                writer.writerow(row)
            
    # creates a new Venue instance and adds it to the list of venues, then saves the updated list to the venue.csv file and returns the newly created Venue instance
    @classmethod
    def add_venue(cls, name, description, address, max_capacity):
        venues = cls.load_all()
        last_id = venues[-1].venue_id if venues else 0
        venue_id = last_id + 1
        venue = Venue(venue_id, name, description, address, max_capacity)
        venues.append(venue)
        cls.save_all(venues)
        return venue

    # removes a venue with a given venue_id from the list of venues, saves the updated list to the venue.csv file, and returns nothing
    @classmethod
    def delete_venue(cls, venue_id):
        venues = cls.load_all()
        venues = [venue for venue in venues if venue.venue_id != venue_id]
        cls.save_all(venues)

