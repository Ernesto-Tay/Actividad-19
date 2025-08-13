import random
class RegistroDuplicadoError(Exception):
    "Pasa cuando se registra una entrada ya existente en una lista"
    pass

class NombreCortoError(Exception):
    "Pasa cuando el nombre es muy corto"
    pass

class NombreNumericoError(Exception):
    "pasa cuando el nombre tiene números"
    pass


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

    def buscar(self, item):
        if not self.lista:
            print("Aún no hay galletas")
        else:
            for galleta in self.lista:
                if galleta.nombre == item:
                    print(f"Galleta encontrada\nNombre: {galleta.nombre}\nPrecio: Q{galleta.precio}\nPeso: {galleta.peso}\nTipo: {galleta.tipo}")
                    break
            else:
                print("No se encontró la galleta")

    def eliminar(self, item):
        if not self.lista:
            print("Aún no hay galletas")
        else:
            for galleta in self.lista:
                if galleta.nombre == item:
                    self.lista.remove(galleta)
                    print("Galleta eliminada")
                    break
            else:
                print("No se encontró la galleta")
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
                self.nombre = input("\nIngrese el nombre de la galleta: ").capitalize()
                self.precio = int(input("Ingrese el precio del galleta: "))
                self.peso = int(input("Ingrese el peso del galleta: "))
                if len(self.nombre)<3:
                    raise NombreCortoError("El nombre debe tener al menos 3 letras")
                elif not self.nombre.isalpha():
                    raise NombreNumericoError("El nombre no puede tener números")
                elif any(cookie.nombre == self.nombre for cookie in main_lista.lista if main_lista.lista):
                    raise RegistroDuplicadoError("Ya existe una galleta con ese nombre")
                if self.precio <= 0:
                    raise ValueError("El precio debe ser mayor a 0")
                if self.peso <= 0:
                    raise ValueError("El peso debe ser mayor a 0")

            except ValueError:
                print("Las entradas numéricas deben ser números enteros")
            except NombreCortoError as e:
                print(e)
            except NombreNumericoError as e:
                print(e)
            except RegistroDuplicadoError as e:
                print(e)
            except Exception as e:
                print("Error inesperado: ",e)

    def mostrar_info(self):
        if not main_lista.lista:
            print("No hay galletas en la lista")
        else:
            print("\n---------- GALLETAS BÁSICAS ----------")
            for i in main_lista.lista:
                if i.tipo == "Básica":
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
                self.nombre = input("\nIngrese el nombre de la galleta: ").capitalize()
                self.precio = int(input("Ingrese el precio del galleta: "))
                self.peso = int(input("Ingrese el peso del galleta: "))
                self.cantidad_chispas = int(input("Ingrese la cantidad de chispas: "))
                if len(self.nombre)<3:
                    raise NombreCortoError("El nombre debe tener al menos 3 letras")
                elif not self.nombre.isalpha():
                    raise NombreNumericoError("El nombre no puede tener números")
                elif any(cookie.nombre == self.nombre for cookie in main_lista.lista if main_lista.lista):
                    raise RegistroDuplicadoError("Ya existe una galleta con ese nombre")
                if self.precio <= 0:
                    raise ValueError("El precio debe ser mayor a 0")
                if self.peso <= 0:
                    raise ValueError("El peso debe ser mayor a 0")
                if self.cantidad_chispas <= 0:
                    raise ValueError("La cantidad de chispas debe ser mayor a 0")

            except ValueError:
                print("Las entradas numéricas deben ser números enteros")
            except NombreCortoError as e:
                print(e)
            except NombreNumericoError as e:
                print(e)
            except RegistroDuplicadoError as e:
                print(e)
            except Exception as e:
                print("Error inesperado: ",e)


    def mostrar_info(self):
        for i in main_lista.lista:
            if i.tipo == "chispas":
                main_lista.mostrar(i)
                print(f"Chispas: {i.cantidad_chispas}")


class GalletaRellena(Galleta, Relleno):
    def __init__(self,nombre,precio,peso,sabor_relleno):
        Galleta.__init__(self,nombre,precio,peso)
        Relleno.__init__(self,sabor_relleno)
        self.tipo = "relleno"

    def validar(self):
        while True:
            try:
                self.nombre = input("\nIngrese el nombre de la galleta: ").capitalize()
                self.precio = int(input("Ingrese el precio del galleta: "))
                self.peso = int(input("Ingrese el peso del galleta: "))
                self.sabor_relleno = input("Ingrese el tipo de relleno: ")
                if len(self.nombre)<3:
                    raise NombreCortoError("El nombre debe tener al menos 3 letras")
                elif not self.nombre.isalpha():
                    raise NombreNumericoError("El nombre no puede tener números")
                elif any( cookie.nombre == self.nombre for cookie in main_lista.lista if main_lista.lista):
                    raise RegistroDuplicadoError("Ya existe una galleta con ese nombre")
                if self.precio <= 0:
                    raise ValueError("El precio debe ser mayor a 0")
                if self.peso <= 0:
                    raise ValueError("El peso debe ser mayor a 0")
                if not self.sabor_relleno:
                    raise ValueError("Debe ingresar un nombre de relleno")

            except ValueError:
                print("Las entradas numéricas deben ser números enteros")
            except NombreCortoError as e:
                print(e)
            except NombreNumericoError as e:
                print(e)
            except RegistroDuplicadoError as e:
                print(e)
            except Exception as e:
                print("Error inesperado: ",e)

    def mostrar_info(self):
        for i in main_lista.lista:
            if i.tipo == "relleno":
                main_lista.mostrar(i)
                print("Relleno:", end = "")
                i.describir_relleno

while True:
    print("\n\n---------- MENÚ DE GALLETAS ----------\n1. Registrar galleta básica\n2. Registrar galleta con chispas\n3. Registrar galleta rellena\n4. Listar galletas por tipo\n5. Buscar galletap por nombre\n6. Eliminar galleta por nombre\n7. Salir")
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
            galletaRellena = GalletaRellena("","","",0)
            galletaRellena.validar()
            main_lista.agregar(galletaRellena)

        case "4":
            galleta = Galleta("", 0, 0)
            galleta.mostrar_info()

            galletaChispas = GalletaChispas("", "", "", 0)
            galletaChispas.mostrar_info()

            galletaRellena = GalletaRellena("", "", "", 0)
            galletaRellena.mostrar_info()

        case "5":
            while True:
                name_search = input("\nIngrese el nombre de la galleta a buscar: ")
                if not name_search.isalpha():
                    print("El nombre de la galleta no debe tener números")
                else:
                    break
            main_lista.buscar(name_search)

        case "6":
            while True:
                name_search = input("\nIngrese el nombre de la galleta a eliminar: ")
                if not name_search.isalpha():
                    print("El nombre de la galleta no debe tener números")
                else:
                    main_lista.eliminar(name_search)
                    break
        case "7":
            print("Saliendo...")
            break
        case _:
            print("Opción inválida, intente nuevamnente")