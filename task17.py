import json
from config import USER_info_DATA_json

class User:
    def __init__(self, username, email, is_active):
       self.username = username
       self.email = email
       self.is_active = is_active
    
    def save(self):
        get_user = {'username': self.username, 'email': self.email, 'is_active': self.is_active}
        found = False
        try:
            with open(USER_info_DATA_json, "r") as f:
                read_json = json.load(f)
            
            for user in read_json:
                if user['username'].lower() == get_user['username'].lower():
                    found = True                
                    user['email'] = get_user['email']
                    user['is_active'] = get_user['is_active']
                
            if not found:
                read_json.append(get_user)
            
            with open(USER_info_DATA_json, "w") as f:
                json.dump(read_json, f, indent=4)
                        
        except FileNotFoundError:
            with open(USER_info_DATA_json, "w") as f:
                l = [get_user]
                json.dump(l, f, indent=4)
        except json.decoder.JSONDecodeError:
            with open(USER_info_DATA_json, "w") as f:
                l = [get_user]
                json.dump(l, f, indent=4)      
    
    def deactivate(self):
        self.is_active = False
        return self.is_active
    
us1 = User("Daler", 'Daler@gamil.com', True)
us2 = User("Samandar", 'Samandar@gamil.com', True)
us1.save()
us1.deactivate()
us1.save()
