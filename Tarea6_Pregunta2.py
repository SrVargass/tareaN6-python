lista=[]
print("opcion 1: Ingresar un elemento a la lista")
print("opcion 2: Modificar un elemento de la lista según el índice")
print("opcion 3: Eliminar un elemento de la lista según el índice") 
print("opcion 4: Eliminar el último elemento de la lista") 
print("opcion 5: Buscar un elemento de la lista según el dato (devuelve el índice)") 
print("opcion 6: Mostrar todos los elementos de la lista") 
print("opcion 7: Salir")
while True:
 try:
  opcion = int(input("Ingrese una de las opciones: "))
  if 1 <= opcion <= 7:
   break
  else:
    print("Opción incorrecta ( se debe poner un numero entre 1 y 7")
 except:
     print("entrada incorrecta porfavor ingrese un número entre 1 y 7") 

while opcion!=7:
 if opcion==1:
  print(" ")
  ingresar=input("ingrese un elemento:")
  lista.append(ingresar)
  print(ingresar,"agregado a la lista.")

 if opcion==2:
   i=int(input("ingrese el indice de la lista para cambiar elemeneto (0 es el primer elemento):"))
   if i>=0 and i<len(lista):
    nuevo_elemento=input("ingrese el nuevo elemento:")
    lista[i]=nuevo_elemento
    print("el elemento a sido modificado.")
   else:
    print("el indice no se encuentra dentro del rango de la lista.")

 if opcion==3:
   elminar=int(input("ingrese el elemento a elminar segun su indice:"))
   if elminar>=0 and elminar<len(lista):
    lista.pop(elminar)
   else:
    print("el indice no se encuentra dentro del rango de la lista.")

 if opcion==4:
   if lista:
    lista.pop()
    print("se elimino el ultimo elemento de la lista.")
   else:
    print("la lista esta vacia.")

 if opcion==5:
   elemento=input("ingrese el elemento a buscar:")
   if elemento in lista:
    indice=lista.index(elemento)
    print("el elemento",elemento,"esta en el indice:",indice)
   else:
    print("elemento no encontrado en la lista.")

 if opcion==6:
   if lista:
    print(lista[:])
   else:
    print("no hay elementos en la lista.")
 print(" ")
 print("opcion 1: Ingresar un elemento a la lista")
 print("opcion 2: Modificar un elemento de la lista según el índice")
 print("opcion 3: Eliminar un elemento de la lista según el índice") 
 print("opcion 4: Eliminar el último elemento de la lista") 
 print("opcion 5: Buscar un elemento de la lista según el dato (devuelve el índice)") 
 print("opcion 6: Mostrar todos los elementos de la lista") 
 print("opcion 7: Salir") 
 while True:
  try:
   opcion = int(input("Ingrese una de las opciones: "))
   if 1 <= opcion <= 7:
    break
   else:
    print("Opción incorrecta ( se debe poner un numero entre 1 y 7")
  except:
     print("entrada incorrecta porfavor ingrese un número entre 1 y 7") 
