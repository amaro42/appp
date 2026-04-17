# for i in "amaro":
#       print(i)
#  # Pregunte al usuario su nombre u muestre sus letras 
print ("ingrese su nombre")
name=input()


#nombra ("ingrese su nombre")
nvocales=0
nletras=0
for i in name:
        print(i)
        nletras+=1
        if i in "aeiouAEIOU":
            nvocales+=1
   elif: i==" ":
print ("la cantidad de vocales de su nombre es", nvocales)
print ("numero de letras de su nombre es", nletras)
print ("la cantidad de consonantes de su nombre es", nletras-nvocales)