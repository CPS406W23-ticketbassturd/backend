class User:
    def __init__(self, id, first_name, last_name, email, phone_num, pass):
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
        self.pass = pass
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
    
    
    
    def change_password(passhash):
    correct_password = passhash
    user_password = input("Please enter your password: ")

    if user_password == correct_password:
        print("Your password is correct.")

        change_password = input("Would you like to change your password? (Yes = 1 or No = 2): ")
        if change_password == 1:
            new_password = input("Enter your new password: ")
            confirm_password = input("Confirm your new password: ")
            if new_password == confirm_password:
                correct_password = new_password
                print("Your password has been changed successfully.")
            else:
                print("Passwords do not match.")
    else:
        print("Your password is incorrect.")
    
    def change_password(self):
        self.password = change_password(self.password)

    def change_user_info(self): 
        password_input = input("Enter your password to change user info: ")

        if password_input == self.password:
      
            print("What would you like to change?")
            print("1. First name")
            print("2. Last name")
            print("3. Email")
            print("4. Phone number")
            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                new_first_name = input("Enter your new first name: ")
                self.first_name = new_first_name
            elif choice == "2":
                new_last_name = input("Enter your new last name: ")
                self.last_name = new_last_name
            elif choice == "3":
                new_email = input("Enter your new email: ") 
                self.email = new_email
            elif choice == "4":
                new_phone_num = input("Enter your new phone number: ")
                self.phone_num = new_phone_num
            else:
                print("Invalid choice. Please try again.")
        else:
            print("Incorrect password. Please try again.")
