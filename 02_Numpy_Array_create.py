##########
# Numpy Array'i oluşturma işlemleri (Creating Numpy Arrays)
##############################################################

import numpy as np

#  SIFIRDAN ARRAY OLUŞTURMA İŞLEMLERİ

np.array([1,2,3,4,5]) # numpy array listesi oluşturma

type(np.array([1,2,3,4,5]))  # numpy.ndarray veri tipindedir

np.zeros(10,dtype=int) # girilen sayı adedi kadar sıfır değeri oluşturur

np.random.randint(0,10,size=10) # sıfır ile 10 arasında 10 tane int değeri oluştur

np.random.normal(10,4,(3,4))  # 3 satır 4 sütundan oluşan ortalaması 10 olan ve standart sapması 4 olan array oluşturma işlemi

