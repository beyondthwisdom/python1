# Sağlık verilerini saklamak için bir sözlük (dict)
saglik_verileri = {
    "agirlik": [],
    "kalori": [],
    "su": [],
    "egzersiz": []
}

# Ağırlık ekleme fonksiyonu
def agirlik_ekle(tarih, agirlik):
    kayit = {
        "tarih": tarih,
        "agirlik": agirlik
    }
    saglik_verileri["agirlik"].append(kayit)
            
 # Kalori alımı ekleme fonksiyonu
def kalori_ekle(tarih, kalori):
    kayit = {
        "tarih": tarih,
        "kalori": kalori
    }
    saglik_verileri["kalori"].append(kayit)

# Su tüketimi ekleme fonksiyonu
def su_ekle(tarih, su):
    kayit = {
        "tarih": tarih,
        "su": su
    }
    saglik_verileri["su"].append(kayit)

# Egzersiz ekleme fonksiyonu
def egzersiz_ekle(tarih, egzersiz, sure):
    kayit = {
        "tarih": tarih,
        "egzersiz": egzersiz,
        "sure": sure
    }
    saglik_verileri["egzersiz"].append(kayit)  