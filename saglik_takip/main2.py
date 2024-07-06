# Ana menü
import datetime
from veri_ekle import agirlik_ekle, kalori_ekle, su_ekle, egzersiz_ekle
from veri_listele import verileri_listele



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