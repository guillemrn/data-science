user_option = input("Elige piedra, papel o tijera: ")
user_option = user_option.lower()
computer_option = "tijera"

if user_option == computer_option:
    print("Empate 🤨")
elif user_option == "piedra":
    if computer_option == "tijera":
        print("Piedra gana a tijera")
        print("Gano el usuario 😎")
    else:
        print("Papel gana a la piedra")
        print("Gano la computadora 🤖")
elif user_option == "papel":
    if computer_option == "piedra":
        print("Papel gana a piedra")
        print("Gano el usuario 😎")
    else:
        print("Tijera gana a papel")
        print("Gano la computadora 🤖")
elif user_option == "tijera":
    if computer_option == "papel":
        print("Tijera gana a papel")
        print("Gano el usuario 😎")
    else:
        print("Piedra gana a tijera")
        print("Gano la computadora 🤖")
else:
    print("Elige un opcion correcta!")