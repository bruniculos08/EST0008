from math import ceil
from math import log10
from matplotlib import pyplot as plt
from math import sqrt


variancia_populacional, variancia_amostral, media, variancia_amostral, mediana, k, numero_de_elementos = 0, 0, 0, 0, 0, 0, 0
frequencias_acumuladas, Li, li, quartil, classe_quartil, percentil, classe_percentil = [], [], [], [], [], [], []

#frequencias = [28,39,51,68,74,27,29,10,4,3,2]
frequencias = [1,1,1,1,1,1,1,1,1,1,1]
pontos_medios = [5.8,5.1,5.7,6.4,6.1,5.1,5.4,4.8,5.2,4.9,5.5]
h = 0.4


numero_de_classes = len(frequencias)
#numero_de_classes = ceil(1 + 3.3*(log10(numero_de_elementos)))

for i in range(numero_de_classes): 
    numero_de_elementos = numero_de_elementos + frequencias[i] 

#& Calculando frequencias_acumuladas

for i in range(numero_de_classes):
#    frequencias.append(int(input("Digite a frequência da classe:")))
    if i > 0:
        frequencias_acumuladas.append(frequencias[i]+frequencias_acumuladas[i-1])
    elif i == 0:
        frequencias_acumuladas.append(frequencias[i])


#& Receber dados (não nessário)

#for i in range(numero_de_classes):
    #li.append(float(input("Entre o limite inferior da classe: ")))
    #Li.append(float(input("Entre o limite superior da classe: ")))
    #pontos_medios.append(float((Li[i]+li[i])/2.0))
    #pontos_medios.append(float(input("Digite o ponto medio da classe: ")))

#& Calculando Média

for i in range(numero_de_classes):
    media = media + ((pontos_medios[i])*(frequencias[i]))
media = media/numero_de_elementos

#& Calculando Variância (populacional e amostral) e Erro Padrão

for i in range(numero_de_classes):
    variancia_populacional = variancia_populacional + (((pontos_medios[i]-media)**2)*frequencias[i])/numero_de_elementos
    variancia_amostral = variancia_amostral + (((pontos_medios[i]-media)**2)*frequencias[i])/(numero_de_elementos-1)
erro_padrao_amostral = sqrt(variancia_amostral)

#& Calculando Mediana

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

#& Calculando Quartis

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

#& Calculando Percentis

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

print("Numero de classes: ",numero_de_classes,"\nFrequencias: ",frequencias,"\nFrequencias Acumuladas: ",frequencias_acumuladas,
"\nPontos Medios:",pontos_medios, "\nMedia = ",media,"\nMediana = ",mediana,"\nVariancia Populacional = ",variancia_populacional,
"\nVariancia Amostral = ",variancia_amostral,"\nQuartis: ", quartil,"\nPercentis: ", percentil)

#& Plotando Gráficos

#* Eixo_x, Eixo_y
plt.plot(pontos_medios, frequencias)
plt.show()

#^ Como definir um gráfico