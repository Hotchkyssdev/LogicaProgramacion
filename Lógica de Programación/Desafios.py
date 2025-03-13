'''
Semana 0: Hola Mundo
'''
print("Hola Mundo")
print("")
'''
Semana 1:

Desafio Extra:

Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos) 
pares, y que no son ni el 16 ni múltiplos de 3.
'''
for number in range(10,56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)

print("")

'''
Semana 2:

DIFICULTAD EXTRA: FIZZ BUZZ

Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
'''
def fizzbuzz(str1, str2):
    cont = 0
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(str1, str2)
        elif number % 3 == 0:
            print(str1)
        elif number % 5 == 0:
            print(str2)
        else:
            print(number)
            cont = cont + 1
    return cont

print("La cantidad de números que devuelve la función es: ", fizzbuzz("Fizz", "Buzz"))
print("")

'''
Semana 3: 

DIFICULTAD EXTRA

Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
'''

def agenda():
    agenda = {}

    def insertar_contacto():
        telefono = input("Ingrese el teléfono del contacto: ")
        if telefono.isdigit() and len(telefono) > 0 and len(telefono) <= 11:
            agenda[nombre] = telefono
        else:
            print("Error: El teléfono debe ser menor a 12 números.")

    while True:
        print("")
        print("1. Buscar Contacto")
        print("2. Insertar Contacto")
        print("3. Actualizar Contacto")
        print("4. Eliminar Contacto")
        print("5. Salir")
        opcion = input("\nSelecciona una opción: ")

        match opcion:
            case "1":
                nombre = input("Ingrese el nombre contacto a buscar: ")
                if nombre in agenda:
                    print(f"El contacto se llama {nombre} y su número de teléfono es {agenda[nombre]}.")
                else:
                    print(f"El contacto {nombre} no existe.")
            case "2":
                nombre = input("Ingrese el nombre del nuevo contacto: ")
                insertar_contacto()
            case "3":
                nombre = input("Ingrese el nombre del contacto a actualizar: ")
                if nombre in agenda:
                    insertar_contacto()
                else:
                    print(f"El contacto {nombre} no existe.")
            case "4":
                nombre = input("Ingrese el nombre del contacto a eliminar: ")
                if nombre in agenda:
                    del agenda[nombre]
                else:
                    print(f"El contacto {nombre} no existe.")
            case "5":
                print("Programa Finalizado.")
                break
            case _:
                print("Opción Inválida. Elige una del 1 al 5.")


agenda()
print("")

'''
Semana 4:

DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
'''

def comprobacion(palabra1: str, palabra2: str):
    
    #Palíndromo
    print(f"¿Es {palabra1} un palíndromo?: {palabra1 == palabra1[::-1]}")
    print(f"¿Es {palabra2} un palíndromo?: {palabra2 == palabra2[::-1]}")
    print("")

    #Anagrama
    print(f"¿Es {palabra1} un anagrama?: {sorted(palabra1) == sorted(palabra2)}")
    print("")
    #Isograma
    def isograma(palabra: str) -> bool:
        palabra_dict = dict()
        for caracter in palabra_dict:
            palabra_dict[caracter] = palabra_dict.get(caracter, 0) + 1

        isograma = True
        valores = palabra_dict.values()
        isograma_len = valores[0]
        for palabra_cont in isograma_len:
            if palabra_cont != isograma_len:
                isograma = False
                break
        return isograma
    
    print(f"¿Es {palabra1} un isograma?: {len(palabra1) == len(set(palabra1))}")
    print(f"¿Es {palabra2} un isograma?: {len(palabra2) == len(set(palabra2))}")


comprobacion("radar", "python")
comprobacion("amor", "roma")
print("")

'''
Semana 5:

DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como
 * variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime
 *   el valor de las variables originales y las nuevas, comprobando que se ha invertido
 *   su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
'''

def intercambio_valor(valorA: int, valorB: int) -> tuple:
    temp = valorA
    valorA = valorB
    valorB = temp
    return valorA, valorB

int1 = 10
int2 = 20
int3, int4 = intercambio_valor(int1 , int2)
print(f"{int1}, {int2}")
print(f"{int3}, {int4}")

def intercambio_referencia(valorA: list, valorB: list) -> tuple:
    temp = valorA
    valorA = valorB
    valorB = temp
    return valorA, valorB

lista1 = [10, 20]
lista2 = [30, 40]
lista3, lista4 = intercambio_referencia(lista1 , lista2)
print(f"{lista1}, {lista2}")
print(f"{lista3}, {lista4}")
print("")

'''
Semana 6:

DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
'''

def factorial(numero: int) -> int:
    if numero < 0:
        print("El número debe ser mayor a 0.")
        return 0
    elif numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)

fact = int(input("Ingrese el número para hacer su factorial: "))
print(factorial(fact))

def fibonacci(numero: int) -> int:
    if numero <= 0:
        print("El número debe ser positivo.")
    elif numero == 1:
        return 0
    elif numero == 2:
        return 1
    else:
        return fibonacci(numero - 1) + fibonacci(numero - 2)

posicion = int(input("Ingrese la posición de la sucesion de fibonacci: "))
print(fibonacci(posicion))
print("")

'''
Semana 7:

DIFICULTAD EXTRA (opcional):
- Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
- Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
'''

def navegadorweb():
    pila = []
    while True:
        accion = input("Añade una url o interactúa con palabras adelante/atrás/salir: ")
        if accion == "salir":
            print("Saliendo del navegador.")
            break
        elif accion == "adelante":
            pass
        elif accion == "atras":
            if len(pila) > 0:
                pila.pop()
        else:
            pila.append(accion)

        if len(pila) > 0:
            print(f"Has navegado a la web: {pila[len(pila) - 1]}")
        else:
            print("Estás en la página de inicio.")

navegadorweb()

def impresora_compartida():
    cola = []
    while True:
        accion = input("Añade un documento o selecciona imprimir/salir: ")
        if accion == "salir":
            break
        elif accion == "imprimir":
            if len(cola) > 0:
                print(f"Imprimiendo: {cola.pop(0)}")
        else:
            cola.append(accion)
        
        print(f"Cola de Impresión: {cola}")

impresora_compartida()
print("")

'''
Semana 8:

DIFICULTAD EXTRA (Opcional):
Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
'''

#Pila/Stack (LIFO)

class Pila:

    def __init__(self):
        self.pila = []

    def push(self, item):
        self.pila.append(item)
    
    def pop(self):
        if self.contador() == 0:
            return None
        return self.pila.pop()
    
    def contador(self):
        return len(self.pila)
    
    def print(self):
        for item in reversed(self.pila):
            print(item)

mi_pila = Pila()
mi_pila.push("A")
mi_pila.push("B")
mi_pila.push("C")
print(mi_pila.contador())
mi_pila.print()
mi_pila.pop()
print(mi_pila.contador())
print(mi_pila.pop())
print(mi_pila.pop())
print(mi_pila.pop())
print(mi_pila.pop())
print(mi_pila.pop())
print(mi_pila.contador())
print("")

#Cola/Queue (FIFO)

class Cola:

    def __init__(self):
        self.cola = []

    def enqueue(self, item):
        self.cola.append(item)

    def dequeue(self):
        if self.contador() == 0:
            return None
        return self.cola.pop(0)

    def contador(self):
        return len(self.cola)
    
    def print(self):
        for item in (self.cola):
            print(item)

mi_cola = Cola()
mi_cola.enqueue("A")
mi_cola.enqueue("B")
mi_cola.enqueue("C")
print(mi_cola.contador())
mi_cola.print()
mi_cola.dequeue()
print(mi_cola.contador())
print(mi_cola.dequeue())
print(mi_cola.dequeue())
print(mi_cola.dequeue())
print(mi_cola.dequeue())
print(mi_cola.dequeue())
print(mi_cola.contador())
print("")