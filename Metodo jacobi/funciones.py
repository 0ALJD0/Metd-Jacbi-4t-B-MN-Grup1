##Función donde pedira el ingreso de los datos
def  menu ():
    print("Ingrese el valor de x_1 de la primera ecuación") #10
    vxa = validcion0oenter() #Cada uno de los ingresos tiene validación 
    print("Ingrese el valor de x_2 de la primera ecuación") #2
    vya=validcion0oenter()
    print("Ingrese el valor de x_3 de la primera ecuación") #-1
    vza= validcion0oenter()
    print("Ingrese el valor independiente de la primera ecuación") #27
    vca= validcion0oenter()
    print("Ingrese el valor de x_1 de la segunda ecuación") #-3
    vxb= validcion0oenter()
    print("Ingrese el valor de x_2 de la segunda ecuación") #-6
    vyb= validcion0oenter()
    print("Ingrese el valor de x_3 de la segunda ecuación") #2
    vzb =validcion0oenter()
    print("Ingrese el valor independiente de la segunda ecuación") #-61.5
    vcb =validcion0oenter()
    print("Ingrese el valor de x_1 de la tercera ecuación") #1
    vxc =validcion0oenter()
    print("Ingrese el valor de x_2 de la tercera ecuación") #1
    vyc = validcion0oenter()
    print("Ingrese el valor de x_3 de la tercera ecuación") #5
    vzc =validcion0oenter()
    print("Ingrese el valor independiente de la tercera ecuación") #-21.5
    vcc =validcion0oenter()
    print("Ingrese el valor de la tolerancia solo ingrese el número no agregue \"%\" (en porcentaje: 0.5, 5, 20)") 
    tol =validcion0oenter()
    tol=validartole(tol) #Definir variable donde se guardará la tolerancia
    
    
    ##Guardamos los datos en un vector (array)
    arr=[[vxa,vya,vza,vca] ##la primera ecuacion
    ,[vxb,vyb, vzb,vcb] ## la 2da
    ,[vxc,vyc, vzc,vcc]## la 3era
    ,tol] ##tolerancia
    return arr

##Validarmos
def validartole (x):
    while True:
        while x<=0 or x>100:
           
                print ("La entrada es incorrecta: Solo valores pertenecientes al intervalo (0,100] ")
                print ("Vuelva a ingresar el dato")
                x=float(input()) 
       
        return x

##Mostramos el sistema de ecuaciones 
def mostrararry(va):
    
    print("El sistema de ecuaciones ingresado es:")
    print(va[0][0],"x1  ",va[0][1],"x2  ",va[0][2],"x3  =",va[0][3]) 
    print(va[1][0],"x1  ",va[1][1],"x2  ",va[1][2],"x3  =",va[1][3]) 
    print(va[2][0],"x1  ",va[2][1],"x2  ",va[2][2],"x3  =",va[2][3])
    print("La tolerancia es: ",va[3],"%") 


#Función para validar que el usuario no ingrese valores nulos o enters como entradas
def validcion0oenter ():
    while True:
        x=input()
        while x=="0":
            print ("La entrada es incorrecta:No se permite valores de 0 ")
            print ("Vuelva a ingresar el dato")
            x=input()  
        try:
            x=float(x)
            return x
        except ValueError:
            print ("El tipo de dato es incorrecto ")
            print ("Vuelva a ingresar el dato")

##Funcion para validar que el usuario solo ingrese s o n 
def validarentrasn ():
    x=input()
    x=x.upper()
    while x!="S" and x!="N":
            print ("La entrada es incorrecta:No se permite otro caracter ")
            print ("Vuelva a ingresar el dato")
            x=input()
            x=x.upper()
            
    return x 
    
    
 #Funcion que ejecuta el proceso con 0 (primera iteracion)  
def processcon0 (arr):
    vca=arr[0][3]
    vcb=arr[1][3]
    vcc=arr[2][3]
    vxa=arr[0][0]
    vyb=arr[1][1]
    vzc=arr[2][2]
 #operaciones que se ejcutan con los valores que se encuentran dentro del array para obtener x1, x2, x3  
    x1=(vca)/vxa    
    x2=(vcb)/vyb 
    x3=(vcc)/vzc 
    a=[x1,x2,x3] #Se guardan los valores x1, x2, x3 dentro de la variable a
    
    ##mostramos la iteración #0
    print("Resultado:\n")
    print("itr=0 El valor x1 es: ",x1,"El valor x2 es: ",x2, "El valor X3 es: ",x3,"\n")
    return a

##Esta función permite obtener el error relativo porcentual
def erpt(a,b):
    k=abs(((a-b)/a)*100) #el error relativo porcentual se guarda en la variable k 
    return k #Retorna el error relativo


##Esta  función revisa si se cumple la condición, de que
##la diagonal principal sea dominante, una de las condiciones para que 
##haya convergencia
def converge (arr):
    k=0.0
    n=0.0
    a=0.0
    b=0.0
    c=0.0
    ##sacamos los valores de la diagonal 
    vxa=abs(arr[0][0])  
    vyb=abs(arr[1][1])
    vzc=abs(arr[2][2])
    ##comparamos que la suma de los valores absolutos de cada elemente en cada fila, sea menor
    ##al valor absoluto del elemento de la diagonal
    for i in [0]:
        for j in [1,2]: 
            n=n+abs(arr[i][j])
           
        if vxa>n:
            a=1.0
        n=0.0
    for i in [1]:
        for j in [0,2]:
            n=n+abs(arr[i][j])
        if vyb>n:
            b=1.0
         
        n=0.0
    for i in [2]: 
        for j in [0,1]:
            n=n+abs(arr[i][j])
        if vzc>n:
            c=1.0  
         
        n=0.0          
    k=a+b+c
    ##si k es = 3, devuelve True
    ##lo cual significa que la diagonal es dominante
    if k==3:
        return True
    else:
        return False

#Función donde se hará el metodo de Jacobi, para resolver la función
def jacobi(arr):
    ##como arr será el array que nos regrese menu
    #sacamos los elementps correspondientes, y los asignamos a una variable especifica
    #vxa(v=valor,x=es la variable,a=es el identicador de la ecuación)
    #vxa= 10
    #en el ssitema:
        #10x1     2x2       3x3     = 20
        #5x1      4x2       1x3     = 10
        #9x1      7x2       8x3     = 30

    vxa=arr[0][0]
    vya=arr[0][1]
    vza=arr[0][2]
    vca=arr[0][3] ;n=0.0 #n es el contrador de iteraciones

    vxb=arr[1][0]
    vyb=arr[1][1]
    vzb=arr[1][2]
    vcb=arr[1][3]

    vxc=arr[2][0]
    vyc=arr[2][1]
    vzc=arr[2][2]
    vcc=arr[2][3]
    a=0.0## es la bandera, que se activa cuando pasamos la 1era itereación
    tol=arr[3]##sacamos la tolerancia
    ##declaramos un valor inicial para los errores relativos de cada variable
    #para que la ejecución  del while comience
    erp1=100.0
    erp2=100.0
    erp3=100.0
    print("\nCalculando...\n")
    ##esta condición indica que si la función nos retorna un true
    #entonces seejecutará el proceso del metodo jaconi
    #y si retorna un false, es por que no hay convergencia
    if converge(arr):
        ##ese ciclo ejecuta las iteraciones, mientras la tolerencia
        #siga siendo mayor que cualquiera de los erroes relativos porcentual de
        #cada variable
        while (erp1<tol and erp2<tol and erp3<tol)==False:
            n+=1
            ##efectuamos este if solo en la primera iteración
            #que inicia con x1=Ca/Aii, x2=Cb/bii ,x3=Cc/cii, calculados en la funcción
            if a==0.0:
                vrbls0=processcon0(arr) ##se obtiene el array x1,x2,x3
                a=1.0##se activa la vandera
                #se efectua el calculo    
                x1=(vca+((vya*-1)*vrbls0[1])+((vza*-1)*vrbls0[2]))/vxa 
                x2=(vcb+((vxb*-1)*vrbls0[0])+((vzb*-1)*vrbls0[2]))/vyb 
                x3=(vcc+((vxc*-1)*vrbls0[0])+((vyc*-1)*vrbls0[1]))/vzc 
                #se realiza el calculo del error relativo porcentual
                erp1=erpt(x1,vrbls0[0])
                erp2=erpt(x2,vrbls0[1])
                erp3=erpt(x3,vrbls0[2])
                ##se imprime el calculo
                
                print("itr=",n," El valor x1 es: ",x1,"El valor x2 es: ",x2, "El valor X3 es: ",x3)
                print("itr=",n,"Erp de x1=",erp1,"%"," Erp de x1=",erp2,"%"," Erp de x3=",erp3,"%\n")
            else:  #esto se ejcuta en la 3 itereacion, o 2da repeticion del while  
                #se guardan los valores de forma recursiva, de x1,x2,x3
                a=x1
                b=x2
                c=x3
                #se efectua el proceso de forma recursiva
                x1=(vca+(vya*b)+(vza*c))/vxa 
                x2=(vcb+(vxb*a)+(vzb*c))/vyb 
                x3=(vcc+(vxc*a)+(vyc*b))/vzc 
                
                erp1=erpt(x1,a)
                erp2=erpt(x2,b)
                erp3=erpt(x3,c)
                
                print("itr=",n," El valor x1 es: ",x1,"El valor x2 es: ",x2, "El valor X3 es: ",x3)
                print("itr=",n,"Erp de x1=",erp1,"%"," Erp de x1=",erp2,"%"," Erp de x3=",erp3,"%\n")
        
        print("Fin de itereaciones!\n")
    else:#muestra mensaje de que no converge
        print("La matriz no converge!! (no tiene una diagonal dominante)")
