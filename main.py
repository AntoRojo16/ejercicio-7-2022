from claseViajeroFrecuente import ViajeroFrecuente
from ManejadorDeViajeros import ListaViajeros
from claseMenu import Menu

if __name__ == '__main__':
    lista=ListaViajeros()
    lista.Inicializar()
    print(lista)
    bandera = False
    num=input("Ingrese un numero de viajero >> ")
    i=lista.buscarViajero(num)
    while not bandera:
        print("\nMENU DE OPCIONES")
        print("0 Salir")
        print("1 ITEM 7.1: Comparar las cantidad de millas acumuladas de un viajero frecuente \ncon un valor entero a través de la sobrecarga del operador igual (== o __eq__)")
        print("2 ITEM 7.2: Acumular millas se pueda resolver de la siguiente forma: \ndebe ser posible realizar v =  100 + v.")
        print("3 ITEM 7.3: Canjear millas se pueda resolver de la siguiente forma: \ndebe ser posible realizar v =  100 - v.")

        opcion = int(input('Ingrese una opcion:'))
        unmenu=Menu()
        unmenu.opcion(opcion,lista,i)
        bandera = int(opcion)== 0

