from math import ceil
from math import log10
from matplotlib import pyplot as plt

variancia_populacional = 0
variancia_amostral = 0
media = 0
numero_de_elementos = 306
#numero_de_classes = int(input("Entre o número de classes: "))
#frequencias = [28,39,51,68,74,27,29,10,4,3,2]
frequencias = [26,32,59,70,56,20,13,11,7,9,3]
frequencias_acumuladas = []
pontos_medios = [15.2,15.6,16,16.4,16.8,17.2,17.6,18,18.4,18.8,19.2]
li = []
Li = []
mediana = 0
quartil = []
classe_quartil = []
classe_percentil = []
percentil = []
k = 0
h = 0.4

#numero_de_classes = ceil(1 + 3.3*(log10(numero_de_elementos)))
numero_de_classes = 11

for i in range(numero_de_classes):
#    frequencias.append(int(input("Digite a frequência da classe:")))
    if i > 0:
        frequencias_acumuladas.append(frequencias[i]+frequencias_acumuladas[i-1])
    elif i == 0:
        frequencias_acumuladas.append(frequencias[i])

#for i in range(numero_de_classes):
    #li.append(float(input("Entre o limite inferior da classe: ")))
    #Li.append(float(input("Entre o limite superior da classe: ")))
    #pontos_medios.append(float((Li[i]+li[i])/2.0))
    #pontos_medios.append(float(input("Digite o ponto medio da classe: ")))

for i in range(numero_de_classes):
    media = media + ((pontos_medios[i])*(frequencias[i]))
media = media/numero_de_elementos

for i in range(numero_de_classes):
    variancia_populacional = variancia_populacional + (((pontos_medios[i]-media)**2)*frequencias[i])/numero_de_elementos
    variancia_amostral = variancia_amostral + (((pontos_medios[i]-media)**2)*frequencias[i])/(numero_de_elementos-1)

for i in range(numero_de_classes):
    if frequencias_acumuladas[i] > (numero_de_elementos)/2:
        classe_mediana = i
        print("classe mediana é a nº",i+1)
        lt = float(input("Digite o limite inferior da classe mediana: "))
        #h = float(input("Digite a amplitude de classe: "))
        #lt = li[i]
        #h = Li[i] - li[i]
        mediana = lt + (((numero_de_elementos)/2) - frequencias_acumuladas[i-1])*(h/frequencias[i])
        break

for i in range(numero_de_classes):
    if frequencias_acumuladas[i] > (k+1)*(numero_de_elementos)/4:
        classe_quartil.append(i+1)
        print("classe do",(k+1),"º quartil é a nº",i+1)
        lt = float(input("Digite o limite inferior da classe do quartil: "))
        #h = float(input("Digite a amplitude de classe: "))
        #lt = li[i]
        #h = Li[i] - li[i]
        if i > 0:
            quartil.append(lt + ((((k+1)*numero_de_elementos)/4)-frequencias_acumuladas[i-1])*(h/frequencias[i]))
        else:
            quartil.append(lt + ((((k+1)*numero_de_elementos)/4)-0)*(h/frequencias[i]))
        k = k+1
        i = 0
    if k == 3:
        break

k = 9
for i in range(numero_de_classes):
    if frequencias_acumuladas[i] > (k+1)*(numero_de_elementos)/100:
        classe_percentil.append(i+1)
        print("classe do",(k+1),"º percentil é a nº",i+1)
        lt = float(input("Digite o limite inferior da classe do percentil: "))
        #h = float(input("Digite a amplitude de classe: "))
        #lt = li[i]
        #h = Li[i] - li[i]
        if i > 0:
            percentil.append(lt + ((((k+1)*numero_de_elementos)/4)-frequencias_acumuladas[i-1])*(h/frequencias[i]))
        else:
            percentil.append(lt + ((((k+1)*numero_de_elementos)/4)-0)*(h/frequencias[i]))
        k = k+80
        i = 0
    if k > 89:
        break

print("numero de classes: ",numero_de_classes)
print("frequencias: ",frequencias)
print("frequencias acumuladas: ",frequencias_acumuladas)
print("pontos medios:",pontos_medios)
print("media =",media)
print("mediana =",mediana)
print("variancia_populacional =",variancia_populacional)
print("variancia_amostral =",variancia_amostral)
print("quartis: ", quartil)
print("percentis: ", percentil)

plt.plot(pontos_medios, frequencias)
plt.show()