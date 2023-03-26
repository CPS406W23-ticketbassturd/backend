class User:
    def __init__(self, id, first_name, last_name, email, phone_num, passhash):
        """
        Construct filled user object, this should only be directly called when creating a new user account

        :param first_name:  User first name
        :param last_name:   User last name
        :param email:       User email
        :param phone_num:   User phone number (Optional)
        :param passhash:    Hash of users password
        """
        # TODO: Input type validation
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_num = phone_num
        self.passhash = passhash
        #TODO: Generate ID Based on global ID function

    # FROM ID LOADS USER IN DB INTO WORKING MEMORY FOR CHANGES AND ACCESSING
    # FOR CHANGES TO OCCUR SERVER SIDE, STORE MUST HAPPEN
    @classmethod
    def fromID(cls, user_id):
        """
        Construct working memory copy of user from DB

        :param user_id: ID of requested user
        :return: User if ID is valid, None if ID invalid
        """
        #TODO: Generate user from query w/ ID
        return User(user_id, None, None, None, None, None)

    # SAVES ACCOUNT TO SERVER
    def save_account(self):
        # TODO: Store user somehow (magic)
        return True
