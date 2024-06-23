print("------------------Şart İfadeleri------------------")
"""
if koşul:
    # Koşul doğruysa bu kod bloğu çalıştırılır

if kosul:

else:
    
if koşul1:
    # koşul1 doğruysa bu kod bloğu çalıştırılır
elif koşul2:
    # koşul1 yanlış, koşul2 doğruysa bu kod bloğu çalıştırılır
else:    

print("------------------Şart Örnekleri------------------")
sayi = int(input("sayiyi giriniz: "))
if sayi > 5:
    print("Sayı 5'ten büyüktür.")
elif sayi < 5:
    print("Sayı 5'ten kucuktur.")
else:
    print("Sayı 5'tir.")    

print("------------------and ve or kullanımı------------------")

sayi = int(input("sayiyi giriniz: "))
if sayi > 0 and sayi < 10:
    print("Sayı 0 ile 10 arasindadir")
elif sayi == 5:
    print("Sayı 5 tir")
else:
    print("Sayı 0 ile 10 arasinda değildir")

print("------------------koşullu atama------------------")
yas = int(input("yasi giriniz: "))

yetiskin = True if yas >= 18 else False
print("Yetişkin mi:", yetiskin)

print("------------------kullanıcı kontrolü------------------")
kullanici_adi = input("Kullanıcı adınızı girin: ")
sifre = input("Şifrenizi girin: ")

if kullanici_adi == "admin" and sifre == "1234":
    print("Giriş başarılı!")
else:
    print("Hatalı kullanıcı adı veya şifre.")

print("------------------Not sistemi------------------")

notum = int(input("Sınav notunuzu girin: "))

if notum >= 90:
    print("Harf notunuz: A")
elif notum >= 80:
    print("Harf notunuz: B")
elif notum >= 70:
    print("Harf notunuz: C")
elif notum >= 60:
    print("Harf notunuz: D")
else:
    print("Harf notunuz: F")

print("------------------Pozitif negatif kontrolü------------------")
sayi = float(input("Bir sayı girin: "))

if sayi > 0:
    print("Sayı pozitiftir.")
elif sayi < 0:
    print("Sayı negatiftir.")
else:
    print("Sayı sıfırdır.")

print("------------------Çift Tek Sayı Kotrolü------------------")
sayi = int(input("Bir sayı girin: "))

if sayi % 2 == 0:
    print("Sayı çifttir.")
else:
    print("Sayı tektir.")

And Mantıklaması
p * q
1   1  1
1   0  0
0   1  0
0   0  0

Or Mantıklaması
p + q
1   1  1
0   1  1
1   0  1
0   0  0


print("------------------Or Örneği------------------")
sayi = int(input("Bir sayı girin: "))
if sayi < 5 or sayi > 10:
    print("Sayı 5'ten küçük veya 10'dan büyüktür.")

print("------------------Not Örneği------------------")
sayi = 8
if !(sayi < 5):
    print("Sayı 5'ten küçük değildir.")

print("------------------Karşılaştırma Operatörleri------------------")
Eşitlik (==)

İki değerin eşit olup olmadığını kontrol eder.
a == b
Eşit Değil (!=)

İki değerin eşit olup olmadığını kontrol eder.
a != b
Büyüktür (>)

Sol taraftaki değerin sağ taraftaki değerden büyük olup olmadığını kontrol eder.
a > b
Küçüktür (<)

Sol taraftaki değerin sağ taraftaki değerden küçük olup olmadığını kontrol eder.
a < b
Büyük Eşittir (>=)

Sol taraftaki değerin sağ taraftaki değerden büyük veya eşit olup olmadığını kontrol eder.
a >= b
Küçük Eşittir (<=)

Sol taraftaki değerin sağ taraftaki değerden küçük veya eşit olup olmadığını kontrol eder.
a <= b

print("------------------Karşılaştırma Operatörleri Örnekleri------------------")

a = 10
b = 10
print(a != b)  # Çıktı: True

print("if li karşılaştırma")
if not(a==b):
    print(True)
else:
    print(False)    

a = 10
b = 5
c = 15
print(a > b and a < c)  # Çıktı: True

a = 5
print(1 < a < 10)  # Çıktı: True 
print(10 < a < 20)  # Çıktı: False


class MyClass:
    pass

class MyClass2:
    pass

nesne = MyClass()
nesne2 = MyClass2()

if type(nesne) == type(nesne2):
    print("nesne1 ve nesne2 nin typeları aynı")
else:
    print("nesne1 ve nesne2 nin typeları faklı")   

    
print("---------------Dinamik Sınıflar---------------------")

MyDynamicClass = type('MyDynamicClass', (object,), {'x': 5})

obj = MyDynamicClass()
print(type(obj))  # Çıktı: <class '__main__.MyDynamicClass'>
print(obj.x)  # Çıktı: 5


print("---------------isInstance---------------------")

x = 10
print(isinstance(x, int))  # Çıktı: True


class Araba:
    pass

class Toyota(Araba):
    pass

corolla = Toyota()

print(isinstance(corolla, Toyota))  # Çıktı: True
print(isinstance(corolla, Araba))  # Çıktı: True 
print(type(corolla) == Toyota)  # Çıktı: True
print(type(corolla) == Araba)  # Çıktı: False

print("---------------isdigit---------------------")

benim_yasim = 47
yas = input("yasinizi giriniz: ")

if yas.isdigit():
    if benim_yasim > int(yas):
        print("ben senden büyüğüm")  
    elif benim_yasim < int(yas):
        print("sen benden büyüksün")  
    else:
        print("ayni yasyayiz")        
else:
    print("lütfen sayısal bir deger giriniz")             
"""

