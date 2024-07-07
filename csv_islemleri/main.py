import pandas as pd

df = pd.read_csv("inventory_csv.csv")

# Tedarikçi başına ürün sayısını, toplam değerini ve stokta 10'dan az olan ürünleri saklayacak sözlükler
tedarikci_basina_urun = {}
tedarikci_basina_toplam_deger = {}
onun_altinda_stok_urunler = {}

# Ürün listesinde her bir satır için döngü
for index, row in df.iterrows():
    tedarikci_adi = row['Supplier']
    envanter = row['Inventory']
    fiyat = row['Price']
    urun_numarasi = row['Product No']

    # Tedarikçi başına ürün sayısını hesaplama
    if tedarikci_adi in tedarikci_basina_urun:
        mevcut_urun_sayisi = tedarikci_basina_urun.get(tedarikci_adi)
        tedarikci_basina_urun[tedarikci_adi] = mevcut_urun_sayisi + 1
    else:
        tedarikci_basina_urun[tedarikci_adi] = 1    

    # Tedarikçi başına toplam envanter değerini hesaplama
    if tedarikci_adi in tedarikci_basina_toplam_deger:
        mevcut_toplam_deger = tedarikci_basina_toplam_deger.get(tedarikci_adi)
        tedarikci_basina_toplam_deger[tedarikci_adi] = mevcut_toplam_deger + envanter * fiyat
    else:
        tedarikci_basina_toplam_deger[tedarikci_adi] = envanter * fiyat

    # Stokta 10'dan az ürünü olanları belirleme
    if envanter < 10:
        onun_altinda_stok_urunler[int(urun_numarasi)] = int(envanter)

    # Toplam envanter fiyatını DataFrame'e ekleme
    df.at[index, 'Inventory Value'] = envanter * fiyat

# Sonuçları yazdır
print(tedarikci_basina_urun)
print(tedarikci_basina_toplam_deger)
print(onun_altinda_stok_urunler)

# Güncellenmiş CSV dosyasını kaydetme
df.to_csv("inventory_with_total_value.csv", index=False)