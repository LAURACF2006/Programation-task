def obtener_entrada_usuario(mensaje):
    """
    Función para obtener la entrada del usuario con un mensaje dado.
    """
    try:
        return input(mensaje)  # Obtener la entrada del usuario
    except Exception as e:
        print(f"Ocurrió un error al recibir la entrada: {e}")
        return None

def preguntar_informacion_usuario():
    """
    Función para preguntar al usuario su nombre, edad y hobbies.
    Utiliza una serie de preguntas y maneja posibles errores en la entrada.
    """
    print("¡Hola! Soy tu asistente de chatbot. Vamos a conocernos mejor.")
    
    # Obtener el nombre del usuario
    nombre = obtener_entrada_usuario("¿Cuál es tu nombre?: ")
    if not nombre:
        print("No se pudo recibir el nombre. Usaré 'Invitado' como nombre.")
        nombre = "Invitado"
    
    # Obtener la edad del usuario
    while True:
        edad = obtener_entrada_usuario(f"{nombre}, ¿cuántos años tienes?: ")
        try:
            # convertir la entrada a un número entero
            edad = int(edad)
            break  # Si es exitoso, salir del bucle
        except ValueError:
            print("Por favor, ingresa un número válido para la edad.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
    
    # Obtener los hobbies del usuario
    hobbies = obtener_entrada_usuario(f"Cuéntame, {nombre}, ¿cuáles son tus hobbies?: ")
    if not hobbies:
        print("No se pudieron recibir los hobbies. Usaré 'Ninguno' como respuesta.")
        hobbies = "Ninguno"
    
    # Mostrar la información recopilada
    print(" Información del Usuario")
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Hobbies: {hobbies}")
    print("¡Gracias por compartir esta información conmigo!")

# Ejecutar la función del chatbot
    preguntar_informacion_usuario()
