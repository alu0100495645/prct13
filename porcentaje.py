#!/usr/bin/python
#!encoding: UTF-8
import sys 
import modulo

  
#programa principal

argumentos= sys.argv[1:]
if(len(argumentos)== 8):
  n=int(argumentos[0])
  aprox=int (argumentos[1])
  umbral=[]
  for i in range(2,7):
    umbral.append(float(argumentos[i]))
  nombre_fich= argumentos[7]
else:
  print "Introduzca el numero de intervalos (n>0): "
  n = int(raw_input())
  print "Introduzca el numero de aproximaciones: "
  aprox = int(raw_input())
  print "Introduzca 5 umbrales de error: "
  umbral=[]
  for i in range(5):
    print"Introduzca el umbral ",i,":"
    umbral.append(float(raw_input()))
  print"Introduzca el nombre del fichero para almacenar los resultados"
  nombre_fich= raw_input()

if (n>0):
  
  
 # Una forma de averiguar si un fichero existe o no puede ser esta
 # debemos de incluir el paquete os.path
 # 	if os.path.isfile(nombre_fich):
 #		fichero=open(nombre_fich,"a")
 #	else:
 #		fichero=open(nombre_fich,"w")
 # Otra forma puede ser mediante excepciones, como vemos a continuacion:
 
  try:
    fichero=open(nombre_fich,"a")
  except:
    fichero=open(nombre_fich,"w")
  fichero.write("Nº de intervalos: %d\n" %(aprox))
  for i in range (5):
    porcentaje=modulo.error (n,aprox,umbral[i])
    fichero.write ("%2.2f%% de fallos para el umbral %2.5f\n" % (porcentaje,umbral[i]))
  fichero.close()
   
 
 
 