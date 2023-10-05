

class User:
    id_counter = 1

    def __init__(self, username, password):
        self.id = User.id_counter
        User.id_counter +=1
        self.username = username
        self.password = password

    def __str__(self):
        return self.username
    
    def __repr__(self):
        return f"<user {self.id}|{self.username}>"
    #method that will take in a password guess and return True if it matches the "PRIVATE passwd" else returns False
    def check_password(self, password_guess):
        return self.__password == password_guess
    

    
