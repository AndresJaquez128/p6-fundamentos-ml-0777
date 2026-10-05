# JAQUEZ CAMACHO JOEL ANDRES 0074 
# ==========================================
# SECCIÓN 1: VARIABLES 
# ==========================================

# Ejemplo 1: Creación básica de variables
x = 5
y = "John"
print("1. Variables - Ejemplo 1:", x, y)

# Ejemplo 2: Cambiar el tipo de dato dinámicamente
a = 4       # 'a' es entero (int)
a = "Sally" # 'a' cambia a cadena (str)
print("1. Variables - Ejemplo 2:", a)

# Ejemplo 3: Especificar tipo mediante Casting
x_str = str(3)    # '3'
y_int = int(3)    # 3
z_float = float(3) # 3.0
print("1. Variables - Ejemplo 3:", x_str, y_int, z_float)


# ==========================================
# SECCIÓN 2: MÚLTIPLES VARIABLES 
# ==========================================

# Ejemplo 1: Múltiples valores a múltiples variables
x, y, z = "Orange", "Banana", "Cherry"
print("\n2. Múltiples Variables - Ejemplo 1:", x, y, z)

# Ejemplo 2: Un mismo valor a múltiples variables
var1 = var2 = var3 = "Apple"
print("2. Múltiples Variables - Ejemplo 2:", var1, var2, var3)

# Ejemplo 3: Desempaquetar una lista (Unpacking)
fruits = ["apple", "banana", "cherry"]
f1, f2, f3 = fruits
print("2. Múltiples Variables - Ejemplo 3:", f1, f2, f3)


# ==========================================
# SECCIÓN 3: TIPOS DE DATOS (python_datatypes.asp)
# ==========================================

# Ejemplo 1: Texto y números (str, int, float)
texto = "Hello World"
entero = 20
decimal = 20.5
print("\n3. Tipos de Datos - Ejemplo 1:", type(texto), type(entero), type(decimal))

# Ejemplo 2: Colecciones (list, tuple, dict)
lista = ["apple", "banana", "cherry"]
tupla = ("apple", "banana", "cherry")
diccionario = {"name": "John", "age": 36}
print("3. Tipos de Datos - Ejemplo 2:", type(lista), type(tupla), type(diccionario))

# Ejemplo 3: Booleano y Conjunto (bool, set)
booleano = True
conjunto = {"apple", "banana"}
print("3. Tipos de Datos - Ejemplo 3:", type(booleano), type(conjunto))


# ==========================================
# SECCIÓN 4: OPERADORES ARITMÉTICOS 
# ==========================================

# Ejemplo 1: Suma, resta y multiplicación
suma = 10 + 5
resta = 10 - 5
multiplicacion = 10 * 5
print("\n4. Aritméticos - Ejemplo 1:", suma, resta, multiplicacion)

# Ejemplo 2: División y división entera
division = 10 / 3
division_entera = 10 // 3
print("4. Aritméticos - Ejemplo 2:", division, "| Entera:", division_entera)

# Ejemplo 3: Módulo y exponenciación
modulo = 10 % 3
exponente = 2 ** 4
print("4. Aritméticos - Ejemplo 3 - Módulo:", modulo, "| Exponente:", exponente)


# ==========================================
# SECCIÓN 5: OPERADORES DE COMPARACIÓN 
# ==========================================

x_comp, y_comp = 5, 10

# Ejemplo 1: Igualdad (==) y desigualdad (!=)
print("\n5. Comparación - Ejemplo 1 (== / !=):", x_comp == y_comp, x_comp != y_comp)

# Ejemplo 2: Mayor que (>) y menor que (<)
print("5. Comparación - Ejemplo 2 (> / <):", x_comp > y_comp, x_comp < y_comp)

# Ejemplo 3: Mayor o igual (>=) y menor o igual (<=)
print("5. Comparación - Ejemplo 3 (>= / <=):", x_comp >= 5, y_comp <= 10)


# ==========================================
# SECCIÓN 6: OPERADORES LÓGICOS 
# ==========================================

n = 5

# Ejemplo 1: Operador AND
res_and = n > 3 and n < 10
print("\n6. Lógicos - Ejemplo 1 (and):", res_and)

# Ejemplo 2: Operador OR
res_or = n > 10 or n < 6
print("6. Lógicos - Ejemplo 2 (or):", res_or)

# Ejemplo 3: Operador NOT
res_not = not(n > 3 and n < 10)
print("6. Lógicos - Ejemplo 3 (not):", res_not)


# ==========================================
# IMPRESIÓN FINAL SOLICITADA
# ==========================================
print("\nNUMERO CONTROL 0074 PROGRAMA HECHO POR JAQUEZ ANDRES ULTIMO PRINT")