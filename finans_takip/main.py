import datetime  # Tarih ve saat işlemleri için datetime modülünü içe aktarıyoruz.

# Kişisel finans bilgilerini saklamak için bir sözlük (dict) oluşturuyoruz.
# "gelirler" ve "giderler" anahtarları altında boş listeler bulunuyor.
finanslar = {
    "gelirler": [],
    "giderler": []
}

# Gelir veya gider eklemek için bir fonksiyon tanımlıyoruz.
def ekle(tur, miktar, kategori, tarih):
    # Verilen tür (gelirler veya giderler) listesine yeni bir sözlük (dict) ekliyoruz.
    finanslar[tur].append({
        "miktar": miktar,
        "kategori": kategori,
        "tarih": tarih
    })

# Harcamaları kategorilere göre analiz eden bir fonksiyon tanımlıyoruz.
def harcama_analizi():
    # Harcama kategorilerini ve toplam harcamaları saklamak için bir sözlük (dict) oluşturuyoruz.
    kategoriler = {}
    # Giderler listesi üzerinde döngü yaparak her bir gideri analiz ediyoruz.
    for gider in finanslar["giderler"]:
        kategori = gider["kategori"]
        miktar = gider["miktar"]
        # Eğer kategori daha önce eklenmişse, mevcut miktara ekliyoruz.
        if kategori in kategoriler:
            kategoriler[kategori] += miktar
        # Eğer kategori yeni ise, sözlüğe ekliyoruz.
        else:
            kategoriler[kategori] = miktar
    return kategoriler

# Aylık bütçeyi analiz eden bir fonksiyon tanımlıyoruz.
def aylik_butce_analizi(ay, yil):
    toplam_gelir = 0
    toplam_gider = 0
    # Gelirler listesi üzerinde döngü yaparak belirtilen ay ve yıla ait gelirleri topluyoruz.
    for gelir in finanslar["gelirler"]:
        gelir_tarih = gelir["tarih"]
        if gelir_tarih.month == ay and gelir_tarih.year == yil:
            toplam_gelir += gelir["miktar"]
    # Giderler listesi üzerinde döngü yaparak belirtilen ay ve yıla ait giderleri topluyoruz.
    for gider in finanslar["giderler"]:
        gider_tarih = gider["tarih"]
        if gider_tarih.month == ay and gider_tarih.year == yil:
            toplam_gider += gider["miktar"]
    # Toplam gelir, toplam gider ve kalan bütçeyi döndürüyoruz.
    return toplam_gelir, toplam_gider, toplam_gelir - toplam_gider

# Ana menü fonksiyonunu tanımlıyoruz.
def ana_menu():
    while True:
        # Kullanıcıya seçenekleri sunuyoruz.
        print("\n1. Gelir Ekle")
        print("2. Gider Ekle")
        print("3. Harcama Analizi")
        print("4. Aylık Bütçe Analizi")
        print("5. Çıkış")
        secim = input("Seçiminiz: ")
        
        if secim == "1":
            # Kullanıcıdan gelir bilgilerini alıyoruz.
            miktar = float(input("Gelir miktarı: "))
            kategori = input("Kategori: ")
            tarih = input("Tarih (YYYY-MM-DD): ")
            tarih = datetime.datetime.strptime(tarih, "%Y-%m-%d")
            # Gelirleri eklemek için fonksiyonu çağırıyoruz.
            ekle("gelirler", miktar, kategori, tarih)
        elif secim == "2":
            # Kullanıcıdan gider bilgilerini alıyoruz.
            miktar = float(input("Gider miktarı: "))
            kategori = input("Kategori: ")
            tarih = input("Tarih (YYYY-MM-DD): ")
            tarih = datetime.datetime.strptime(tarih, "%Y-%m-%d")
            # Giderleri eklemek için fonksiyonu çağırıyoruz.
            ekle("giderler", miktar, kategori, tarih)
        elif secim == "3":
            # Harcama analizini yapıp sonucu ekrana yazdırıyoruz.
            analiz = harcama_analizi()
            print("Kategoriye Göre Harcama Analizi:")
            for kategori, miktar in analiz.items():
                print(f"{kategori}: {miktar} TL")
        elif secim == "4":
            # Aylık bütçe analizini yapıp sonucu ekrana yazdırıyoruz.
            ay = int(input("Ay (1-12): "))
            yil = int(input("Yıl: "))
            gelir, gider, kalan = aylik_butce_analizi(ay, yil)
            print(f"Aylık Gelir: {gelir} TL")
            print(f"Aylık Gider: {gider} TL")
            print(f"Kalan Bütçe: {kalan} TL")
        elif secim == "5":
            # Programdan çıkmak için döngüyü sonlandırıyoruz.
            break
        else:
            print("Geçersiz seçim!")

# Programı çalıştırmak için ana menü fonksiyonunu çağırıyoruz.
ana_menu()
