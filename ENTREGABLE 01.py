# Importamos la librería NumPy para trabajar con matrices y vectores

import numpy as np # type: ignore


# El usuario ingresa cuántas horas estudia por semana
# Usa float para permitir decimales 
horas = float(input("¿Cuántas horas estudias a la semana?: "))

# Aplicamos una fórmula de regresión lineal simple (representa un modelo de Machine Learning supervisado simple que predice una variable continua (la nota))
# Fórmula: nota = pendiente * horas + intercepto
# En este caso, cada hora suma 3 puntos y el punto base es 5
nota = 3 * horas + 5

# Mostramos la nota estimada, redondeando a 2 decimales
print(f"Tu nota final estimada sería: {nota:.2f}")

# Paso 4: Función para crear un vector y validar la entrada
def crear_vector():
    while True:  # Este bucle se repetirá hasta que se ingrese un vector válido
        try:
        
            vector = np.array([float(x) for x in input("Ingresa 3 números para el vector (separados por espacio): ").split()])
            if len(vector) != 3:
                print("Error: Debes ingresar exactamente 3 números.")
            else:
                return vector
        except ValueError:
            print("¡Error! Todos los valores deben ser números.")

# Crear los vectores A, B y C
A = crear_vector()
B = crear_vector()
C = crear_vector()


# Mostrar los vectores
print("Vector A:", A)
print("Vector B:", B)
print("Vector C:", C)

# Paso 5: Propiedades Aritméticas con NumPy

# Propiedad Conmutativa (A + B == B + A)
def propiedad_conmutativa(A, B):
    print("\n--- Propiedad Conmutativa ---")
    print(f"A + B: {A} + {B} = {A + B}")
    print(f"B + A: {B} + {A} = {B + A}")
    return np.array_equal(A + B, B + A)

# Propiedad Asociativa ((A + B) + C == A + (B + C))
def propiedad_asociativa(A, B, C):
    print("\n--- Propiedad Asociativa ---")
    print(f"(A + B) + C: ({A} + {B}) + {C} = {A + B + C}")
    print(f"A + (B + C): {A} + ({B} + {C}) = {A + B + C}")
    return np.array_equal((A + B) + C, A + (B + C))

# Propiedad Distributiva (k * (A + B) == k * A + k * B) con k = 2
def propiedad_distributiva(A, B, k=2):
    print("\n--- Propiedad Distributiva ---")
    print(f"k * (A + B): {k} * ({A} + {B}) = {k * (A + B)}")
    print(f"k * A + k * B: {k} * {A} + {k} * {B} = {k * A + k * B}")
    return np.array_equal(k * (A + B), k * A + k * B)

# Propiedad del Inverso Aditivo (A + (-A) == 0)
def propiedad_inverso(A):
    print("\n--- Propiedad del Inverso Aditivo ---")
    print(f"A: {A}")
    print(f"-A: {-A}")
    print(f"A + (-A): {A} + {-A} = {A + (-A)}")
    return np.array_equal(A + (-A), np.zeros_like(A))

# Propiedad de Identidad Aditiva (A + 0 == A)
def propiedad_identidad(A):
    print("\n--- Propiedad de Identidad Aditiva ---")
    print(f"A: {A}")
    print(f"0: {np.zeros_like(A)}")
    print(f"A + 0: {A} + {np.zeros_like(A)} = {A + np.zeros_like(A)}")
    return np.array_equal(A + np.zeros_like(A), A)


# Evaluamos las propiedades
print("\n--- Validación de Propiedades Aritméticas ---")
print(f"¿Conmutativa? {propiedad_conmutativa(A, B)}")
print(f"¿Asociativa? {propiedad_asociativa(A, B, C)}")
print(f"¿Distributiva? {propiedad_distributiva(A, B)}")
print(f"¿Inverso Aditivo? {propiedad_inverso(A)}")
print(f"¿Identidad Aditiva? {propiedad_identidad(A)}")