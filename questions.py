import random

categorias = {
    "tipos de dato" : ["cadena","entero","lista"],
    "conceptos de programacion": ["variable", "funcion", "bucle"],
    "general": ["python","programa"],
}

print("¡Bienvenido al Ahorcado!")
print()

print("Categorias:")
for categoria in categorias: 
    print(f"-{categoria}")

categoria_elegida = input("Elegí una Categoría: ").lower()

palabras_disponibles = random.sample (categorias[categoria_elegida], len (categorias[categoria_elegida]))

for word in palabras_disponibles: 
    guessed = []
    attempts = 6
    score=0


    while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "
        print(progress)

    # Verificar si el jugador ya adivinó la palabra completa
        if "_" not in progress:
            score+= 6
            print("¡Ganaste!")
            print (f"Puntaje Obtenido: {score}")
            break

        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")
        letter = input("Ingresá una letra: ")

        if len(letter) !=1 or not letter.isalpha():
            print("Entrada no válida")
            continue

        if letter in guessed:
            print("Ya usaste esa letra.")
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            attempts -= 1
            score-= 1
            print("Esa letra no está en la palabra.")
        print()
    else:
        print(f"¡Perdiste! La palabra era: {word}")
        score = 0
        print (f"Puntaje Obtenido: {score}")
        print()
    
    print("-------Nueva Ronda-------")

print("No hay más palabras en esta Categoria")