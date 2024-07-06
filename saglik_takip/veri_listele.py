from veri_ekle import saglik_verileri

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