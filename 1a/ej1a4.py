'''
Enunciado:
Crea una función llamada "count_vowels(text_chain)" que reciba como parámetro
una cadena de texto de tipo string llamada 'text_chain' y retorne el número
de vocales, ya sean mayúsculas o minúsculas, sin tilde que se encuentren en dicha 
cadena de texto.

Parámetros:
- text_chain: Este parámetro admite únicamente strings.

Ejemplo: 
    Entrada:
    count_vowels('Hello world, this is an example.')

    Salida:
    9

Enunciat:
Crea una funció anomenada "count_vowels(text_chain)" que rebi com a paràmetre
una cadena de text de tipus string anomenada 'text_chain' i retorni el número
de vocals, ja siguin majúscules o minúscules, sense accent, que es trobin en 
aquesta cadena de text.

Paràmetres:
- text_chain: Aquest paràmetre només admet strings.

Exemple:
     Entrada:
     count_vowels('Hello world, this is an example.')

     Sortida:
     9

'''

def count_vowels(text_chain:str):

    vocales = ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U'] #Creamos una lista con las vocales
    contador = 0 #Iniciamos un contador de vocales

    for letra in text_chain: #Iteramos letra por letra
        if letra in vocales: #Comprobamos si la letra esta dentro de la lista
            contador += 1 #Si se encuentra una vocal el contador suma 1
            print(f"Vocal encontrada: {letra}") #Entonces imprime la vocal encontrada
    
    print(contador)
    

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script 
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
(count_vowels("Hello world, this is an example."))
