# Daniel Felipe Cardenas Romero 
# DDYA
# SEMANA_1

def main():
    num = pedir_num()
    print("--- Punto 1 ---")
    verificar_pos(num)
    print("--- Punto 2 ---")
    verificar_fib(num)
    print("--- Punto 3 ---")
    verificar_primo(num)
    print("--- Punto 4 y 5 ---")
    num1 = pedir_num()
    num2 = pedir_num()
    verificar_pos(num1)
    verificar_fib(num1)
    verificar_primo(num1)
    verificar_pos(num2)
    verificar_fib(num2)
    verificar_primo(num2)
    sumar_multi_int(num1, num2)
    print("--- Punto 6 ---")
    elevar(num1, num2)
    print("--- Punto 7 ---")
    codigo = pedir_codigo()
    codigo_por_pares_acumulado(codigo)
    print("--- Punto 8 y 9 ---")
    mensaje = pedir_mensaje()
    separar_123abc(mensaje)
    print("--- Punto 10 ---")
    numero_abc = pedir_num_abc()
    posicion_abc(numero_abc)

def pedir_num():
    num = int(input("Ingrese un numero: "))
    return num

def pedir_num_abc(): 
    num = int(input("Ingrese un numero entre 1 y 27: "))
    while num < 1 or num > 27:
        print("Error, por favor ingresa un numero valido")
        num = int(input("Ingrese un numero entre 1 y 27: "))
    return num

def pedir_mensaje():
    mensaje = input("Ingrese el mensaje alfanumerico para eliminar las letras: ")
    return mensaje

def pedir_codigo():
    codigo = input("Ingrese su codigo de estudiante: ")
    return codigo

def verificar_pos(num):
    if num < 0:
        print(f"su numero {num} es negativo.")
    elif num > 0:
        print(f"su numero {num} es positivo.")
    else:
        print(f"su numero es 0")
    
def verificar_fib(num):
    es_fib = False
    if num >= 0:
        a, b = 0, 1
        if num == 0 or num == 1:
            es_fib = True
        else:
            while a+b <= num:
                c = a+b
                if c == num:
                    es_fib = True
                    break
                a, b = b, c
    if es_fib:
        print(f"Su numero {num} es un numero que pertenece a fibonacci.")
    else: 
        print(f"Su numero {num} no es un numero fibonacci")

def verificar_primo(num):
    es_primo = False
    if num <= 1:
        es_primo = False
    else:
        for rep in range(2, num):
            if num % rep == 0:
                es_primo = True
                break #Ya encontro un divisor x lo q no es primo
    if not es_primo:
        print(f"Su numero {num} es un numero primo")
    else:
        print(f"Su numero {num} no es un numero primo")

def sumar_multi_int(num1, num2):
    lista = []
    if num1 <= num2 and not (num1 < 0 and num2 < 0):
        for rep in range(num1, num2+1):
            lista.append(rep)
        sumatoria = 0
        for rep in range(len(lista)):
            sumatoria += lista[rep]
        print(f"La sumatoria total de los extremos y los intermedios es: {sumatoria}.")
    elif num2 > num1 and not (num1 < 0 and num2 < 0):
        for rep in range(num2, num1+1):
            lista.append(rep)
        sumatoria = 0
        for rep in range(len(lista)):
            sumatoria += lista[rep]
        print(f"La sumatoria total de los extremos y los intermedios es: {sumatoria}.")
    if num1 and num2 < 0:
        if num2 >= num1:
            for rep in range(num1, num2+1):
                lista.append(rep)
            multi = 1
            for rep in range(len(lista)):
                multi *= lista[rep]
            print(f"La multiplicacion total de los extremos y los intermedios es: {multi}.")
        elif num1 > num2:
            for rep in range(num2, num1+1):
                lista.append(rep)
            multi = 1
            for rep in range(len(lista)):
                multi *= lista[rep]
            print(f"La multiplicacion total de los extremos y los intermedios es: {multi}.")
 
def elevar(num1, num2):
    if num1 % 2 == 0:
        print(f"su numero 1: {num1} es par, al elevar al cubo queda {num1**3}")
    else:
        print(f"su numero 1: {num1} es impar, al elevar al cuadrado queda {num1**2}")
    if num2 % 2 == 0:
        print(f"su numero 2: {num2} es par, al elevar al cubo queda {num2**3}")
    else:
        print(f"su numero 2: {num2} es impar, al elevar al cuadrado queda {num2**2}")

def codigo_por_pares_acumulado(codigo):
    print(f"Procesando el código {codigo} por parejas consecutivas:\n")
    suma_acu = 0  
    for i in range(len(codigo) - 1):
        num1 = int(codigo[i])
        num2 = int(codigo[i + 1])
        print(f"--> Pareja {i+1} ({num1} y {num2}):")
        sumar_multi_int(num1, num2)
        menor = min(num1, num2)
        mayor = max(num1, num2) #Para el acumulado
        suma_pareja = 0
        for rep in range(menor, mayor + 1):
            suma_pareja += rep
        suma_acu += suma_pareja
        
        print(f"    [Acumulado actual: {suma_acu}]")
    print(f"La suma acumulada del codigo es: {suma_acu}")

def separar_123abc(mensaje):
    mens_numerico = []
    mens_alfabetico = []
    for rep in mensaje:
        if rep == "0" or rep == "1" or rep == "2" or rep == "3" or rep == "4" or rep == "5" or rep == "6" or rep == "7" or rep == "8" or rep == "9":
            mens_numerico.append(rep)
        else:
            mens_alfabetico.append(rep)
    print("El mensaje numerico resultante es: ")
    print("".join(mens_numerico))

    for rep in mens_alfabetico:
        if rep == "a" or rep == "e" or rep == "i" or rep == "o" or rep == "u":
            print(f"la letra {rep} es vocal.")
        else:
            print(f"la letra {rep} es consonante. ")
    
def posicion_abc(numero_abc):
    abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                  "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u",
                  "v", "w", "x", "y", "z"]
    print(f"Su numero {numero_abc} en el abecedario conrresponde a la letra {abecedario[numero_abc-1]}")
                  
main()