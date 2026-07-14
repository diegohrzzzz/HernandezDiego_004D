#FUNCIONES
def validar_codigo(codigo:str):
    return codigo.strip() != ""
def menu():
    print(f"===== MENU PRINCIPAL =====")
    print(f"1. Cupos por tipo de plan")
    print(f"2. Busqueda de planes por rango de precio")
    print(f"3. Actualizar precio de plan")
    print(f"4. Agregar plan")
    print(f"5. Eliminar plan")
    print(f"6. Salir")

def leer_opcion():
    try:
        op = int(input(f"Ingrese una opcion: "))
        if op not in [1,2,3,4,5,6]:
            return 0
        return op
    except ValueError:
        return 0

def cupos_tipo(tipo, planes, inscripcciones ):
    total_cupos = 0
    for codigo in planes:
        tipo = planes[codigo][1]
        cupos_actuales = inscripcciones[codigo][1]
        
        if tipo == cupos_actuales:
            total_cupos += cupos_actuales
    print(f"Total de cupos disponibles es: {total_cupos}")
    
    
def busqueda_precio(p_min, p_max, planes, inscripcciones):
    encontrados = []
    for codigo in planes:
        nombre = planes[codigo][0]
        cupos = inscripcciones[codigo][0]
        presupuesto = inscripcciones[codigo][1]
        
    if cupos >= p_min and cupos <= p_max and presupuesto > 0:
        nombre_codigo = nombre + "--" + codigo
        encontrados.append(nombre_codigo)

def buscar_codigo(codigo):
    if codigo:
        return True
    else:
        return False

def actualizar_precio(codigo, nuevo_precio):
    pass
        
    
#PROGRAMA PRINCIPAL
planes = {
    'F001': ['Plan Basico', 'Mensual', 1, False, False, 'Libre'],
    'F002' : ['Plan Full', 'Mensual', 1, True, True, 'Libre'],
    'F003' : ['Plan Estudiante', 'Trimestral', 3, False, True, 'Tarde'],
    'F004' : ['Plan Senior', 'Trimestral', 3, True, False, 'Mañana'],
    'F005': ['Plan Anual Pro', 'anual', 12, True, True, 'libre'],
    'F006': ['Plan nocturno', 'mensual', 1, False, True, 'noche']
    
}

inscripcciones = {
    'F001': [14990, 30],
    'F002' : [22990, 10],
    'F003' : [39990, 0],
    'F004' : [35990, 6],
    'F005': [159990, 2],
    'F006': [18990, 15]
    
}

while True:
    menu()
    op = leer_opcion()
    
    if op == 1:
        tipo = input(f"Ingrese el plan a buscar: ")
        cupos_tipo(tipo, planes, inscripcciones )
        
    elif op == 2:
        while True:
            p_min = int(input("Ingrese precio minimo: "))
            p_max = int(input("Ingrese precio maximo: "))
            
            try:
                if p_min < 0 or p_max < 0 or p_min > p_max:
                    print(f"Dato invalido vuelva a intentarlo")
                else:
                    break
            except ValueError:
                print(f"Dato invalido vuelva a intentarlo")
                continue
        busqueda_precio(p_min, p_max, planes, inscripcciones)

        
    elif op == 3:
        respuesta = "s"
        while respuesta == "s":
            codigo = input("Ingrese el codigo del animal")
            try:
                nuevo_precio = int(input("Ingrese el nuevo precio"))
                if buscar_codigo(codigo) == False:
                    print(f"Nuevo peso invalido")
                    continue
            except ValueError:
                continue
            
            
    elif op == 4:
        pass
    elif op == 5:
        pass
    elif op == 6:
        print(f"Usted a salido del programa")
        break
    else:
        print(f"Ingrese una opcion valida")
    