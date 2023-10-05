from app.models import User
class Blog:
    def __init__(self):
        self.users = []
        self.posts = []

    #method to create a new uer instance and add to the blog's user list

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
            

