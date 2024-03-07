from .models import User

class Blog:
    def __init__(self):
        self.users = []
        self.posts = []

# Method that will take in a password guess and return True if it matches the "private" password, else False 
    def create_new_user(self):
        # Get user info from input
        username = input('Please enter a username: ')
        # Check to see if a user with that username already exists
        if username in {u.username for u in self.users}:
            print(f"User with the username {username} already exists.")
        else:
            password = input('Please enter a password: ')
            # Create a new instance of User with the inputted info (imported at top)
            new_user = User(username, password)
            # Add the new user to the blog's user list
            self.users.append(new_user)
            print(f"{new_user} has been created.")