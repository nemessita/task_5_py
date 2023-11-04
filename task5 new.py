from datetime import datetime

dogum_gunu = input("GG-AA-YYYY: ")

indi = datetime.now()

dogum_tarixi = datetime.strptime(dogum_gunu, '%d-%m-%Y')

gecen_sure = indi - dogum_tarixi

saniye = gecen_sure.total_seconds()
deqiqe = saniye / 60
saat = deqiqe / 60
gun = saat / 24
ay = gun / 30.4375 

yas = int(indi.year - dogum_tarixi.year)

print(f"""qaqa
      {int(saniye):,} saniye 
      {int(deqiqe):,} deqiqə 
      {int(saat):,} saat 
      {int(gun):,} gün 
      {int(ay):,} ay
      sizin {yas} yaşiniz var.""")