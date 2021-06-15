variancia_populacional = 0
variancia_amostral = 0
media = 0
numero_de_elementos = int(input("Entre o número de elementos: "))
numero_de_classes = int(input("Entre o número de classes: "))
frequencias = []
pontos_medios = []

for i in range(numero_de_classes):
    frequencias.append(float(input("Entre a frequência da classe: ")))


for i in range(numero_de_classes):
    #li = float(input("Entre o limite inferior da classe: "))
    #Li = float(input("Entre o limite superior da classe: "))
    pontos_medios.append(float(input("Entre o limite superior da classe: ")))

for i in range(numero_de_classes):
    media = media + ((pontos_medios[i])*(frequencias[i]))
media = media/numero_de_elementos


for i in range(numero_de_classes):
    x = pontos_medios[i]
    f = frequencias[i]
    variancia_populacional = variancia_populacional + (((pontos_medios[i]-media)**2)*frequencias[i])/numero_de_elementos
    variancia_amostral = variancia_amostral + (((pontos_medios[i]-media)**2)*frequencias[i])/(numero_de_elementos-1)

print("frequencia:",frequencias)
print("pontos medios:",pontos_medios)
print("media =",media)
print("variancia_populacional =",variancia_populacional)
print("variancia_amostral =",variancia_amostral)