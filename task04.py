import json

from config import USER_DATA_json

getName = input('Enter Name: ')
getAge = input('Enter Age: ')

user = {'name': getName, 'age': getAge}

try:
    with open(USER_DATA_json, "r") as f:
        read_json = json.load(f)
        read_json.append(user)
    
    with open(USER_DATA_json, "w") as f:
        json.dump(read_json, f, indent=4)
                
except FileNotFoundError:
    with open(USER_DATA_json, "w") as f:
        l = [user]
        json.dump(l, f, indent=4)
except json.decoder.JSONDecodeError:
    with open(USER_DATA_json, "w") as f:
        l = [user]
        json.dump(l, f, indent=4)
        