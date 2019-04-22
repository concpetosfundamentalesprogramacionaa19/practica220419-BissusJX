"""
  ejemplo2
"""
import sys 

nombre_archivo= sys.argv[0]
valor1 = sys.argv [1]
valor2 = sys.argv [2]
suma = int(valor1) + int(valor2)  #suma de variables
multiplicacion = int(valor1) * int(valor2) # multiplicacion variables

print ("la suma es: %d" % suma )
print ("la multiplicacion es: %d" % multiplicacion)