import gestionpelis

def ejecutar_menu():
    listpelis = []
    
    while True:
        print("\n=== GESTIÓN DE PELÍCULAS ===")
        print("1. Agregar película")
        print("2. Ver películas")
        print("3. Eliminar película")
        print("4. Buscar película")
        print("5. Salir")
        
        opcion = input("Elige una opción del 1 al 5: ").strip()
        
        if opcion == "1":
            gestionpelis.aggpelis(listpelis)  
        elif opcion == "2":
            gestionpelis.verpelis(listpelis)
        elif opcion == "3":
            gestionpelis.elimpelis(listpelis)
        elif opcion == "4":
            gestionpelis.buscarpeli(listpelis)
        elif opcion == "5":
            print("Saliendo")
            break
        else:
            print("Opción inválida, ingresa un numero del 1 al 5")