from app import Blog

def run_blog():
    print("welcome to blog")
    #create an instance of the blog class
    blog = Blog()
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
            else:
                print(f'Option {to_do} is a work in progress')
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
                blog.log_user_out() ##names not working HERE


    #onche user quits
    print('Thanks for checking out the blog')
    print(blog.users)
    print(blog.posts)
    print('Goodbye!')

if __name__ =="__main__":
    run_blog()

# my_blog = Blog()

# print(my_blog)
# print(my_blog.users)
# print(my_blog.posts)

# my_blog.create_new_user()
# print(my_blog.users)
# print(my_blog.posts)

# my_blog.create_new_user()
# print(my_blog.users)
# print(my_blog.posts)

# my_blog.create_new_user()
# print(my_blog.users)
# print(my_blog.posts)
