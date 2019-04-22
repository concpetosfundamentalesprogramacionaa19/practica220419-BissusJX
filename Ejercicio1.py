"""
   primer ejercicio 
"""
horas =  input("Ingresar el numero de horas:") #se pide el numero de horas
costo = input("Ingrese el costo oficial:") #se pide el costo oficial

sueldomensual = int(horas) * int(costo)
descuento = float(sueldomensual) * 0.10
print("Su sueldo mensual es: %1f" % sueldomensual)
print ("Su descuento es:%1f"%float(descuento))



