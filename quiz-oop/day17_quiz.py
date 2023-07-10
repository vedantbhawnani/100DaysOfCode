class User:
    def __init__(self, user_id, user_name) -> None:
        print(f"new user being created with id {user_id}.... Please wait...")
        self.id = user_id
        self.name = user_name
        self.followers = 0
        self.following = 0

    def follow(self, user) -> None:
        user.followers += 1
        self.following += 1


user_1 = User("001", "Vedant")
user_2 = User("002", "Aaryan")
user_1.follow(user_2)
print(user_2.followers)
print(user_1.following)
