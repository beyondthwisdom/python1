import sys, os, datetime, math, random, json


print("Python sürümü:", sys.version)
print("Komut satırı argümanları:", sys.argv)

print("Geçerli çalışma dizini:", os.getcwd())
#os.mkdir('moduller/btw_klasoru')

şu_an = datetime.datetime.now()
print("Şu an:", şu_an)

print("Pi sayısı:", math.pi)
print("Karekök (16):", math.sqrt(16))

import random

print("Rastgele sayı (0-1):", random.random())
print("Rastgele tam sayı (1-10):", random.randint(1, 10))

veri = {
    "isim": "Ali",
    "yas": 30,
    "sehir": "Istanbul"
}
json_veri = json.dumps(veri)
print("JSON verisi:", json_veri)
python_verisi = json.loads(json_veri)
print("Python verisi:", python_verisi)