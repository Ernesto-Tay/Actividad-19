import random
class lista:
    def __init__(self):
        self.lista = []

    def agregar(self, item):
        self.lista.append(item)
    def mostrar(self, item):
        print(f"Nombre: {item.nombre}")
        print(f"Precio: Q{item.precio}")
        print(f"Peso: {item.peso}")
        print(f"Tipo: {item.tipo}")

    def eliminar(self, item):
        self.lista.remove(item)
main_lista=lista()


class Galleta:
    def __init__(self,nombre,precio,peso):
        self.nombre = nombre
        self.precio = precio
        self.peso = peso
        self.tipo = "Básica"

    def validar(self):
        while True:
            try:
                self.nombre = input("\nIngrese el nombre de la galleta: ")
                self.precio = int(input("Ingrese el precio del galleta: "))
                self.peso = int(input("Ingrese el peso del galleta: "))
                if self.nombre.len()<3:
                    raise ValueError("El nombre debe tener al menos 3 letras")
                if self.precio <= 0:
                    raise ValueError("El precio debe ser mayor a 0")
                if self.peso <= 0:
                    raise ValueError("El peso debe ser mayor a 0")

            except ValueError:
                print("Las entradas numéricas deben ser números enteros")
            except Exception as e:
                print("Error inesperado: ",e)

    def mostrar_info(self):
        if not main_lista.lista:
            print("No hay galletas en la lista")
        else:
            for i in main_lista.lista:
                main_lista.mostrar(i)
                print(f"Tipo: {i.tipo}")


class Relleno:
    def __init__(self,sabor_relleno):
        self.sabor_relleno = sabor_relleno


    def describir_relleno(self):
        descripciones = [f"Un exquisito sabor a {self.sabor_relleno}", f"Una cremosa mezcla que sabe a {self.sabor_relleno}", f"Una explosión de {self.sabor_relleno} que te deja deseando más"]
        print(random.choice(descripciones))


class GalletaChispas(Galleta):
    def __init__(self,nombre,precio,peso,cantidad_chispas):
        super().__init__(nombre,precio,peso)
        self.cantidad_chispas = cantidad_chispas
        self.tipo = "chispas"

    def validar(self):
        while True:
            try:
                self.nombre = input("\nIngrese el nombre de la galleta: ")
                self.precio = int(input("Ingrese el precio del galleta: "))
                self.peso = int(input("Ingrese el peso del galleta: "))
                self.cantidad_chispas = int(input("Ingrese la cantidad de chispas: "))
                if self.nombre.len()<3:
                    raise ValueError("El nombre debe tener al menos 3 letras")
                if self.precio <= 0:
                    raise ValueError("El precio debe ser mayor a 0")
                if self.peso <= 0:
                    raise ValueError("El peso debe ser mayor a 0")
                if self.cantidad_chispas <= 0:
                    raise ValueError("La cantidad de chispas debe ser mayor a 0")

            except ValueError:
                print("Las entradas numéricas deben ser números enteros")
            except Exception as e:
                print("Error inesperado: ",e)


    def mostrar_info(self):
        for i in main_lista.lista:
            if i.tipo == "chispas":
                main_lista.mostrar(i)


class GalletaRellena(Galleta, Relleno):
    def __init__(self,nombre,precio,peso,sabor_relleno):
        super().__init__(nombre,precio,peso)
        self.sabor_relleno = sabor_relleno
        self.tipo = "relleno"

    def validar(self):
        while True:
            try:
                self.nombre = input("\nIngrese el nombre de la galleta: ")
                self.precio = int(input("Ingrese el precio del galleta: "))
                self.peso = int(input("Ingrese el peso del galleta: "))
                self.sabor_relleno = input("Ingrese el tipo de relleno: ")
                if self.nombre.len()<3:
                    raise ValueError("El nombre debe tener al menos 3 letras")
                if self.precio <= 0:
                    raise ValueError("El precio debe ser mayor a 0")
                if self.peso <= 0:
                    raise ValueError("El peso debe ser mayor a 0")
                if not self.sabor_relleno:
                    raise ValueError("Debe ingresar un nombre de relleno")

            except ValueError:
                print("Las entradas numéricas deben ser números enteros")
            except Exception as e:
                print("Error inesperado: ",e)


    def mostrar_info(self):
        for i in main_lista.lista:
            if i.tipo == "relleno":
                main_lista.mostrar(i)

while True:
    print("\n\n---------- MENÚ DE GALLETAS ----------\n1. Registrar galleta básica\n2. Registrar galleta con chispas\n3. Registrar galleta rellena\n4. Listar galletas por tipo\n5. Buscar galletap por nombre\n. 6. Eliminar galleta por nombre\n. 7. Salir")
    select = input("Seleccione una opción: ")
    match select:
        case "1":
            galleta = Galleta("",0,0)
            galleta.validar()
            main_lista.agregar(galleta)

        case "2":
            galletaChispada = GalletaChispas("","","",0)
            galletaChispada.validar()
            main_lista.agregar(galletaChispada)

        case "3":
            pass
        case "4":
            pass
        case "5":
            pass
        case "6":
            pass
        case "7":
            print("Saliendo...")
            break
        case _:
            print("Opción inválida, intente nuevamnente")