from flask import Flask
app = Flask(__name__)

class User:
    def __init__(self, name) -> None:
        self.name = name
        self.is_logged_in = False

def logged_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

@logged_decorator
def new_post(user):
    print(f"This is {user.name}'s new blog post.")

new_user = User("Vedant")
new_user.is_logged_in = True
new_post(new_user)
