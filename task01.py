from config import USER_DATA_txt

getName = input('Enter Name: ')
getAge = input('Enter Age: ')

with open(USER_DATA_txt, "a") as f:
    f.write(f'{getName} - {getAge} yosh\n')