############# ##############
# İndex seçimlerinde NumPy - Index Selection
######

import numpy as np
a =np.random.randint(10, size=12)
a.reshape(3,4)

a[0]
a[0:7]  # dilimleme işlemidir > :
a[3] = 23 # bu şekilde değiştiriliebilir


k = np.random.randint(10, size=(3,6))  # 3 satır 6 sütunlu bir array oluştur 0-10 arasında

k[0,1] # 0 daki satır 1.sütunu ekrana verir
k[2,0]
k[1,1]

# değiştirelim

k [2,3] = 99 # şeklinde değiştirdik

# NUMPY FIXTYPE YANİ SABİT BİR ARRAYDİR. VERİYİ HIZLI SAKLAMAK İÇİN TEK BİR TİP SAKLAR YANİ 2.9 YERİNDE 2 ALIR
k [2,3] = 120.30  # 120 olarak aldı

# SATIR VE SÜTUNLARDA ARALIK SEÇME İŞLEMİ

k[0:2, 0:3]
