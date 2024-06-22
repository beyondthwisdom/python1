print("------------String birleştirme---------------------")
print("Sıcaklık:", 25, "derece")
print(f"Toplam: {100 + 250} TL")
print("Skor: " + str(85) + " puan")
print("------------Matematiksel İşlemler---------------------")
print("Toplama: ", 10 + 5)
print("Çıkarma: ", 10 - 5)
print("Çarpma: ", 10 * 5)
print("Bölme: ", 10 / 5)
print("Üs Alma: ", 2 ** 3)
print("Mod Alma: ", 10 % 3)
print("------------Detaylı Matematiksel İşlemler-----------------------")
print("5 + 3 =", 5 + 3)
print("10 - 4 =", 10 - 4)
print("7 * 6 =", 7 * 6)
print("8 / 2 =", 8 / 2)
print("3^4 =", 3 ** 4)
print("14 % 5 =", 14 % 5)
print("----------------Değişken Kullanımı------------------")
a = 5
b = 7
print(f"{a} sayısıyla {b} sayısının toplamı  = {a + b} dir")

print("------------------Karmaşık Aritmetik İşlemler-----------------------")
p = 3
q = 4
r = 5
sonuc = (p + q) * r - (q / p) ** r
print(f"({p} + {q}) * {r} - ({q} / {p}) ^ {r} = {sonuc}")
print("------------------Reserved Word kullanımı-----------------------")
"""
False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield
"""
print("-------------------Metodlar--------------------------------")
"""
def fonksiyon_adi(parametre1, parametre2):
    # Bu blok fonksiyonun gövdesidir
    # Burada yapılacak işlemler tanımlanır
    sonuc = parametre1 + parametre2
    return sonuc
"""

print("-------------------Zorunlu Parametre Kullanımı---------------")
def toplama(parametre1, parametre2):
    # Bu blok fonksiyonun gövdesidir
    # Burada yapılacak işlemler tanımlanır
    sonuc = parametre1 + parametre2
    return sonuc

sonuc = toplama (3, 5)
print(f"{3} + {5} = {sonuc}")

print("-------------------Ön Değerli Parametre Kullanımı---------------")
def bilgi_goster(isim, yas):
    print(f"İsim: {isim}, Yaş: {yas}")

bilgi_goster(yas=30, isim="Ali")

print("-------------------Değişken sayıda Parametre Kullanımı---------------")
def toplama(*args):
    return sum(args)

print(toplama(1, 2, 3, 4, 5, 7, 9)) 

print("-------------------Basit fonksiyonlar---------------")
def merhaba_de():
    print("Merhaba, Dünya!")
merhaba_de()  # Çıktı: Merhaba, Dünya!

print("-------------------parametreli fonksiyonlar---------------")  
def toplama1(a, b):
  return a + b

sonuc = toplama1(5, 3)
print(sonuc)  # Çıktı: 8
print("-------------------varsayılan parametreli fonksiyonlar---------------")  
def selamla(isim="Misafir"):
    print(f"Merhaba, {isim}!")

selamla()         # Çıktı: Merhaba, Misafir!
selamla("Ahmet")  # Çıktı: Merhaba, Ahmet!

print("-------------------değişken sayılı parametreli fonksiyonlar---------------")  
def toplama2(*args):
    return sum(args)

print(toplama2(1, 2, 3))      # Çıktı: 6
print(toplama2(1, 2, 3, 4, 5))  # Çıktı: 15

print("-------------------DocString---------------")  
def toplama3(a, b):
    """
    İki sayının toplamını döndürür.

    Parametreler:
    a (int): İlk sayı
    b (int): İkinci sayı

    Döndürür:
    int: İki sayının toplamı
    """
    return a + b

"""help(toplama3)  # Fonksiyonun docstring'ini gösterir"""

print("-------------------Yerel Scope---------------")  
"""
def my_function():
    local_var = 10  # Yerel değişken
    print(local_var)  # Bu fonksiyon içinde erişilebilir

my_function()
print(local_var)  # Hata verir, çünkü local_var fonksiyon dışında tanımlı değil
"""
print("-------------------Kapsayıcı Scope---------------") 
def outer_function():
    enclosing_var = "dış değişken"

    def inner_function():
        print(enclosing_var)  # Kapsayan değişkene erişebilir

    inner_function()

outer_function()
print("-------------------NonLocal Scope---------------") 
def outer_function():
    enclosing_var = "dış değişken"

    def inner_function():
        nonlocal enclosing_var
        enclosing_var = "değiştirildi"
    
    inner_function()
    print(enclosing_var)  # Çıktı: değiştirilmiş

outer_function()
















print("-----------------------------------------------------------")








