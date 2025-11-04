import json

from config import USER_DATA_json

try:
    with open(USER_DATA_json, "r") as f:
        read_json = json.load(f)
    
    for user in read_json:
        print(f"Name: {user['name']}, Age: {user['age']}") 
except FileNotFoundError:
    print('Fayl topilmadi!')
except json.decoder.JSONDecodeError:
    print('Fayl ichi bosh!')
        