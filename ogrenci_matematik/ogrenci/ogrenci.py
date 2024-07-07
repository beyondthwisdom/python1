# ogrenci.py

class Ogrenci:
    def __init__(self, ad, soyad, yas):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas

    def ogrenci_bilgileri(self):
        return f"Öğrenci: {self.ad} {self.soyad}, Yaş: {self.yas}"
