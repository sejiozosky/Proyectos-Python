import os #Importamos librerias que se usan en el programa
import sys
import time
def menu(): #Funcion para crear el menu
    os.system('cls')
    print ("|||||||||| Menu de la calculadora ||||||||||")
    print ("           **********************           ")
    print ("\t1 - Sumar")
    print ("\t2 - Restar")
    print ("\t3 - Multiplicar")
    print ("\t4 - Dividir")
    print ("\t9 - Salir")
    print ("********************************************")
                            
def n1(): #Funcion para introduir un numero como primer valor 
    while True:
        try:
            numero1 = float(input("Inserta el primer valor: "))
            menu()
            if operador == "1":
                print(numero1,"+")
            elif operador == "2":
                print(numero1,"-")     
            elif operador == "3":
                print(numero1,"*")
            elif operador == "4":
                print(numero1,"/")
        except ValueError:
            os.system('cls') 
            menu()
            if operador == "1":
                print("+")
            elif operador == "2":
                print("-")     
            elif operador == "3":
                print("*")
            elif operador == "4":
                print("/")
            print("Introduce un número válido")
        
        else:
            return numero1

def n2(): #Funcion para introducir un numero como segundo valor 
    while True:
        try:
            numero2 = float(input("Inserta el segundo valor: "))
            menu()
            if operador == "1":
                print(numero1,"+",numero2)
            elif operador == "2":
                print(numero1,"-",numero2)     
            elif operador == "3":
                print(numero1,"*",numero2)
            elif operador == "4":
                print(numero1,"/",numero2)
        except ValueError:
            os.system('cls') 
            menu()
            if operador == "1":
                print(numero1,"+")
            elif operador == "2":
                print(numero1,"-")     
            elif operador == "3":
                print(numero1,"*")
            elif operador == "4":
                print(numero1,"/")
            print("Introduce un número válido")
        else:
            return numero2
       
#Definimos 2 variables que vamos a usar
operador = 0

#Mientas que la variable i sea mayor que cero se ejecuta el bucle (SIEMPRE)
while True :
    # Mostramos el menu
    menu()
    #Preguntamos que operacion quiere realizar
    operador = input("¿Que operación quieres realizar?: ")
    if operador == "1":
        print("+")
    elif operador == "2":
        print("-")     
    elif operador == "3":
        print("*")
    elif operador == "4":
                print("/")
    while operador != "1" and operador != "2" and operador != "3" and operador != "4" and operador != "9":
        os.system('cls')
        menu()
        print("Introduce un operador correcto")
        operador = input("¿Que operación quieres realizar?: ")
        if operador == "1":
            print("+")
        elif operador == "2":
             print("-")     
        elif operador == "3":
            print("*")
        elif operador == "4":
            print("/")
    
    if operador == "9": #Si es 9 cerramos el programa
        os.system('cls')
        print("SALIENDO.")
        time.sleep(1)
        os.system('cls')
        print("SALIENDO..")
        time.sleep(1)
        os.system('cls') 
        print("SALIENDO...")
        time.sleep(1)
        sys.exit()

    #Realizamos una operacion u otra
    if operador == "1":
        numero1 = n1()
        numero2 = n2()
        resultado = numero1 + numero2 
    elif operador == "2":
        numero1 = n1()
        numero2 = n2()
        resultado = numero1 - numero2      
    elif operador == "3":
        numero1 = n1()
        numero2 = n2()
        resultado = numero1 * numero2
    elif operador == "4":
        numero1 = n1()
        numero2 = n2()
        resultado = numero1 / numero2    
       
    #Mostramos el resultado en pantalla y preguntamos si realizamos otra operación    
    print("El resultado es: ",resultado)
    salir =(input("Pulsa cualquier tecla para realizar otra operación o pulsa 9 para salir..."))
    if salir == "9":
        os.system('cls')
        print("SALIENDO.")
        time.sleep(1)
        os.system('cls')
        print("SALIENDO..")
        time.sleep(1)
        os.system('cls') 
        print("SALIENDO...")
        time.sleep(1)
        sys.exit()
    