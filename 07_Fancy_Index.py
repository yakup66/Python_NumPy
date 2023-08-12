###################
 #  FANCY INDEX -DATA FRAME İÇİNDE İNDİS LİSTESİ SEÇME İŞLEMİ
########


import numpy as np

h = np.arange(0,40,2)   # arange > 0-40 a kadar 5 er 5 er şekilde artacak şekilde adım oluşturma metodur. 40 dahil değil

h [1]
h [2]
h [3]

deneme = [3,4,5,9,10]   # bir liste ve içinde 5 adet farklı eleman var

h[deneme]  # yukarıdaki listeyi array içerisinde aratınca FANCY INDEX ile listedeki örneğin 3,4,5,9,10 var sırası ile
           # h arrayinde 0 ile 40 arasındaki sayıların 3,4 ve 5. indexlerindeki sayıları bize getirir.

# h > bir NumPy arrayi'dir
# deneme > bir listedir
# # >>> listemizdeki sayıları index olarak h array'i içerisinde aratıp karşılık gelen değeri bulduk

# ELİNDE BİNLERCE VERİ VE İNDEX BİLGİSİ İÇERİSİNDEN TEK BİR SEÇİMDE İLGİLİ ARRAYA GÖNDERDİĞİNDE FANCY INDEX GERÇEKLEŞMİŞ OLUR.

