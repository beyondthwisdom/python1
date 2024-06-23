print("---------------basit hata yakalama---------------------")
"""
#sayi = int(input("Bir sayı girin: "))
#print("Girdiğiniz sayı:", sayi)
try:
    sayi = int(input("Bir sayı girin: "))
    print("Girdiğiniz sayı:", sayi)
except ValueError:
    print("Geçersiz giriş! Lütfen bir sayı girin.")


print("---------------birden fazla hata yakalama---------------------")

try:
    sayi1 = int(input("Birinci sayıyı girin: "))
    sayi2 = int(input("İkinci sayıyı girin: "))
    sonuc = sayi1 / sayi2
    print("Sonuç:", sonuc)

except ValueError:
    print("Geçersiz giriş! Lütfen bir sayı girin.")
except ZeroDivisionError:
    print("Bir sayıyı sıfıra bölemezsiniz!")
except Exception:
    print("Bir Exception oluştu")     

print("---------------else blogu ile kullanım---------------------")
try:
    sayi1 = int(input("Birinci sayıyı girin: "))
    sayi2 = int(input("İkinci sayıyı girin: "))
    sonuc = sayi1 / sayi2
except ValueError:
    print("Geçersiz giriş! Lütfen bir sayı girin.")
except ZeroDivisionError:
    print("Bir sayıyı sıfıra bölemezsiniz!")
finally:
    print("program bitti")

try:
    sayi1 = int(input("Birinci sayıyı girin: "))
    sayi2 = int(input("İkinci sayıyı girin: "))
    sonuc = sayi1 / sayi2
except ValueError as e:
    print("Geçersiz giriş! Lütfen bir sayı girin. ", e)
except ZeroDivisionError as e:
    print("Bir sayıyı sıfıra bölemezsiniz!", e)
else:
    print("Sonuç:", sonuc)
"""
print("---------------Kendimize özel hata kontrolü---------------------")

class SayiHatasi(Exception):
    pass

def pozitif_sayi_kontrol(sayi):
    if sayi <= 0:
        raise SayiHatasi("Sayı pozitif olmalıdır!")
    return sayi

try:
    sayi = int(input("Pozitif bir sayı girin: "))
    pozitif_sayi_kontrol(sayi)
except SayiHatasi as e:
    print("Hata:", e)
except ValueError:
    print("Geçersiz giriş! Lütfen bir sayı girin.")
else:
    print("Girdiğiniz sayı:", sayi)