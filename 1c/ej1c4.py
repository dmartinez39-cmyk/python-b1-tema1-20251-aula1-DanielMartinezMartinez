""" 
Enunciado:
Escribe una función llamada is_palindrome(word) que reciba como parámetro
una cadena word y verifique si es un palíndromo utilizando recursión.
La función debe devolver True si la cadena es un palíndromo y False en
caso contrario.

Parámetros:
    word (str): una cadena de caracteres.

Ejemplo:
    Entrada:
    word = "racecar"
    print(is_palindrome(word))

    Salida:
    True



Enunciat:

Enunciat:
Escriu una funció anomenada is_palindrome(word) que rebi com a paràmetre
una cadena word i verifiqui si és un palíndrom utilitzant recursió.
La funció ha de tornar True si la cadena és un palíndrom i False a
cas contrari.

Paràmetres:
     word (str): una cadena de caràcters.

Exemple:
     Entrada:
     word = "racecar"
     print(is_palindrome(word))

     Sortida:
     True

"""


def is_palindrome(word):
    # Normalizamos el texto: sin espacios y en minúsculas
    word = word.replace(" ", "").lower()

    # Caso base: si tiene 0 o 1 letra, es palíndromo
    if len(word) <= 1:
        return True
    # Si la primera y última letra son distintas, no es palíndromo
    elif word[0] != word[-1]:
        return False
    else:
        # Paso recursivo: verificamos el interior de la palabra
        return is_palindrome(word[1:-1])


# Ejemplo de uso
word = "racecar"
print(is_palindrome(word))  # 👉 True
