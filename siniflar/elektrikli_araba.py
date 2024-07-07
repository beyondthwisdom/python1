from araba import Araba

class ElektriliAraba(Araba):
    def __init__(self, marka, model, yil, batarya_kap):
        super().__init__(marka, model, yil)
        self.batarya_kap = batarya_kap

    def bilgileri_goster(self):
        super().bilgileri_goster()
        print(f"Batarya Kapasitesi: {self.batarya_kap} kWh")
