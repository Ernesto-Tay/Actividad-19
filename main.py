import random
class lista:
    def __init__(self):
        self.lista = []

    def agregar(self, item):
        self.lista.append(item)
    def mostrar(self, item):
        print(f"Nombre: {item["nombre"]}")
        print(f"Precio: {item["precio"]}")
        print(f"Peso: {item["peso"]}")
        print(f"Tipo: {item["tipo"]}")

    def eliminar(self, item):
        self.lista.remove(item)
main_lista=lista()


class Galleta:
    def __init__(self,nombre,precio,peso):
        self.nombre = nombre
        self.precio = precio
        self.peso = peso

    def validar(self):
        while True:
            nombre_ok = True
            peso_ok = True
            precio_ok = True
            if self.nombre.len()<=1:
                print("El nombre debe tener un largo mínimo de 3 letras")
                nombre_ok = False
            if self.precio <= 0:
                print("El precio debe ser mayor a cero")
                peso_ok = False
            if self.peso <= 0:
                print("El peso debe ser mayor a cero")
                peso_ok = False

            if nombre_ok and peso_ok and precio_ok:
                break
            else:
                while True:
                    try:
                        self.nombre = input("\nIngrese el nombre de la galleta: ")
                        self.precio = int(input("Ingrese el precio del galleta: "))
                        self.peso = int(input("Ingrese el peso del galleta: "))
                        break
                    except ValueError:
                        print("Las entradas numéricas deben ser números enteros")
                    except Exception as e:
                        print("Error inesperado: ",e)

    def mostrar_info(self):
        for i in main_lista.lista:
            main_lista.mostrar(i)


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

    def mostrar_info(self):
        for i in main_lista.lista:
            if i["tipo"] == "chispas":
                main_lista.mostrar(i)


class GalletaRellena(Galleta, Relleno):
    def __init__(self,nombre,precio,peso,sabor_relleno):
        super().__init__(nombre,precio,peso)
        self.sabor_relleno = sabor_relleno
        self.tipo = "relleno"

    def mostrar_info(self):
        for i in main_lista.lista:
            if i["tipo"] == "relleno":
                main_lista.mostrar(i)

