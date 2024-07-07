from matematik.islem import topla, cikar, carp, bol
from ogrenci.ogrenci import Ogrenci

# Değişkenler
sayi1 = 10
sayi2 = 5

# Fonksiyonları kullanarak matematik işlemleri yapalım
toplam = topla(sayi1, sayi2)
fark = cikar(sayi1, sayi2)
carpim = carp(sayi1, sayi2)
bolum = bol(sayi1, sayi2)

print(f"Toplam: {toplam}")
print(f"Fark: {fark}")
print(f"Çarpım: {carpim}")
print(f"Bölüm: {bolum}")

ogrenci1 = Ogrenci("Ali", "Veli", 20)
print(ogrenci1.ogrenci_bilgileri())