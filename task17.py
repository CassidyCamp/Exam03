class User:
    def __init__(self, username, email, is_active):
       self.username = username
       self.email = email
       self.is_active = is_active
    
    def save(self):
        return {'username': self.username, 'email': self.email, 'is_active': self.is_active}
    
    def deactivate(self):
        self.is_active = False
        return self.is_active
    
us1 = User("Daler", 'Daler@gamil.com', True)
print(us1.deactivate())
print(us1.save())