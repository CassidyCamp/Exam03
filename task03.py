from config import USER_DATA_txt

count = 0
try:
    with open(USER_DATA_txt, "r") as f:
        r = f.readlines()

    for word in r:
        count+=1

    print(f'data.txt faylida {count} ta foydalanuvchi mavjud')
except FileNotFoundError:
    print('Fayl topilmadi!')