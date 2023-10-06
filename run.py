from app import Blog
from app.models import Post, User
def run_blog():
    print("welcome to blog")
    #create an instance of the blog class
    blog = Blog()
    
    #CREATE SOME INITIAL DATA
    user1 = User('brians', 'abc123')  #temp data
    user2 = User('jumpman23', '6rings')#temp data
    blog.users.append(user1)#temp data
    blog.users.append(user2)#temp data
    post1 = Post('Friday', 'it is friday', user1)#temp data
    post2 = Post('weekend', 'i am ready for weekend', user2)#temp data
    blog.posts.append(post1)#temp data
    blog.posts.append(post2)#temp data
   
   
    #start "running" our blog until user quits
    while True:
        if blog.current_user is None:

            #print menu options
            print("1 sign up\n2. login \n 3. view all posts\n 4. view single position\n5. quit")
            #ask user what they want to do
            to_do = input('which option woult you like to do?')
            #while user inputs an invalid option
            while to_do not in {'1','2','3','4','5',}:
                #redefine to_do with a new input
                to_do = input('invalid option, please choose 1,2,3,4,5')
            if to_do == '5':
                break
            elif to_do == '1':
                #call the create new user method on the blog
                blog.create_new_user()
            elif to_do == '2':
                blog.log_user_in()
            # else:
            #     print(f'Option {to_do} is a work in progress')
            elif to_do == '3':
                blog.view_posts()
            elif to_do == '4':
                post_id = input('What is the ID of the post you would like to view?')
                #if the post is not a digit, reask
                while not post_id.isdigit():
                    post_id = input('Invalid ID.  Must be INT, try again')
                #Call the view single post method with int version of post_id
                blog.view_post(int(post_id))
        else:
            #print menu options for a logged in user
            print("1. signout\n2. create post\n3. view all posts\n4. view single posts\n5. edit a post\n6. delete a post")
            #ask the user what they want to do
            to_do = input('which option do you want?')
            #while user inputs an invalid optionion
            while to_do not in {'1','2','3','4','5',}:
                #redefine to_do with new input
                to_do = input('invalid option, please choose 1-5')
            if to_do == '1':
                blog.log_user_out() ##names not working HERE - got fxn from indenting blog.py def log_user_out
            elif to_do == '2':
                blog.create_new_posts()
            elif to_do == '3':
                blog.view_posts()
            elif to_do == '4':
                post_id = input('What is the ID of the post you would like to view?')
                #if the post is not a digit, reask
                while not post_id.isdigit():
                    post_id = input('Invalid ID.  Must be INT, try again')
                #Call the view single post method with int version of post_id
                blog.view_post(int(post_id))
            elif to_do == '5':
                post_id = input('What is the ID of the post you would like to view?')
                #if the post is not a digit, reask
                while not post_id.isdigit():
                    post_id = input('Invalid ID.  Must be INT, try again')
                #Call the view single post method with int version of post_id
                blog.view_post(int(post_id))


    #once user quits
    print('Thanks for checking out the blog')
    print(blog.users)
    print(blog.posts)
    print('Goodbye!')


#if this is executed
if __name__ == "__main__":
    run_blog()


