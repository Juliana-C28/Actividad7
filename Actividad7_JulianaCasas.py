

#Actividad 7 Juliana Casas Ramirez
from dataclasses import dataclass
# Defina una clase Elemento usando el decorador @dataclass que contenga lo siguiente
@dataclass
class Elemento:
    nombre: str #Un atributo nombre de tipo str
    #Un método especial para soportar la operación de igualdad == que permita comparar dos objetos de la clase Elemento indicando si el nombre es igual.

    def igualdad (self, otro):
        if isinstance(otro, Elemento):
            return self.nombre == otro.nombre
        return False
#Defina una clase Conjunto
class Conjunto:
    contador = 0

    def __init__(self, nombre): #Un atributo de instancia que representa la lista de objetos de la clase Elemento
        self.elementos = [] # inicialice el atributo como una lista vacía.
        self.nombre = nombre #Un atributo de instancia nombre que contiene el nombre del conjunto. Inicialice dicho atributo a partir de un parámetro dado en el método inicializador.
        Conjunto.contador += 1 #Un atributo de clase contador que lleve registro del número de instancias creadas. Incremente en uno el valor de dicho atributo en el método inicializador.
        self.__id = Conjunto.contador#Un atributo “privado” __id al cual se le asigna el valor actual del atributo de clase contador al momento de la inicialización. Defina una propiedad de solo lectura para dicho atributo
 

    def id(self):
        return self.__id

    def contiene(self, elemento): #Un método de instancia contiene, el cual recibe como parámetro un objeto de la clase Elemento y retorna un valor bool indicando si el conjunto contiene ya un elemento con el mismo nombre.
        return any(e == elemento for e in self.elementos)

    def agregar_elemento(self, elemento): #Un método de instancia agregar_elemento, el cual recibe un objeto de la clase Elemento como parámetro y lo agrega a la lista de elementos si no está contenido ya en el conjunto (utilice el método anterior para verificar)
        if not self.contiene(elemento):
            self.elementos.append(elemento)

    def unir(self, otro_conjunto): #Un método unir que recibe otro conjunto como parámetro y agrega sus elementos a la lista de elementos del objeto actual en el que se invoca el método. Tenga en cuenta que un conjunto no puede tener elementos repetidos. Implemente también esta operación por medio de un método especial para soportar el operador +.
        nuevo_conjunto = Conjunto(f"{self.nombre} UNION {otro_conjunto.nombre}")
        for elemento in self.elementos:
            nuevo_conjunto.agregar_elemento(elemento)
        for elemento in otro_conjunto.elementos:
            nuevo_conjunto.agregar_elemento(elemento)
        return nuevo_conjunto

    def __add__(self, otro_conjunto):
        return self.unir(otro_conjunto)

    @classmethod
    def intersectar(cls, conjunto1, conjunto2):#Un método de clase intersectar que recibe dos conjuntos como parámetros y retorna un nuevo conjunto con los elementos de la intersección de los conjuntos dados. Recuerde que la intersección de dos conjuntos está conformada por los elementos que pertenecen a ambos conjuntos. El nombre del conjunto resultante debe ser "<Nombre Conjunto 1> INTERSECTADO <Nombre Conjunto 2>.
        elementos_comunes = [elem for elem in conjunto1.elementos if conjunto2.contiene(elem)]
        nombre_resultado = f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}"
        resultado = Conjunto(nombre_resultado)
        resultado.elementos = elementos_comunes
        return resultado

    def __str__(self): #Un método __str__ que retorne una representación legible de un conjunto con el siguiente formato

        elementos_str = ", ".join(elemento.nombre for elemento in self.elementos)
        return f"Conjunto {self.nombre}: ({elementos_str})"

conjunto_A = Conjunto("A") # Crear conjuntos
conjunto_B = Conjunto("B")

elemento_1 = Elemento("1")
elemento_2 = Elemento("2")  #Crear elementos
elemento_3 = Elemento("3")

interseccion = Conjunto.intersectar(conjunto_A, conjunto_B) # Intersectar dos conjuntos
print(interseccion)
conjunto_A.agregar_elemento(elemento_1)  # Agregar elementos a los conjuntos
conjunto_A.agregar_elemento(elemento_2)
conjunto_B.agregar_elemento(elemento_3)
union = conjunto_A + conjunto_B # Unir dos conjuntos
print(union)


