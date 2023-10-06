from app.models import User, Post
class Blog:
    def __init__(self):
        self.users = []
        self.posts = []
        self.current_user = None #instance attribute

    #Private method that will get a post by it's ID or return none if no post with that ID
    def _get_post_from_id(self, post_id):
        #loop through all of the posts in the blog
        for post in self.posts:
        #if post's ID matches the post_id argument
            if post.id == post_id:
                #return post instance
                return post
        #if we finish the loop, that means most ID does not exist
        return post

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
            new_user = User(username, password)  #User instance
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

#method to add a new post to the blog, authored by the logged in user
    def create_new_posts(self):
        #check to makesure user is logged it
        if self.current_user is not None:
            #Get the title and body for the new post from input
            title=input('enter new post title')
            body = input('enter new post body')
            #create a new instance of Post with the inputted into + logged in user
            new_post = Post(title, body, self.current_user)
            #add the new post to blog's post list
            self.posts.append(new_post)
            print(f'{new_post.title} has been created')
            
        else:
            print('gotta be logged in to post, yo') #401 unauthorized/no permissions

    #method to view all posts
    def view_posts(self):
        #check if there are any posts
        if self.posts:

            #loop through the blog's post list
            for post in self.posts:
                #print the posts( __str__ already formats it for us)
                print(post)
        else:
            print('There are currently no posts for this blog')

    #method to view a SINGLE post by ID
    def view_post(self, post_id):
        post = self._get_post_from_id(post_id)
        if post:
            print(post)
        else:
            print(f"post with an ID of {post_id} does not exist") #404 not found

    #method to edit post by ID
    def edit_post_method(self, post_id):
        post = self._get_post_from_id(post_id)
        if post:
            #check to see if logged in user is author or post
            if post.author == self.current_user:
                #print the post so the user can see what they are editing
                print(post)

                #ask for new title or have them skip to keep
                new_title = input("Enter new title or type 'skip' to keep current title")
                if new_title.lower() != 'skip':
                    #set title attribute on post to the new title
                    post.title = new_title

                new_body = input("Enter new title or type 'skip' to keep current title")
                if new_body.lower() != 'skip':
                    #set body attribute on post to the new title
                    post.body = new_body
            #if the user is logged in but not the author
            elif self.current_user is not None:
                print("You don't have permission to edit this post") #403 forbidden
            else: 
                print("you must be logged in to perform this action")    #401 unauthorized
                

        else:
            print(f"Post with an ID of {post_id} does not exist")
