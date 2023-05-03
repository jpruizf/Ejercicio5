#Defino la clase Plan Ahorro
#import csv


class PlanAhorro:
    __codigo: str
    __modelo: str
    __version_vehiculo: str
    __precio: int
    __cant_cuotas: int
    __pagar_cuotas: int
    __total_licitar: int

    def __init__(self, codigo, modelo, version_vehiculo, precio, pagar_cuotas):
        self.__codigo = codigo
        self.__modelo = modelo
        self.__version_vehiculo = version_vehiculo
        self.__precio = precio
        self.__cant_cuotas = 60
        self.__pagar_cuotas = pagar_cuotas
        self.total_licitar = 0

    def getcodigo(self):
        return self.__codigo
    
    def getmodelo(self):
        return self.__modelo
    
    def getversionvehiculo(self):
        return self.__version_vehiculo
    
    def getprecio(self):
        return self.__precio
    
    def getcantidad_cuotas(self):
        return self.__cant_cuotas
    
    def getpagar_cuotas(self):
        return self.__pagar_cuotas
    def valorCuota(self):
        val = int(self.__precio * 0.10 // self.__cant_cuotas)
        return val
    def encontrarModelo(self,lista_planes,codigo,modelo,version_vehiculo,valor_vehiculo):
        i = 0
        while (i < len(lista_planes)):
            if lista_planes[i][0] == codigo and lista_planes[i][1] == modelo and lista_planes[i][2] == version_vehiculo and lista_planes[i][3] == valor_vehiculo:
                self.__precio = valor_vehiculo
            else:
                i += 1
                print("Codigo no encontrado :/")
            break
        return self.__precio
    
    def mostrarmenu(self, planes):
        print("********|Menu de opciones|*********\n")
        print("1. Actualizar el valor del vehiculo para cada plan ")
        print("2. Dando un valor del plan de cuotas ver codigo del plan, modelo del vehiculo, version del vehiculo ")
        print("3. Ver el monto total pagado para licitar el vehiculo ")
        print("4. Dado un codigo de plan modificar la cantidad de cuotas que el cliente debe pagar para licitar ")
        while True:
            opcion = input("Ingrese una opcion >> ")
            if opcion == '1':
                codigo = input("Ingrese el codigo del plan ")
                modelo = input("Ingrese el modelo del vehiculo:")
                version = input("Ingrese la version del vehiculo: ")
                valor_vehiculo = int(input("Ingrese el valor actual del vehiculo:"))
                print(f"El precio se actualizo con exito. Precio actualizado >> {self.encontrarModelo(planes,codigo,modelo,version,valor_vehiculo)}")
            elif opcion == '2':
                valor_vehiculo = int(input("Ingrese un valor: "))
                print("Planes cuya cuota es inferior a", valor_vehiculo, ':')
                i = 0
                while i in len(planes):
                    if self.__precio < valor_vehiculo:
                        print(f"Codigo >> {self.__codigo} | Modelo >> {self.__modelo} | Version del vehiculo >> {self.__version_vehiculo}")
            elif opcion == '3':
                codigo = input("Ingrese el codigo del plan: ")
                while i in len(planes):
                    if self.__codigo == codigo:
                        self.__total_licitar = (int(self.__cant_cuotas * self.valorCuota()))
                        print(f"El monto para licitar el vehiculo es: {self.__total_licitar}")
            elif opcion == '4':
                codigo = input("Ingrese el codigo del plan: ")
                i = 0
                while i in len(planes):
                    if self.__codigo == codigo:
                        self.__cant_cuotas -= self.__total_licitar
                        print("La cantidad de cuotas para licitar se ha modificado con exito.")
                        break
                    else:
                        print("No se ha encontrado ningun plan del codigo ingresado.")
            elif opcion == '5':
                break
            else:
                print("Opcion ingresada no encontrada. Ingrese una opcion valida. ")                                