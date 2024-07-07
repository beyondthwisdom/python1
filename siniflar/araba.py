class Araba:
    def __init__(self, marka, model, yil):
        self.marka = marka
        self.model = model
        self.yil = yil

    def bilgileri_goster(self):
        print(f"Aracın markası: {self.marka} Aracın Modeli: {self.model} Aracın Yılı: {self.yil}" )

    def marka_degistir(self, yeni_marka):
        self.marka = yeni_marka
    