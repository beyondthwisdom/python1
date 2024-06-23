"""
print("-----------------------------------------------------------")

print("15", "+", "23" , 15 + 23)
print(f"15 + 23 = {15 + 23}")

print(int("15") + int("23"))

print(str(15) + str(23))
print(type(True))


print("-----------------------------------------------------------")
benim_yasim = 50
senin_yasin = input("yaşınızı giriniz: ")
fark = benim_yasim - int(senin_yasin)
yanyana = str(benim_yasim) + senin_yasin



print(f"Aramızdan {fark} yaş fark var")
print(f"Benim yasimla senin yasını yanyana yazınca {yanyana}")

print(str(float("124.9999999922611659999")) + " rakamı bir floattır")

print("------------------Type Çevirimleri------------------")
sayi_str = "123"
sayi_int = int(sayi_str)
print(sayi_int)  # Çıktı: 123
print(type(sayi_int))  # Çıktı: <class 'int'>

sayi_str = "123.45"
sayi_float = float(sayi_str)
print(sayi_float)  # Çıktı: 123.45
print(type(sayi_float))  # Çıktı: <class 'float'>

sayi_int = 123
sayi_str = str(sayi_int)
print(sayi_str)  # Çıktı: "123"
print(type(sayi_str))  # Çıktı: <class 'str'>

sayi_float = 123.45
sayi_str = str(sayi_float)
print(sayi_str)  # Çıktı: "123.45"
print(type(sayi_str))  # Çıktı: <class 'str'>

my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)  # Çıktı: (1, 2, 3)
print(type(my_tuple))  # Çıktı: <class 'tuple'>

my_tuple = (1, 2, 3)
my_list = list(my_tuple)
print(my_list)  # Çıktı: [1, 2, 3]
print(type(my_list))  # Çıktı: <class 'list'>

print("------------------Tarihler------------------")
from datetime import datetime

tarih_str = "2023-06-22"
tarih_obj = datetime.strptime(tarih_str, "%Y-%m-%d")
print(tarih_obj)  # Çıktı: 2023-06-22 00:00:00

true_str = "True"
false_str = "False"
true_bool = bool(true_str)
false_bool = bool(false_str)
print(type(true_bool))  # Çıktı: True
print(type(false_bool))  # Çıktı: True, çünkü boş olmayan her string True olarak değerlendirilir

import json

json_str = '{"isim": "Ali", "yas": 30}'
print(type(json_str))
python_obj = json.loads(json_str)
print(python_obj)  # Çıktı: {'isim': 'Ali', 'yas': 30}
print(type(python_obj))  # Çıktı: <class 'dict'>


sayi = int("dcf122")
print(sayi)
"""
print("------------------Mantıksal Çevirimler------------------")
print(bool(""))  # Çıktı: False
print(bool("vgfsdfgsdfsdf"))  # Çıktı: True
print(bool(0))  # Çıktı: False
print(bool(125+651561563))  # Çıktı: True




