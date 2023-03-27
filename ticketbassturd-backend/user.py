from ticket import Ticket
from csv_reader import csvReader

user_csv = csvReader('DB/users.csv')

class User:
    def __init__(self, user_id, first_name, last_name, email, phone_num, passhash, ticket_history):
        """
        Construct filled user object, this should only be directly called when creating a new user account

        :param first_name:  User first name
        :param last_name:   User last name
        :param email:       User email
        :param phone_num:   User phone number (Optional)
        :param passhash:    Hash of users password
        """
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_num = phone_num
        self.passhash = passhash
        self.ticket_history = ticket_history

    @classmethod
    def from_id(cls, user_id):
        """
        Constructs a workable user object from an ID, does validation

        :param user_id: ID of user to construct
        :return:    User, if user valid
                    None, if user invalid
        """
        # Get and make sure user ID points to real user
        db_user = DB_User.from_id(user_id)
        if not db_user:
            return None

        # GENERATE USER OBJ ----------------------
        # Make sure all arguments can be converted without errors
        try:
            # CONVERT TICKET IDS TO TICKET OBJECTS
            mem_tickets = []
            for ticket_id in db_user.ticket_history.split(" "):
                mem_tick = Ticket.from_id(ticket_id)
                if mem_tick:
                    mem_tickets.append(mem_tick)
        except ValueError:
            return None

        return User(user_id, db_user.first_name, db_user.last_name,
                    db_user.email, db_user.phone_num, db_user.passhash,
                    mem_tickets)

    def to_db_user(self):
        """
        Construct a DB_User representation of this User object
        :return: the DB_User
        """
        # Convert tickets to IDs
        ticketstr = ""
        for ticket in self.ticket_history:
            ticketstr += ticket.ticket_id + " "
        # Remove last space
        ticketstr = ticketstr[:-1]

        return DB_User([self.user_id, self.first_name, self.last_name, self.email,
                        self.phone_num, self.passhash, ticketstr])

    def update_user(self):
        """
        Updates this user in the user CSV
        :return:
        """
        db_user = self.to_db_user()
        db_user.save_user()

    def delete_user(self):
        """
        Deletes this user in the CSV
        :return:
        """
        DB_User.delete_user(self.user_id)


class DB_User:
    """
    DB_User is the Database representation of an user
    mainly used as an intermediate state between DB query and usable fields
    """

    def __init__(self, query):
        """
        Parses a DB query into easily handleable fields

        :param query: query from which to procure entries
        """
        self.query = query
        self.user_id = query[0]
        self.first_name = query[1]
        self.last_name = query[2]
        self.email = query[3]
        self.phone_num = query[4]
        self.passhash = query[5]
        self.ticket_history = query[6]

    @classmethod
    def from_id(cls, user_id):
        """
        Converts an ID into the DB rep. of a user

        :param user_id: ID of user
        :return:    DB_User, if ID valid
                    None, if ID invalid
        """
        found_user = user_csv.find_id_match(user_id)
        if not found_user:
            return None
        return DB_User(found_user)

    @classmethod
    def delete_user(cls, user_id):
        """
        Deletes a user from the user CSV\

        :param user_id: ID of user to delete
        :return:
        """
        user_csv.delete_id_match(user_id)

    def save_user(self):
        """
        Updates or appends user to CSV
        :return:
        """
        user_csv.write_entry_id_match(self.user_id, self.query)

