import datetime

gorevler = []

def gorev_ekle(aciklama, son_tarih):
    # Görev bilgileri ile bir sözlük (dict) oluşturuyoruz
    
    gorev_id = len(gorevler) + 1

    gorev = {
        "id": gorev_id,
        "aciklama": aciklama,
        "son_tarih": son_tarih,
        "tamamlandi": False
    }
    # Görevi görevler listesine ekliyoruz
    gorevler.append(gorev)
    print(f"Yeni görev id niz: {gorev_id}")

# Görev tamamlama fonksiyonu
def gorev_tamamla(gorev_id):
    for gorev in gorevler:
        if gorev["id"] == gorev_id:
            gorev["tamamlandi"] = True
            break 

# Görevleri listeleme fonksiyonu
def gorevleri_listele():
    print("\nGörev Listesi:")
    for gorev in gorevler:
        durum = "Tamamlandı" if gorev["tamamlandi"] else "Tamamlanmadı"
        print(f"{gorev['id']}. {gorev['aciklama']} - Son Tarih: {gorev['son_tarih']} - Durum: {durum}")


def ana_menu():
    while True:
        # Kullanıcıya seçenekleri sunuyoruz
        print("\n1. Görev Ekle")
        print("2. Görev Tamamla")
        print("3. Görevleri Listele")
        print("4. Çıkış")
        secim = input("Seçiminiz: ")
        if secim == "1":
            # Kullanıcıdan görev bilgilerini alıyoruz
            aciklama = input("Görev açıklaması: ")
            son_tarih = input("Son tarih (YYYY-MM-DD): ")
            try:
                datetime.datetime.strptime(son_tarih, "%Y-%m-%d")  # Tarih doğrulama
                gorev_ekle(aciklama, son_tarih)
            except ValueError:
                print("Geçersiz tarih formatı! Lütfen YYYY-MM-DD formatında girin.")
        elif secim == "2":
            # Kullanıcıdan tamamlanacak görevin ID'sini alıyoruz
            gorevleri_listele()
            try:
                gorev_id = int(input("Tamamlanacak görevin ID'sini seçiniz: "))
                gorev_tamamla(gorev_id)
            except ValueError:
                print("Geçersiz ID formatı! Lütfen sayısal bir değer girin.")
            finally:
                gorevleri_listele()    
        elif secim == "3":
            # Görevleri listeleme
            gorevleri_listele()
        elif secim == "4":
            # Programdan çıkmak için döngüyü sonlandırıyoruz
            break
        else:
            print("Geçersiz seçim!")


ana_menu()