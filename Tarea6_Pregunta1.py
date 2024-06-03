vocales="aeiou"
consonantes="bcdfghjklmnpqrstvwxyz"
contVocales=0
contConsonantes=0

lista=[]
palabra=(input("Ingresar palabra (enter para finalizar):"))
palabra=palabra.lower()                                           # se ordenan las palabras en minusculas ya que "a" y "A" son distintas, esto nos permite que sea una forma de asegurarse de que todas las letras sean coherentes. 
while palabra!="":
  if not palabra.isalpha():                                       # se comprueba si todas los caracteres de la palabra son letras
    print("porfavor ingrese solo palabras.")
  else:
   contVocales=0
   contConsonantes=0  
   for letra in palabra:                                          # aqui se corrobora letra por letra cada palabra ingresada
    if letra in vocales:                                          # se corrobora si las letras pertenecen a las vocales
     contVocales=contVocales+1
    elif letra in consonantes:                                    # se corrobora si las letras pertenecen a las consonantes
     contConsonantes=contConsonantes+1 
   nueva_lista=[]                                                 # esta nueva lista almacena cada palabra con sus respectivas vocales y consonantes (por cada iteracion se forma una nueva lista)
   nueva_lista.append(palabra)                                    #indice 0
   nueva_lista.append(contVocales)                                #indice 1
   nueva_lista.append(contConsonantes)                            #indice 2
   lista.append(nueva_lista)                                      #se crea una nueva lista por iteracion con tres elementos cada una.
  palabra=(input("Ingresar palabra (enter para finalizar):"))
  palabra=palabra.lower()
for elemento in lista:                                           # aqui recorre cada una de las listas que se formo por cada iteracion del bucle
    print("La palabra",elemento[0], "tiene:")                    # en este caso el elemento con indice 0 (elemento[0]) de cada lista, es la "palabra" ingresada.
    print(elemento[1], "vocales y", elemento[2], "consonantes.") # el elemento[1] y [2] son respectivamente los indices de las "vocales" y "consonantes" de cada lista
    print(" ")