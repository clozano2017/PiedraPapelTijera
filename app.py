"""
Juego creado a partir de los conociminetos optenidos en el curso fundamentos de la progracion en python de platzi
"""
import random
# Lista de opciones válidas
opciones = ["piedra", "papel", "tijera"]

while True:
  # Pedimos al usuario que ingrese su elección
  eleccion_usuario = input("¿Piedra, papel o tijera? (Escribe 'terminar' para finalizar el juego): ").lower()

  # Si el usuario elige terminar, salimos del bucle
  if eleccion_usuario == "terminar":
    break

  # Si el usuario ingresa una elección inválida, seguimos pidiéndola
  if eleccion_usuario not in opciones:
    print("Opción inválida. Inténtelo de nuevo.")
    continue

  # Elige una opción aleatoria para el computador
  eleccion_computador = random.choice(opciones)

  # Mostramos las elecciones de ambos
  print(f"Tú elegiste {eleccion_usuario} y el computador eligió {eleccion_computador}.")

  # Evaluamos quién ganó
  if eleccion_usuario == eleccion_computador:
    print("Empate!")
  elif (eleccion_usuario == "piedra" and eleccion_computador == "tijera") or (eleccion_usuario == "papel" and eleccion_computador == "piedra") or (eleccion_usuario == "tijera" and eleccion_computador == "papel"):
    print("¡Ganaste!")
  else:
    print("Perdiste.")

print("¡Gracias por jugar!")
#Carlos Eduardo Lozano miranda 
# 3162950230
