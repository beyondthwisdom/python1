import datetime
import json
import os

# Veritabanı dosyası
DB_FILE = 'finanslar.json'

# Kişisel finans bilgilerini saklamak için bir sözlük
finanslar = {
    "gelirler": [],
    "giderler": [],
    "kategori_gelir": [],
    "kategori_gider": []
}

# Dosyadan veri yükleme
def veri_yukle():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, 'r') as file:
            return json.load(file)
    return finanslar

# Dosyaya veri kaydetme
def veri_kaydet():
    with open(DB_FILE, 'w') as file:
        json.dump(finanslar, file, default=str)

# Gelir veya gider ekleme fonksiyonu
def ekle(tur, miktar, kategori, tarih):
    finanslar[tur].append({
        "miktar": miktar,
        "kategori": kategori,
        "tarih": tarih
    })
    veri_kaydet()

# Kategori ekleme fonksiyonu
def kategori_ekle(tur, kategori):
    if kategori not in finanslar[tur]:
        finanslar[tur].append(kategori)
        veri_kaydet()

# Kategori silme fonksiyonu
def kategori_sil(tur, kategori):
    if kategori in finanslar[tur]:
        finanslar[tur].remove(kategori)
        veri_kaydet()

# Harcama analizi fonksiyonu
def harcama_analizi():
    kategoriler = {}
    for gider in finanslar["giderler"]:
        kategori = gider["kategori"]
        miktar = gider["miktar"]
        if kategori in kategoriler:
            kategoriler[kategori] += miktar
        else:
            kategoriler[kategori] = miktar
    return kategoriler

# Aylık bütçe analizi fonksiyonu
def aylik_butce_analizi(ay, yil):
    toplam_gelir = 0
    toplam_gider = 0
    for gelir in finanslar["gelirler"]:
        gelir_tarih = datetime.datetime.strptime(gelir["tarih"], "%Y-%m-%d")
        if gelir_tarih.month == ay and gelir_tarih.year == yil:
            toplam_gelir += gelir["miktar"]
    for gider in finanslar["giderler"]:
        gider_tarih = datetime.datetime.strptime(gider["tarih"], "%Y-%m-%d")
        if gider_tarih.month == ay and gider_tarih.year == yil:
            toplam_gider += gider["miktar"]
    return toplam_gelir, toplam_gider, toplam_gelir - toplam_gider

# Rapor oluşturma fonksiyonu (günlük, haftalık, yıllık)
def rapor_olustur(tur, tarih_baslangic, tarih_bitis):
    toplam_gelir = 0
    toplam_gider = 0
    for gelir in finanslar["gelirler"]:
        gelir_tarih = datetime.datetime.strptime(gelir["tarih"], "%Y-%m-%d")
        if tarih_baslangic <= gelir_tarih <= tarih_bitis:
            toplam_gelir += gelir["miktar"]
    for gider in finanslar["giderler"]:
        gider_tarih = datetime.datetime.strptime(gider["tarih"], "%Y-%m-%d")
        if tarih_baslangic <= gider_tarih <= tarih_bitis:
            toplam_gider += gider["miktar"]
    return toplam_gelir, toplam_gider, toplam_gelir - toplam_gider

# Ana menü
def ana_menu():
    global finanslar
    finanslar = veri_yukle()

    while True:
        print("\n1. Gelir Ekle")
        print("2. Gider Ekle")
        print("3. Harcama Analizi")
        print("4. Aylık Bütçe Analizi")
        print("5. Rapor Oluştur (Günlük/Haftalık/Yıllık)")
        print("6. Kategori Ekle")
        print("7. Kategori Sil")
        print("8. Çıkış")
        secim = input("Seçiminiz: ")
        
        if secim == "1":
            try:
                miktar = float(input("Gelir miktarı: "))
                kategori = input("Kategori: ")
                tarih = input("Tarih (YYYY-MM-DD): ")
                datetime.datetime.strptime(tarih, "%Y-%m-%d")  # Tarih doğrulama
                ekle("gelirler", miktar, kategori, tarih)
            except ValueError:
                print("Geçersiz giriş! Lütfen doğru formatta girin.")
        elif secim == "2":
            try:
                miktar = float(input("Gider miktarı: "))
                kategori = input("Kategori: ")
                tarih = input("Tarih (YYYY-MM-DD): ")
                datetime.datetime.strptime(tarih, "%Y-%m-%d")  # Tarih doğrulama
                ekle("giderler", miktar, kategori, tarih)
            except ValueError:
                print("Geçersiz giriş! Lütfen doğru formatta girin.")
        elif secim == "3":
            analiz = harcama_analizi()
            print("Kategoriye Göre Harcama Analizi:")
            for kategori, miktar in analiz.items():
                print(f"{kategori}: {miktar} TL")
        elif secim == "4":
            try:
                ay = int(input("Ay (1-12): "))
                yil = int(input("Yıl: "))
                gelir, gider, kalan = aylik_butce_analizi(ay, yil)
                print(f"Aylık Gelir: {gelir} TL")
                print(f"Aylık Gider: {gider} TL")
                print(f"Kalan Bütçe: {kalan} TL")
            except ValueError:
                print("Geçersiz giriş! Lütfen doğru formatta girin.")
        elif secim == "5":
            try:
                tur = input("Rapor Türü (günlük/haftalık/yıllık): ").strip().lower()
                tarih_baslangic = input("Başlangıç Tarihi (YYYY-MM-DD): ")
                tarih_bitis = input("Bitiş Tarihi (YYYY-MM-DD): ")
                tarih_baslangic = datetime.datetime.strptime(tarih_baslangic, "%Y-%m-%d")
                tarih_bitis = datetime.datetime.strptime(tarih_bitis, "%Y-%m-%d")
                gelir, gider, kalan = rapor_olustur(tur, tarih_baslangic, tarih_bitis)
                print(f"Gelir: {gelir} TL")
                print(f"Gider: {gider} TL")
                print(f"Kalan Bütçe: {kalan} TL")
            except ValueError:
                print("Geçersiz giriş! Lütfen doğru formatta girin.")
        elif secim == "6":
            try:
                tur = input("Tür (kategori_gelir/kategori_gider): ").strip().lower()
                kategori = input("Kategori: ")
                kategori_ekle(tur, kategori)
            except ValueError:
                print("Geçersiz giriş! Lütfen doğru formatta girin.")
        elif secim == "7":
            try:
                tur = input("Tür (kategori_gelir/kategori_gider): ").strip().lower()
                kategori = input("Kategori: ")
                kategori_sil(tur, kategori)
            except ValueError:
                print("Geçersiz giriş! Lütfen doğru formatta girin.")
        elif secim == "8":
            break
        else:
            print("Geçersiz seçim!")

# Programı çalıştır
ana_menu()
