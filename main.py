from claseplanAhorro import PlanAhorro
import csv
#Defino la funcion menu en el algoritmo principal

if __name__ == '__main__':
    with open("planes.csv", "r", encoding='utf-8') as archivo:
        lector = csv.reader(archivo, delimiter=';')
        lista_planes = []
        for fila in lector:
            codigo = str(fila[0].split()[0])
            modelo = str(fila[1].split()[0])
            version_vehiculo = str(fila[2].split()[0])
            precio = int(fila[3].split()[0]) #type:ignore
            cant_cuotas = int(fila[4].split()[0]) #type:ignore
            pagar_cuotas = int(fila[5].split()[0]) #type:ignore
            planes_guardados = PlanAhorro(codigo, modelo ,version_vehiculo, precio, pagar_cuotas)
            lista_planes.append(planes_guardados)
    todo = PlanAhorro(codigo,modelo,version_vehiculo,precio,pagar_cuotas)
    print(f"{todo.mostrarmenu(lista_planes)}")