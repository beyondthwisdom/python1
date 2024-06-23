print("------------------while döngüsü------------------")

"""
while koşul:
    # Koşul doğru olduğu sürece bu kod bloğu çalıştırılır

i = 1
a = 20
while i <= 5:
    print(i)
    i += 1  # i'yi 1 artır

user_input = ""
while user_input != "exit":
    user_input = input("İsminizi yazınız (exit ile çık): ")
    print("İsminiz:", user_input)

while True:
    user_input = input("Bir şey yazın (exit ile çık): ")
    if user_input == "exit":
        break  # Döngüyü kır
    print("Girdiğiniz:", user_input)


while True:
    user_input = input("Yaşınızı girin (0-120 arası): ")
    if user_input.isdigit():
        age = int(user_input)
        if 0 <= age <= 120:
            break
        else:
            print("Geçersiz yaş! Lütfen 0 ile 120 arasında bir değer girin.")
    else:
        print("Geçersiz giriş! Lütfen bir tam sayı girin.")
print("Girdiğiniz yaş:", age)


i = 6
while i <= 5:
    print(i)
    i += 1
else:
    print("Döngü sona erdi.")

i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue  # Çift sayıları atla
    print(i)

correct_password = "1234"
user_input = ""
i = 1

while user_input != correct_password and i <= 3:
    user_input = input("Şifreyi girin: ")
    i += 1
    if user_input == correct_password:
        print("Şifre doğru, hoş geldiniz!")
    else:
        print("Yanlış şifre, tekrar deneyin.")
print("3 deneme sonuna gelindi")        

"""
import random

target_number = random.randint(1, 100)
print(target_number)
guess = None

while guess != target_number:
    guess = int(input("1 ile 100 arasında bir sayı tahmin edin: "))
    if guess < target_number:
        print("Daha büyük bir sayı tahmin edin.")
    elif guess > target_number:
        print("Daha küçük bir sayı tahmin edin.")
    else:
        print("Tebrikler! Doğru tahmin.")

