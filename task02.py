from config import USER_DATA_txt

try:
    
    with open(USER_DATA_txt, "r") as f:
        r = f.readlines()

    for word in r:
        print(word.strip())
except FileNotFoundError:
    print('Fayl topilmadi!')