###############################
# Yeniden şekillendirme ( Reshaping )
##########

import numpy as np

# boyutunu değiştirmek için reshaping kullanılır

np.random.randint(1,10,size=9) # rastegele olarak 1 ile 10 arasında 9 tane değer oluşturalım- tek boyutlu

# şimdi ise reshaping ile boyutunu değiştirelim çünkü yukarıdaki veri tek boyutlu - 2 boyutlu array'a çevirelim


np.random.randint(1,10,size=9).reshape(3,3)   # RESHAPE METOTU İLE 3 E 3 LÜK BOYUT OLUŞTURDUK

# KALICI DEĞİLDİR ÇÜNKÜ BİR DEĞİŞKENE AKTA RMASINI YAPMADIK

ex_reshape = np.random.randint(1,10,size=9).reshape(3,3)  # ŞİMDİ KALICI OLARAK VERİMİZ TUTULMAKTADIR.

ex_reshape.reshape(3,3)  # bu şekilde de sonrasında gerçekleştirebiliriz.

# ÖRNEK OLARAK ;
ornek = np.random.randint(1,10,size=9)
ornek.reshape(3,3)

# SONUNA BAĞLAYARAK YA DA BİR DEĞİŞKENE AKTARDIKTAN SONRA OLARAK KULLANABİLİRSİN
# DİKKAT EDİLMESİ GEREKEN KONU : 9 ELEMANLI İSE 3 E 3 LÜK BİR RESHAPE YAPILABİLİR 10 YA DA 7 OLMAZ.
                               # BUNUN SEBEBİ İSE BOYUT BİLGİSİ İLE ELEMAN TAM OLMALIDIR.