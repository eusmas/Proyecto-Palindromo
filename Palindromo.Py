def palindromo(palabra):
    palabra=palabra.replace(" ", "").lower()
    if palabra[::]==palabra[::-1]:
        return True
    else:
        return False
#El operador de comparación == genera un boolean (True o False), podemos aprovechar esto y simplificar la función:
# def palindromo(palabra):
#     palabra = palabra.replace(' ','').lower()    
#     return palabra == palabra[::-1]


def run():
    palabra=input("Escribe una palabra: ")
    
    if palindromo(palabra):
        print("Es Palindromo")
    else:
        print("No es Palindromo")


if __name__ == "__main__":
    run()