"""
Referencias:
RC: Cantidad de respuestas correctas.
RI: Cantidad de respuestas incorrectas.
RB: Cantidad de respuestas en blanco.
NT: Nota total

"""
#Input
RC = int(input("Ingrese la cantidad de notas correctas: "))
RI = int(input("ingresa la cantidad de notas incorrectas: "))
RB = int(input("Ingrese la cantidad de respuestas en blanco: "))

#Proceso
NT = (RC*3) + (RI*(-1))

#Output
print("El puntaje total del aspirante es: ", NT)