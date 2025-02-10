#Hacer función que realiza el promedio
def promedio_notas():

    #Inicializamos la variable lv_sumar_notas con 0
    lv_sumar_notas = 0

    #El for pide notas y luego las suma
    for i in range(3):
        lv_nota = float(input(f"Introduce la nota {i+1}: "))
        lv_sumar_notas = lv_sumar_notas + lv_nota

    #El return devuelve el promedio de las notas introducidas por el usuario
    return lv_sumar_notas / 3

#Definir el grado según la nota obtenida, pv_nota se refiere a parámetro variable nota para diferenciar con la global, pr se refiere a parametro return
def obtener_calificacion(pv_nota):
    if(pv_nota < 5):
        pr_calificacion = "SUSPENSO"
    elif(pv_nota >= 5 and pv_nota < 7):
        pr_calificacion = "APROBADO"
    elif(pv_nota >= 7 and pv_nota < 9):
        pr_calificacion = "NOTABLE"
    else:
        pr_calificacion = "SOBRESALIENTE"
    return pr_calificacion


#Inizializar la lista.
gv_mensajes = ["Mensaje inicial"]

#Se procesarán 5 alumnos (para las 5 vueltas, los valores de "i" serán 0, 1, 2, 3 y 4)
for i in range(5):

    #Pedir el nombre del alumno
    gv_nombre_alumno = input(f"{i+1} - Introduce el nombre del alumno: ")

    #Poner el nombre en mayúscula
    gv_nombre_alumno = gv_nombre_alumno.upper()

    #Llamar a la función para calcular el promedio
    gv_promedio_notas = promedio_notas()

    #Llamar a la función para obtener la calificación
    gv_calificacion = obtener_calificacion(gv_promedio_notas)

    #Cuando i = 0 sabemos que estamos trabajando con el primer alumno. Por ende, aquí no podemos usar APPEND. El primero tiene que ser agregado con una asignación 
    if(i == 0):
        gv_mensajes[0] = f"El promedio para {gv_nombre_alumno} es {gv_promedio_notas} y su calificación es {gv_calificacion}"
    #Cuando i no es 0 sabemos que estamos trabajando con el los siguientes alumnos. No con el primero. 
    else:
        gv_mensajes.append(f"El promedio para {gv_nombre_alumno} es {gv_promedio_notas} y su calificación es {gv_calificacion}")

    #Agrega una línea en blanco
    print("")

#Imprimir los resultados
for i in range(5):
    print(gv_mensajes[i])

