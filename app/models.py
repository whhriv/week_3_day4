from random import randint
from ascii_magic import AsciiArt

class User:
    id_counter = 1

    def __init__(self, username, password):
        self.id = User.id_counter
        User.id_counter +=1
        self.username = username
        self.__password = password #mod __pass
        self.image_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/132.png"

    def __str__(self):
        return self.username
    
    def __repr__(self):
        return f"<user {self.id}|{self.username}>"
    #method that will take in a password guess and return True if it matches the "PRIVATE passwd" else returns False
    def check_password(self, password_guess):
        return self.__password == password_guess ##self.__password original
    
    #method that will print the user's image to terminal
    def display_image(self):
        prof_image = AsciiArt.from_url(self.image_url)
        prof_image.to_terminal()
      
    
class Post:
    id_counter = 1

    def __init__(self, title, body, author):
        """
        Title:str
        body: str
        author: User (instance of user)
        """
        self.id = Post.id_counter
        Post.id_counter +=1
        self.title = title
        self.author = author

    def __str__(self):
        return f"""
        {self.id} - {self.title}
        by: {self.author}
        {self.body}
        """
    def __repr__(self):
        return f"<Post {self.id}|{self.title}>"
    
