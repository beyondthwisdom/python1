print("---------------regular expressions---------------------")
# r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def get_valid_name():
    while True:
        name = input("Adınızı girin: ")
        if name.strip():
            return name.strip()
        else:
            print("Geçersiz giriş! Lütfen boş bırakmayın.")

def get_valid_age():
    while True:
        user_input = input("Yaşınızı girin (0-120 arası): ")
        if user_input.isdigit():
            age = int(user_input)
            if 0 <= age <= 120:
                return age
            else:
                print("Geçersiz yaş! Lütfen 0 ile 120 arasında bir değer girin.")
        else:
            print("Geçersiz giriş! Lütfen bir tam sayı girin.")

def get_valid_email():
    while True:
        email = input("Email adresinizi girin: ")
        if is_valid_email(email):
            return email
        else:
            print("Geçersiz email formatı! Lütfen geçerli bir email adresi girin.")

# Kullanıcı bilgilerini al ve doğrula
name = get_valid_name()
age = get_valid_age()
email = get_valid_email()           

print("\nKullanıcı Bilgileri:")
print("\tAd:", name)
print("\tYaş:", age)
print("\tEmail:", email)