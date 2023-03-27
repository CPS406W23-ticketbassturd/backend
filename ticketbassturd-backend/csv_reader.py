import csv

class csvReader:
    def __init__(self, file):
        self.file = file

    def get_all_entries(self):
        with open(self.file, 'r') as file:
            reader = csv.reader(file, delimiter=",")
            return list(reader)

    def id_match(self, find_id):
        for entry in self.get_all_entries():
            if entry[0] == find_id:
                return entry
        return None

