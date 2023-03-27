import csv
from typing import List
from Ticket_DB import Ticket

class Account:
    def __init__(self, id: int, first_name: str, last_name: str, email: str, phone_number: str, password: str, tickets: List[Ticket]):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.password = password
        self.tickets = tickets

    def add_tickets(self, tickets: List[Ticket]):
        self.tickets.extend(tickets)
        self.update_csv()

    def get_tickets(self):
        return self.tickets

    def change_first_name(self, new_first_name: str):
        self.first_name = new_first_name
        self.update_csv()

    def change_last_name(self, new_last_name: str):
        self.last_name = new_last_name
        self.update_csv()

    def change_email(self, new_email: str):
        self.email = new_email
        self.update_csv()

    def change_phone_number(self, new_phone_number: str):
        self.phone_number = new_phone_number
        self.update_csv()

    def change_password(self, new_password: str):
        self.password = new_password
        self.update_csv()

    def update_csv(self):
        with open('accounts.csv', 'r') as file:
            reader = csv.reader(file)
            accounts_list = list(reader)

        for i in range(len(accounts_list)):
            if accounts_list[i][0] == str(self.id):
                accounts_list[i] = [str(self.id), self.first_name, self.last_name, self.email, self.phone_number, self.password, ",".join([str(ticket.id) for ticket in self.tickets])]

        with open('accounts.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(accounts_list)

    @staticmethod
    def add_account(account: Account):
        with open('accounts.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([str(account.id), account.first_name, account.last_name, account.email, account.phone_number, account.password, ",".join([str(ticket.id) for ticket in account.tickets])])

    @staticmethod
    def delete_account(account_id: int):
        with open('accounts.csv', 'r') as file:
            reader = csv.reader(file)
            accounts_list = list(reader)

        with open('accounts.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for account in accounts_list:
                if account[0] != str(account_id):
                    writer.writerow(account)
