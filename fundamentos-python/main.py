import random

options = ("piedra", "papel", "tijera")
computer_wins = 0
user_wins = 0
rounds = 1


while True:
    print("*" * 20)
    print(f"ROUND {rounds}")
    print("*" * 20)

    print("-" * 20)
    print(f"Computador: {computer_wins}")
    print(f"Usuario: {user_wins}")
    print("-" * 20)

    user_option = input("Elige piedra, papel o tijera: ")
    user_option = user_option.lower()
    computer_option = random.choice(options)

    print(f"User option => {user_option}")
    print(f"Computer option => {computer_option}")

    if user_option == computer_option:
        print("Empate 🤨")
    elif user_option == "piedra":
        if computer_option == "tijera":
            print("Piedra gana a tijera")
            print("Gano el usuario 😎")
            user_wins += 1
        else:
            print("Papel gana a la piedra")
            print("Gano la computadora 🤖")
            computer_wins += 1
    elif user_option == "papel":
        if computer_option == "piedra":
            print("Papel gana a piedra")
            print("Gano el usuario 😎")
            user_wins += 1
        else:
            print("Tijera gana a papel")
            print("Gano la computadora 🤖")
            computer_wins += 1
    elif user_option == "tijera":
        if computer_option == "papel":
            print("Tijera gana a papel")
            print("Gano el usuario 😎")
            user_wins += 1
        else:
            print("Piedra gana a tijera")
            print("Gano la computadora 🤖")
            computer_wins += 1
    else:
        print("Elige un opcion correcta!")


    if computer_wins == 2:
        print(f"El computador obtuvo {computer_wins} victorias, es el vecendor!!!")
        break
    if user_wins == 2:
        print(f"El usuario obtuvo {user_wins} victorias, es el vecendor!!!")
        break


    rounds += 1