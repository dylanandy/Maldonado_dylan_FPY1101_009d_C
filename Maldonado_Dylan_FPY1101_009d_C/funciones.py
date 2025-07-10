productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],                       '2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i7', 'Nvidia GTX1050'], 
            'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i5', 'Nvidia RTX2080Ti'], 
            'fgdxFHD': ['HP', 15.6, '12GB', 'DD', '1T', 'Intel Core i5', 'integrada'], 
            'GF75HD': ['Asus', 15.6, '12GB', 'DD', '1T', 'Intel Core i3', 'Nvidia GTX1050'],                      '123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 7', 'integrada'], 
            '342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'Nvidia GTX1050'], 
            'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'Nvidia GTX1050']
                        }
stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1], 
              'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7], 
              'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0] 
} 
def menu(): 
    print("*** MENU PRINCIPAL ***") 
    print("1.Stock marca.")
    print("2.Búsqueda por precio.") 
    print("3.Listado de productos. ")
    print("4.Salir.") 

def stock_marca(marca):
    while True:
        try:
            for marca in stock:
                len(productos[1, 2])
                respuesta = (input(str("ingrese marca a buscar: ")))
        except ValueError:
                respuesta.strip().title().isalpha()
                print(f"El stock es: {stock['8475HD'[6, 7]]}") 
def busqueda_precio(p_min, p_max):
    while True:
            for precio in stock:
                p_min = int(input("ingrese un valor minimo: "))
                p_max = int(input("ingrese un valor maximo: "))
            print(f"el precio minimo es {p_min}, el precio maximo es {p_max}")
            print(f"{stock[[6, 7]]}")
def ordenar_productos():
    pass
def salir():
    print("Saliendo del programa...")