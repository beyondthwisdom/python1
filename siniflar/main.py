from araba import Araba 
from elektrikli_araba import ElektriliAraba

arac1 = Araba("Mercedes",
              "E320",
              2024)

arac2 = Araba("Toyota",
              "Corolla",
              2023)

arac3 = Araba("Audi",
              "R8",
              2025)


arac4 = ElektriliAraba("Tesla", "Model3" , 2024, "75")

arac4.bilgileri_goster()


#arac1.bilgileri_goster()
#arac2.bilgileri_goster()
#arac3.bilgileri_goster()

#arac1.marka_degistir("Honda")

#arac1.bilgileri_goster()
