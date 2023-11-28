#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------
import random
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

# write 'hello world' to the console
print('hello world')



def jugar():
    opciones = ['piedra', 'papel', 'tijeras']
    oponente = random.choice(opciones)

    jugador = input("Elige piedra, papel o tijeras: ").lower()

    if jugador in opciones:
        print(f"\nTu oponente eligió: {oponente}")

        if jugador == oponente:
            print("¡Empate!")
        elif (jugador == 'piedra' and oponente == 'tijeras') or \
             (jugador == 'papel' and oponente == 'piedra') or \
             (jugador == 'tijeras' and oponente == 'papel'):
            print("¡Ganaste!")
        else:
            print("¡Perdiste!")
    else:
        print("Opción no válida. Por favor, elige piedra, papel o tijeras.")

if __name__ == "__main__":
    while True:
        jugar()

        volver_a_jugar = input("\n¿Quieres jugar de nuevo? (s/n): ").lower()
        if volver_a_jugar != 's':
            print("¡Gracias por jugar! ¡Hasta luego!")
            break
