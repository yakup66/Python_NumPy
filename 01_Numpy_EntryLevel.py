###############
# NUMPY
import numpy
# PYTHON KULLANARAK MATEMATİK İSTATİSTİK KULLANARAK VERİ ANALİTİĞİ YAPMAK İÇİN
# VERİMLİ VERİ SAKLAMA, YÜKSEK SEVİYEDEN YANİ VEKTÖREL İŞLEMLER - FIX TYPE
# HIZLI BİR ŞEKİLDE ARRAY İŞLEMLERİ YAPAR
# DAHA AZ ÇABA İLE DAHA FAZLA İŞLEM YAPMAMIZI SAĞLAR

import numpy as np

#neden hızlı
a = [1,2,3,4]
b = [2,3,4,5]
ab = []          # normalde iki listeyi çarpıp boş listeye eklenir

for i in range(0, len(a)):
    ab.append(a[i] * b [i])
ab

# numpy ile nasıl yapılır
a = np.array([1,2,3,4])
b = np.array([2,3,4,5])
a * b