##Este programa calcula el indice de masa corporal
#indiceDeMasaCorporal = peso/(altura*altura)
#<19 = delgadez
#20 y 25 normal
#26 y 30 sobrepeso
# mayor a 30 obesidad

peso = float(input("Ingresar peso corporal en KG"))
altura = float(input("Ingresar altura en cm"))
alturaMetros = altura/100
indiceDeMasaCorporal = peso/(alturaMetros*alturaMetros)

if (indiceDeMasaCorporal <20):
    print("Esta delgado,coma más")
else:
    if(indiceDeMasaCorporal >=20 and indiceDeMasaCorporal <=25):
        print("Tu peso es normal")
    else:
         if(indiceDeMasaCorporal > 25 and indiceDeMasaCorporal <=30):
            print("Tienes sobre peso")
         else:
            if (indiceDeMasaCorporal>30):
                print("Tienes obesidad")