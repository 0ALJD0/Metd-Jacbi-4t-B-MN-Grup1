import sys
from funciones import menu,mostrararry,validarentrasn, jacobi

a="S" ;b=[]; c="S"; dat0=[]

##Mensaje de presentación    
print("Muy buenas, somos el primer grupo, conformado por: \n"
"--ANCHUNDIA SANTANA FRANCISCO \n--ARCE PONCE BRYAN\n--ARTEAGA CHILAN JOSE\n--BAILON DELGADO TONNY\n--BALCAZAR SOLIS SADANA\n"
"tenemos como objetivo la resolucion de ecuaciones lineales por el método de Jacobi mediante un programa\nelaborado en lenguaje Python"
"esperando que sea de su agrado, se mostrará su funcionalidad correspondiente:  ")

##Validar sí quiere salir o cerrar el programa, o si desea volver a ejecutar el programa
##después del mensaje de bienvenida
while a=="S": 
    ##Validar sí desea corregir los datos, reptirá la inserción de datos
    
  while c=="S": 
        ##pedimos el ingreso de datos, tanto de los valores del sistema
        ##como de la tolerancia
        b=menu()
        mostrararry(b)
        ##Mostramos 
        print("Desea corregir los datos?")
        print("Ingrese S si así es o N si no ")
        c=validarentrasn()

        ##Ejecutamos el algritmo  de jacobi  
        jacobi(b)  
  print("Desea volver a ejecutar el programa?")
  print("Ingrese S si así es o N = no (cierre del programa) ")
  a=validarentrasn()

print("Adios! Buen día")

sys.exit()





