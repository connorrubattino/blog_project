from .models import User, Post

class Blog:
    def __init__(self):
        self.users = []
        self.posts = []
        self.current_user = None
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


    # Method to log a user in by setting the current_user to a User instance
    def log_user_in(self):
        # Get the user credentials via input
        username_input = input('What is your username? ')
        password_input = input('What is your password? ')
        # Loop through the users in blog's user list
        for user in self.users:
            # Check if that user's username and password match the inputs
            if user.username == username_input and user.check_password(password_input):
                # If both are True, set the blog's current user to that user
                self.current_user = user
                print(f'{user} has logged in.')
                # Once we find the right user, we don't need to search any more
                break
        # if we go through the for loop without breaking, we know we have invalid credentials
        else:
            print('Username and/or password is incorrect.')

    
    # Method to log a user out by setting the current_user to None
    def log_user_out(self):
        username = self.current_user.username
        self.current_user = None
        print(f'{username} has successfully logged out')

    # Method to add a new post to the blog, authored by the logged in user
    def create_new_post(self):
        # Check to make sure we have a logged in user
        if self.current_user is None:
            print("You must be logged in to perform this action") # 401 Unauthorized Status Code
        else:
            # Get the title and body for the new post from input
            title = input("Enter new post title: ")
            body = input("Enter new post body: ")
            # Create a new instance of Post with the inputted info + logged in user
            new_post = Post(title, body, self.current_user)
            # Add the new post to the blog's posts list
            self.posts.append(new_post)
            print(f"{new_post.title} has been created!")
