import os 

 

archivo_platos = "platos.txt" 

 

# Carga platos desde archivo 

def cargar_platos(): 

    platos = [] 

    if os.path.exists(archivo_platos): 

        with open(archivo_platos, "r", encoding="utf-8") as f: 

            for linea in f: 

                try: 

                    nombre, tipo, precio = linea.strip().split(";") 

                    platos.append({"nombre": nombre, "tipo": tipo, "precio": float(precio)}) 

                except ValueError: 

                    continue 

    return platos 

 

# Guarda platos en archivo 

def guardar_platos(platos): 

    with open(archivo_platos, "w", encoding="utf-8") as f: 

        for plato in platos: 

            f.write(f"{plato['nombre']};{plato['tipo']};{plato['precio']}\n") 

 

# Validación del tipo 

def pedir_tipo(): 

    tipos_validos = ["entrada", "principal", "postre"] 

    tipo_valido = False 

    while not tipo_valido: 

        tipo = input("Tipo (entrada, principal, postre): ").strip().lower() 

        if tipo in tipos_validos: 

            tipo_valido = True 

        else: 

            print("Tipo inválido. Intente de nuevo.") 

    return tipo 

 

# Validación del precio 

def pedir_precio(): 

    precio_valido = False 

    while not precio_valido: 

        entrada = input("Precio: ").strip() 

        try: 

            precio = float(entrada) 

            if precio >= 0: 

                precio_valido = True 

            else: 

                print("El precio debe ser positivo.") 

        except ValueError: 

            print("Entrada inválida. Ingrese un número válido.") 

    return precio 

 

# Agrega plato con validación 

def agregar_plato(platos): 

    nombre = input("Nombre del plato: ").strip().title() 

    tipo = pedir_tipo() 

    precio = pedir_precio() 

    platos.append({"nombre": nombre, "tipo": tipo, "precio": precio}) 

    print("✔ Plato agregado correctamente.\n") 

 

# Mostrar platos 

def mostrar_platos(platos): 

    if not platos: 

        print("No hay platos cargados.") 

        return 

    print("\n--- Lista de platos ---") 

    for p in platos: 

        print(f"{p['nombre']} | {p['tipo'].capitalize()} | ${p['precio']:.2f}") 

    print() 

 

# Buscar plato 

def buscar_plato(platos): 

    nombre = input("Ingrese el nombre a buscar: ").strip().title() 

    encontrados = [p for p in platos if p['nombre'] == nombre] 

    if encontrados: 

        print(" Plato encontrado:") 

        for p in encontrados: 

            print(f"{p['nombre']} | {p['tipo'].capitalize()} | ${p['precio']:.2f}") 

    else: 

        print("Plato no encontrado.") 

    print() 

 

# Ordenar por precio 

def ordenar_por_precio(platos): 

    n = len(platos) 

    for i in range(n): 

        for j in range(0, n - i - 1): 

            if platos[j]['precio'] > platos[j + 1]['precio']: 

                platos[j], platos[j + 1] = platos[j + 1], platos[j] 

    print("✔ Platos ordenados por precio ascendente.\n") 

 

# Filtrar por tipo 

def filtrar_por_tipo(platos): 

    tipo = input("Filtrar por tipo (entrada, principal, postre): ").strip().lower() 

    filtrados = [p for p in platos if p['tipo'] == tipo] 

    if filtrados: 

        print(f"\n--- Platos del tipo '{tipo}' ---") 

        for p in filtrados: 

            print(f"{p['nombre']} | ${p['precio']:.2f}") 

    else: 

        print("No se encontraron platos de ese tipo.") 

    print() 

 

# Menú principal  

def menu(): 

    platos = cargar_platos() 

    salir = False 

    while not salir: 

        print("=== Menú Interactivo de Restaurante ===") 

        print("1. Agregar plato") 

        print("2. Mostrar todos los platos") 

        print("3. Buscar plato por nombre") 

        print("4. Ordenar platos por precio") 

        print("5. Filtrar platos por tipo") 

        print("6. Guardar y salir") 

 

        opcion = input("Elija una opción: ") 

 

        if opcion == "1": 

            agregar_plato(platos) 

        elif opcion == "2": 

            mostrar_platos(platos) 

        elif opcion == "3": 

            buscar_plato(platos) 

        elif opcion == "4": 

            ordenar_por_precio(platos) 

        elif opcion == "5": 

            filtrar_por_tipo(platos) 

        elif opcion == "6": 

            guardar_platos(platos) 

            print("Datos guardados. ¡Hasta luego!") 

            salir = True 

        else: 

            print("Opción inválida.\n") 

 

# Ejecutar programa 

menu() 
