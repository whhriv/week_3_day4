from app.models import User
class Blog:
    def __init__(self):
        self.users = []
        self.posts = []
        self.current_user = None #instance attribute

    #method to create a new user instance and add to the blog's user list

    def create_new_user(self):
        #get usr info from input
        username = input('Please enter usrname')
        #check to see if usr with usrname exists
        if username in [u.username for u in self.users]:
            print(f"User with the username {username} already exists")
        else:
            password = input('please enter your passwd')

            #create new instance of user with inputted info
            new_user = User(username, password)
            #add new user to the blog's user list
            self.users.append(new_user)
            print(f"{new_user} has been created")

#method to log a user in by setting the current_user to a User instance
    def log_user_in(self):
        #get the user credentials via input
        username = input('What is your username?')
        password = input('gimme your passswd')
        #loop through blog's user list
        for user in self.users:
            #check if uesr's name and pass math inputs
            if user.username == username and user.check_password(password):
                #if both are True, set blog's current user to that user
               
                self.current_user = user
                print(f"{user} has logged in.")
                #once we find correct user we don't need to search anymore
                break
        #if we go through FOR loop without breaking
        else:
            print('Username and/or password is incorrect')    

#method to log user out -- by setting current_user to None
def log_user_out(self):
    
    username = self.current_user.username
    self.current_user = None
    print(f'{username} has logged out')