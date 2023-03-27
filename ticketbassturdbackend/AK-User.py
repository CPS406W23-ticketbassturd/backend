class User:
    
    curr = {}
    
    def __init__(self, id, first_name, last_name, email, number, password):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.number = number
        self.password = password
        if self.id in User.curr.keys():
           print("User already exists!")
        else:
            User.curr[id] = (first_name, last_name, email, number, password)
            print("User successfully created!")
            
            
    def delete(self, id):
        if id not in User.curr.keys(): print("Enter valid ID")
        else: User.curr.pop(id)
