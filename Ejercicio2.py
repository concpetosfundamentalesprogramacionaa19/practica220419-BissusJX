"""
  Segundo ejercicio a Resolver
"""
x = input("Ingrese la variable x")
y = input("Ingrese la variable y")
z = input("Ingrese la variable z")
m = float(x)+float(y)/float(z)/float(x)-(float(y)/float(z))
print("el valor de m en base a las variables:\nx= %s\n y= %s\n  z: %s\nDieron como resultado de \n\tm%2.f" % (x,y,z,m))