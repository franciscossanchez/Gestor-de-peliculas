def aggpelis(listpelis):
    titulo = input("Ingresa el título de la película: ").strip()
    if titulo:
        listpelis.append(titulo)
        print(f"'{titulo}' Agregada.")
    else:
        print("El título no puede estar vacío.")

def verpelis(listpelis):
    if not listpelis:
        print("No hay películas.")
    else:
        print("\n--- Lista de Películas ---")
        contador = 1
        for pelicula in listpelis:
            print(f"{contador}. {pelicula}")
            contador += 1

def elimpelis(listpelis):
    verpelis(listpelis)
    if listpelis:
        entrada = input("Ingresa el número de la película a eliminar: ").strip()
        
        es_valido = True
        if entrada == "":
            es_valido = False
        else:
            for numero in entrada:
                if numero < "0" or numero > "9":
                    es_valido = False
                    break
        
        if es_valido:
            num = int(entrada)
            if 1 <= num <= len(listpelis):
                eliminada = listpelis.pop(num - 1)
                print(f"'{eliminada}' Eliminada.")
            else:
                print("Número invalido.")
        else:
            print("Por favor, ingresa un número válido.")

def buscarpeli(listpelis):
    busqueda = input("Ingresa el título o palabra clave a buscar: ").lower()
    
    encontradas = []
    for p in listpelis:
        if busqueda in p.lower():
            encontradas.append(p)
            
    if encontradas:
        print("\n--- Resultados ---")
        for p in encontradas:
            print(f"- {p}")
    else:
        print("No se encontro.")