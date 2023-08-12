#################
# NumPY Array özellikleri ( Attirbutes of Numpy Arrays)
##########################

import numpy as np
# BU METOTLARI KULLANARAK ÖZELLİKLERE ERİŞİM;
# ndim : boyut sayısını söyler
# shape : boyut bilgisini verir
# size : toplam eleman sayısını verir
# dtype : array veri tipini gösterir

a = np.random.randint(10,size=5) # aralık girmek istersen (0,10 , size=5) , girmezsen sıfırdan başlar

# buyut bilgisi için ( sayısı )
a.ndim

#  bilgisini verir,boyutunu verir( Kaç boyutlu ise bunu kullan)
a.shape

# eleman sayısı
a.size

# tip bilgisi
a.dtype