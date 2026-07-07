#definicion de funcion
def calcularFuerza(m,a):
    f=m*a
    return f

#programa principal
masa = float(input("ingresa la masa del cuerpo:"))
aceleracion = float(input("ingresa la aceleracion del cuerpo:"))
f= calcularFuerza(masa,aceleracion)
print("la fuerza del cuerpo es:",f,"newtons")