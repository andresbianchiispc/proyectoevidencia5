from dispositivo import Dispositivo
from accion import Accion
from automatizacion import Automatizacion
from usuario import Usuario

# -----------------------------
# Crear usuario
# -----------------------------
nombre_usuario = input("Ingrese su nombre: ")
email_usuario = input("Ingrese su email: ")
usuario = Usuario(nombre_usuario, email_usuario)
print(f"\nUsuario creado: {usuario}\n")

# -----------------------------
# Funciones de menú
# -----------------------------
def agregar_dispositivo():
    nombre_disp = input("Ingrese el nombre del dispositivo: ")
    tipo_disp = input("Ingrese el tipo del dispositivo: ")
    dispositivo = Dispositivo(nombre_disp, tipo_disp)
    usuario.agregar_dispositivo(dispositivo)
    print(f"Dispositivo '{nombre_disp}' agregado.\n")

def listar_dispositivos():
    dispositivos = usuario.dispositivos
    if dispositivos:
        print("Dispositivos del usuario:")
        for d in dispositivos:
            print(f"- {d}")
    else:
        print("No hay dispositivos agregados aún.")
    print()

def ejecutar_accion():
    if not usuario.dispositivos:
        print("No hay dispositivos para ejecutar acciones.\n")
        return
    print("Dispositivos disponibles:")
    for i, d in enumerate(usuario.dispositivos):
        print(f"{i+1}. {d.get_nombre_dispositivo()}")
    try:
        idx = int(input("Seleccione un dispositivo por número: ")) - 1
        dispositivo = usuario.dispositivos[idx]
    except (ValueError, IndexError):
        print("Selección inválida.\n")
        return
    acciones = ["encender", "apagar", "set_nombre", "cambiar_estado", "set_tiempo_encendido", "set_tiempo_apagado"]
    
    tipo_accion = input("Ingrese la acción: ")
    valor_configurado = None
    if tipo_accion == "set_nombre":
        valor_configurado = input("Ingrese el nuevo nombre: ")
    elif tipo_accion == "set_tiempo_encendido":
        valor_configurado = input("Ingrese el tiempo de encendido en minutos: ")
    elif tipo_accion == "set_tiempo_apagado":
        valor_configurado = input("Ingrese el tiempo de apagado en minutos: ")
    elif tipo_accion == "set_brillo":
        valor_configurado = input("Ingrese el brillo (0-100): ")
    accion = Accion(tipo_accion, valor_configurado)
    resultado = dispositivo.ejecutar_accion(accion)
    print(resultado + "\n")

def mostrar_estado():
    if not usuario.dispositivos:
        print("No hay dispositivos agregados.\n")
        return
    print("Estado de los dispositivos:")
    for d in usuario.dispositivos:
        print(d)
    print()

def agregar_automatizacion():
    descripcion = input("Ingrese la descripción de la automatización: ")
    automatizacion = Automatizacion(descripcion)
    while True:
        print("\nAgregar acción a la automatización:")
        print("Opciones: encender, apagar, cambiar_estado, set_nombre, set_tipo, set_estado, set_tiempo_encendido, set_tiempo_apagado")
        tipo_accion = input("Tipo de acción (o 'fin' para terminar): ")
        if tipo_accion == "fin":
            break
        valor_configurado = None
        if tipo_accion in ["set_nombre", "set_tipo", "set_estado", "set_tiempo_encendido", "set_tiempo_apagado"]:
            valor_configurado = input("Ingrese el valor configurado: ")
        accion = Accion(tipo_accion, valor_configurado)
        automatizacion.agregar_accion(accion)
        print("Acción agregada.")
    usuario.agregar_automatizacion(automatizacion)
    print(f"Automatización '{descripcion}' agregada.\n")

def listar_automatizaciones():
    automatizaciones = usuario.automatizaciones
    if automatizaciones:
        print("Automatizaciones del usuario:")
        for i, a in enumerate(automatizaciones):
            print(f"{i+1}. {a.get_descripcion()}")
    else:
        print("No hay automatizaciones agregadas aún.")
    print()

def ejecutar_automatizaciones():
    if not usuario.automatizaciones:
        print("No hay automatizaciones para ejecutar.\n")
        return
    resultados = usuario.ejecutar_automatizaciones()
    print("Resultados de la ejecución de automatizaciones:")
    for r in resultados:
        print(r)
    print()

# -----------------------------
# Menú principal
# -----------------------------
while True:
    print("===== MENÚ SMART HOME =====")
    print("1. Agregar dispositivo")
    print("2. Listar dispositivos")
    print("3. Ejecutar acción en dispositivo")
    print("4. Mostrar estado de dispositivos")
    print("5. Agregar automatización")
    print("6. Listar automatizaciones")
    print("7. Ejecutar automatizaciones")
    print("8. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_dispositivo()
    elif opcion == "2":
        listar_dispositivos()
    elif opcion == "3":
        ejecutar_accion()
    elif opcion == "4":
        mostrar_estado()
    elif opcion == "5":
        agregar_automatizacion()
    elif opcion == "6":
        listar_automatizaciones()
    elif opcion == "7":
        ejecutar_automatizaciones()
    elif opcion == "8":
        print("Saliendo del sistema. ¡Hasta luego!")
        break
    else:
        print("Opción inválida, intente nuevamente.\n")
