#Introducir el nombre del estudiante, gv significa global variable
gv_student_name = input("Introduce el nombre del estudiante: ")

#Introducir las tres notas
gv_note_1 = float(input("Introduce la primera nota: "))
gv_note_2 = float(input("Introduce la segunda nota: "))
gv_note_3 = float(input("Introduce la tercera nota: "))

#Calcular la nota final
gv_final_note = (gv_note_1 + gv_note_2 + gv_note_3) / 3

#Mostrar el nombre del estudiante en mayúscula
gv_upper = gv_student_name.upper()

#Imprimir la nota final
print("La nota final: ")
print("Nombre", gv_student_name)
print("La nota final", gv_final_note)