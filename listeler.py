print("---------------listeler---------------------")
"""
meyveler = ["elma", "muz", "çilek"]
print(meyveler)
matris = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
    ]



sayilar = [1, 2, 3, 4, 5]
print(sayilar)

matris = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
    ]
print("eleman değiştirme")
sayilar[2] = 8
print(sayilar)

print("sona eleman ekleme")
sayilar.append(6)
print(sayilar)

print("araya eleman ekleme")
sayilar.insert(3, 13)
print(sayilar)

print("eleman silme")
sayilar.remove(13)
print(sayilar)

print("son elemanı silme")
sayilar.pop(2)
print(sayilar)

print("tüm elemanları silme")
sayilar.clear()
print(sayilar)


sayilar = [1, 2, 2, 4, 17]
print(sayilar)
print("tüm elemanları sıralama")
sayilar.sort()
print(sayilar)

print("tüm elemanları terse çevirme")
sayilar.reverse()
print(sayilar)

print("elemanın indexini bulma")
print(sayilar.index(2))

print("listedeki elemanın sayısını bulma")
print(sayilar.count(17))

sayilar2 = [4, 6 ,7]
print(sayilar)
sayilar.extend(sayilar2)
print(sayilar)
sayilar.sort()
print(sayilar)
print(sayilar.count(4))

print("listeyi bölme")
sayılar = [1, 2, 3, 4, 5]
print(sayılar[1:3])  # Çıktı: [2, 3]
print(sayılar[:2])   # Çıktı: [1, 2]
print(sayılar[2:])   # Çıktı: [3, 4, 5]
print(sayılar[:])    # Çıktı: [1, 2, 3, 4, 5]
print(sayılar[::2])  # Çıktı: [1, 3, 5]

print("liste doldurma")
sayılar = [1, 2, 3, 4, 5]
kareler = [x**2 for x in sayılar]
print(kareler)  # Çıktı: [1, 4, 9, 16, 25]

çift_sayılar = [x for x in sayılar if x % 2 == 0]
print(çift_sayılar)  # Çıktı: [2, 4]




#print(matris[2][1])


class Meyve:
    def renk():
        pass
    def sekil():
        pass

elma = Meyve()
armut =Meyve()
muz= Meyve()

meyveler = [elma, armut, muz]

for meyve in meyveler:
    print(meyve.renk)


sayılar = [10, 20, 30, 40, 50]
i = 0

while i < len(sayılar):
    print(sayılar[i])
    i += 1

sayılar = [1, 2, 3, 4, 5]
toplam = 0

for sayı in sayılar:
    toplam += sayı

print("Toplam:", toplam)  # Çıktı: Toplam: 15
"""

matris = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for satır in matris:
    for eleman in satır:
        print(eleman, end=" ")
    print()
