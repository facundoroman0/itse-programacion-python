"""
DESAFIO 10
Un instituto de enseñanza de inglés necesita un programa que le permita, cada día,
procesar observaciones sobre las clases de ese día. El instituto dicta clases a
estudiantes de distintos niveles y cada nivel tiene clases en un día de la semana
diferente: los lunes se dicta el nivel inicial, los martes el nivel intermedio, los miércoles
el nivel avanzado, los jueves son para práctica hablada y los viernes se dicta inglés
para viajeros.
Se debe comenzar por solicitar al usuario que ingrese la fecha actual en formato "día,
DD/MM", donde [día] es un día de la semana, DD es el número de día y MM es el
número de mes. Si el usuario ingresa un día de la semana inexistente o una fecha cuyo
día supere el número 31 o el mes supere el número 12, finalizar el programa indicando
que se produjo un error. Debe permitirse que ingrese el día de la semana en
minúsculas o mayúsculas indistintamente. Como precondición se tiene que lo
ingresado por el usuario tendrá la forma <[alfanumérico], [numérico]/[numérico]>.
Una vez indicada la fecha, el usuario necesita poder indicar si ese día se tomaron
exámenes, pero eso sólo si se trata de los niveles inicial, intermedio o avanzado, ya
que las prácticas habladas y el inglés para viajeros no tienen exámenes. Si hubo
exámenes, el usuario ingresará cuántos alumnos aprobaron y cuántos no, y el
programa le mostrará el porcentaje de aprobados.
Si el día fue el correspondiente a práctica hablada, el usuario deberá ingresar el
porcentaje de asistencia a clase y el programa le indicará "asistió la mayoría" en caso
de que la asistencia sea mayor al 50% o "no asistió la mayoría" si no es así.
Si se trata del inglés para viajeros y la fecha actual corresponde al día 1 del mes 1 o del
mes 7, se deberá imprimir "Comienzo de nuevo ciclo" y solicitar al usuario que ingrese
la cantidad de alumnos del nuevo ciclo y el arancel en $ por cada alumno, para luego
imprimir el ingreso total en $.
"""

print(f"- - - - - - PROGRAMA - - - - - -")
print("Ingrese la fecha actual [Dia, DD/MM]")
print("Dia: ")

dia_palabra = input().lower()
dd = int(input("DD: "))
mm = int(input("MM: "))

if (dd >= 1 and dd <= 31) and (mm >= 1 and mm <=12):
    
    if dia_palabra in ["lunes", "martes", "miercoles"]:
        print(f"¿Hubo Examen?")
        hubo_examen = input("(S/N): ").lower()
        if hubo_examen=="s":
            aprobados = int(input("Cantidad de aprobados: "))
            desaprobados = int(input("Cantidad de desaprobados: "))
            total_alumnos = aprobados + desaprobados
            print(f"El porcentaje de aprobados es de: {(aprobados/total_alumnos)*100:.2f}%")

    elif dia_palabra == "jueves":
        porcentaje_asistencia = int(input("Ingrese el porcentaje de asistencia: "))
        if porcentaje_asistencia > 50:
            print(f"Asistió a mayoría")
        else:
            print(f"No asistió la mayoría")
    else:
        if dia_palabra == "viernes" and (dd == 1 and (mm == 1 or mm == 7)):
            print("\nComienza un nuevo ciclo")
            cantidad_alumnos = int(input("Ingrese la cantidad de alumnos: "))
            arancel_alumnos = float(input("Ingrese el arancel por cada alumno: "))
            print(f"El total recaudado es de: %{cantidad_alumnos*arancel_alumnos}")
else:
    print("Se produjo un error!")


