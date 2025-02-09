#Definir el grado según la nota obtenida, pv_nota se refiere a parámetro variable nota para diferenciar con la global, pr se refiere a parametro return
def mensaje_nota(pv_nota):
    if(pv_nota < 5):
        pr_mensaje = "SUSPENSO"
    elif(pv_nota >= 5 and pv_nota < 7):
        pr_mensaje = "APROBADO"
    elif(pv_nota >= 7 and pv_nota < 9):
        pr_mensaje = "NOTABLE"
    else:
        pr_mensaje = "SOBRESALIENTE"
    return pr_mensaje

#Pedir el usuario que introduzca la nota
gv_nota_usuario = float(input("Introduce la nota del alumno: "))

#Llamar a la función
gv_mensaje = mensaje_nota(gv_nota_usuario)

#Imprimir los resultados
print(gv_mensaje)
