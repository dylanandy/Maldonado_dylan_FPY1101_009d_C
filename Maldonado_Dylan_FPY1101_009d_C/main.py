from funciones import *
import os
os.system('cls')

while True:
    menu()
    opción = input("ingrese una opción: ")
    if opción == '1':
        print("Stock marca")
        stock_marca()
    
    elif opción == '2':
        busqueda_precio()
    
    elif opción == '3':
        pass

    elif opción == '4':
        salir()
        break
    else:
        print("Debe seleccionar una opción válida!!")