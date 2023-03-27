import csv

class csvReader:
    def __init__(self, file):
        self.file = file

    def get_all_entries(self):
        with open(self.file, 'r') as file:
            reader = csv.reader(file, delimiter=",")
            return list(reader)

    def find_id_match(self, find_id):
        for entry in self.get_all_entries():
            if entry[0] == find_id:
                return entry
        return None

    def delete_id_match(self, del_id):
        with open(self.file, 'w', newline='\n') as events_file:
            writer = csv.writer(events_file, delimiter=",")
            for entry in self.get_all_entries():
                if entry[0] != del_id:
                    writer.writerow(entry)

    def write_entry_id_match(self, write_id, write_entry):
        overwrote = False
        with open(self.file, 'w', newline='\n') as events_file:
            writer = csv.writer(events_file, delimiter=",")
            for entry in self.get_all_entries():
                if entry[0] != write_id:
                    writer.writerow(entry)
                else:
                    overwrote = True
                    writer.writerow(write_entry)
            if not overwrote:
                writer.writerow(write_entry)

