'''
Enunciado:
Implementa una función llamada "invert_text(text_chain)" que reciba como
parámetro una cadena de texto de tipo string llamada 'text_chain' y devuelva
el texto invertido.

Parámetros:
- text_chain: Este parámetro solo admite strings.

Ejemplo:
    Entrada:
    invert_text('Hello world!')

    Salida:
    !dlrow olleH

Enunciat:
Implementa una funció anomenada "invert_text(text_chain)" que rebi com
paràmetre una cadena de text de tipus string anomenada 'text_chain' i torni
el text invertit.

Paràmetres:
- text_chain: Aquest paràmetre només admet strings.

Exemple:
     Entrada:
     invert_text('Hello world!')

     Sortida:
     !dlrow olleH

'''

def invert_text(text_chain: str):
    resultado = [] #Creamos una lista para almacenar letra por letra

    # Recorremos cada letra y la agregamos a la lista
    for letra in text_chain:
        resultado.append(letra)

    ''' Unimos las letras invertidas y devolvemos el resultado
     Utilizamos [::-1] para invertir la lista
     La función .join es muy util para convertir listas en str
     La función .join se compone de 'separador'.join(iterable)
     En este caso no utilzamos seprador porque en una de las posiciónes de la lista
     tenemos guardado el espació entre palabras.

     Ej:
     letras = ['H', 'o', 'l', 'a']
     resultado = '/'.join(letras)

     salida:
     H/o/l/a
     '''

    return ''.join(resultado[::-1]) 


# Probar la función
texto_invertido = invert_text("Hello world!")
print(texto_invertido)
