class User:
    '''Contins the User Info '''
    def __init__(self,user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    
    def follow(self,user):
        '''Expects a user object and increase the followers of user while also increasing the following of self'''
        self.following += 1
        user.followers += 1

# Making User 1 obj from User Class
user_1 = User(1,"yujan")

# Making User 2 obj from User Class
user_2 = User(2, "naruto")

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)

print(user_2.followers)
print(user_2.following)
