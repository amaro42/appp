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
        elif i==" ":
            nletras-=1

print ("la cantidad de vocales de su nombre es", nvocales)
print ("numero de letras de su nombre es", nletras)
print ("la cantidad de consonantes de su nombre es", nletras-nvocales)


# preguntar la cantidad de votantes 
# poner los dos candidatos: Dexter/samurai jack 
# preguntar a cada votante por quien vota
# al final mostrar el ganador o si hay empate

print ("ingrese la cantidad de votantes")
votantes=int(input())
dexter=0
samurai_jack=0
for i in range (votantes):
    print ("por quien vota? dexter o samurai jack")
    voto=input()
    if voto=="dexter":
        dexter+=1
    elif voto=="samurai jack":
        samurai_jack+=1

if dexter>samurai_jack:
    print("el ganador es dexter")
elif samurai_jack>dexter:
    print("el ganador es samurai jack")
else:
    print("hay un empate")