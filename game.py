import datetime
import json
import random

player = input("Bienvenido Jugador, introduzca su nombre: ")

secret = random.randint(1, 30)
attempts = 0

with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())
    print("Estas son las puntuaciones actuales.¿Podrás superarlas?:")

new_score_list = sorted(score_list, key=lambda k: k['attempts'])[:3]

for score_dict in new_score_list:
    score_text = "El Jugador  {0} hizo {1} intentos el {2}. El número secreto fue el {3}.".format(score_dict.get("player_name"),
                                                                                         str(score_dict.get("attempts")),
                                                                                         score_dict.get("date"),
                                                                                         score_dict.get("secret_number"))
    print(score_text)

while True:
    guess = int(input("Escoja el número secreto (entre 1 y 30): "))
    attempts += 1

    if guess == secret:
        score_list.append({"attempts": attempts, "date": str(datetime.datetime.now()), "player_name": player,
                           "secret_number": secret})

        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))

        print("Felicidades, acertaste el número secreto. Era el  " + str(secret))
        print("Has necesitado " + str(attempts) + " Intentos")

        break
    elif guess > secret:
        print("intenta con un número más pequeño")
    elif guess < secret:
        print("intenta con un número más grande")