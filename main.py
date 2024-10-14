import random
character = "abcdefghklmnopqrstuvwxyzABCGHKLMNOPQRSTUVWXYZ1234567890!#$&^*?-_😵‍💫☠️"
password_length = int(input("Şifre kaç karakter olsun : "))
password_count = int(input("Kaç adet şifre olsun : "))
for x in range(0, password_count):
        password = ""
        for x in range(0, password_length):
            password_char = random.choice(character)
            password      = password + password_char
        print("Rastgele Oluşturulan Şifreniz : " , password)
