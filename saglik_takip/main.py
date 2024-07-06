import datetime

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

# Verileri listeleme fonksiyonu
def verileri_listele():
    print("\nAğırlık Kayıtları:")
    for kayit in saglik_verileri["agirlik"]:
        print(f"Tarih: {kayit['tarih']} - Ağırlık: {kayit['agirlik']} kg")
    
    print("\nKalori Kayıtları:")
    for kayit in saglik_verileri["kalori"]:
        print(f"Tarih: {kayit['tarih']} - Kalori: {kayit['kalori']} kcal")
    
    print("\nSu Tüketimi Kayıtları:")
    for kayit in saglik_verileri["su"]:
        print(f"Tarih: {kayit['tarih']} - Su: {kayit['su']} litre")
    
    print("\nEgzersiz Kayıtları:")
    for kayit in saglik_verileri["egzersiz"]:
        print(f"Tarih: {kayit['tarih']} - Egzersiz: {kayit['egzersiz']} - Süre: {kayit['sure']} dakika")
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

# Ana menü
def ana_menu():
    while True:
        # Kullanıcıya seçenekleri sunuyoruz
        print("\n1. Ağırlık Ekle")
        print("2. Kalori Alımı Ekle")
        print("3. Su Tüketimi Ekle")
        print("4. Egzersiz Ekle")
        print("5. Verileri Görüntüle")
        print("6. Çıkış")
        secim = input("Seçiminiz: ")
        if secim == "1":
            # Kullanıcıdan ağırlık bilgilerini alıyoruz
            tarih = input("Tarih (YYYY-MM-DD): ")
            try:
                agirlik = float(input("Ağırlık (kg): "))
                datetime.datetime.strptime(tarih, "%Y-%m-%d")  # Tarih doğrulama
                agirlik_ekle(tarih, agirlik)
            except ValueError:
                print("Geçersiz giriş! Lütfen doğru formatta girin.")
        elif secim == "2":
            # Kullanıcıdan kalori alımı bilgilerini alıyoruz
            tarih = input("Tarih (YYYY-MM-DD): ")
            try:
                kalori = int(input("Kalori (kcal): "))
                datetime.datetime.strptime(tarih, "%Y-%m-%d")  # Tarih doğrulama
                kalori_ekle(tarih, kalori)
            except ValueError:
                print("Geçersiz giriş! Lütfen doğru formatta girin.")
        elif secim == "3":
            # Kullanıcıdan su tüketimi bilgilerini alıyoruz
            tarih = input("Tarih (YYYY-MM-DD): ")
            try:
                su = float(input("Su (litre): "))
                datetime.datetime.strptime(tarih, "%Y-%m-%d")  # Tarih doğrulama
                su_ekle(tarih, su)
            except ValueError:
                print("Geçersiz giriş! Lütfen doğru formatta girin.")
        elif secim == "4":
            # Kullanıcıdan egzersiz bilgilerini alıyoruz
            tarih = input("Tarih (YYYY-MM-DD): ")
            try:
                egzersiz = input("Egzersiz: ")
                sure = int(input("Süre (dakika): "))
                datetime.datetime.strptime(tarih, "%Y-%m-%d")  # Tarih doğrulama
                egzersiz_ekle(tarih, egzersiz, sure)
            except ValueError:
                print("Geçersiz giriş! Lütfen doğru formatta girin.")
        elif secim == "5":
            # Verileri listeleme
            verileri_listele()                
        elif secim == "6":
            # Programdan çıkmak için döngüyü sonlandırıyoruz
            break
        else:
            print("Geçersiz seçim!")

# Programı çalıştır
ana_menu()