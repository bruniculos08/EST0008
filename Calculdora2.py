from math import ceil
from math import log10
from matplotlib import pyplot as plt
from math import sqrt


pontos_medios = [77.1, 77.3, 77.2, 77.1, 77.6, 77.4, 77.3, 77.2, 77.1, 77.5, 77.3, 77.6, 77.2, 77,8]
#pontobeta = []
n = 14
x = 77.335
variancia_amostral = 0

for i in range(n):
    variancia_amostral = variancia_amostral + ((pontos_medios[i]-x)**2)/13

erro_padrao_amostral = sqrt(variancia_amostral)


print(variancia_amostral)
print(erro_padrao_amostral)
