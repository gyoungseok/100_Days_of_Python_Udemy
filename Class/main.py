# Learning class

# PascalCase
class User:
    def __init__(self, user_id, username) -> None:
        self.id = user_id
        self.username = username
        self.follower = 0    
        self.following = 0
        
    def follow(self, user):
        user.follower += 1
        self.following += 1

user_1 = User('001', 'Jayden')
#print(user_1.username)
user_2 = User('004', 'jack')
#print(user_2.id)


user_1.follow(user_2)
print(user_1.follower)
print(user_1.following)
print(user_2.follower)
print(user_2.following)

