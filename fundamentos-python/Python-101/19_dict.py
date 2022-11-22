my_dict = {}
print(type(my_dict))

my_dict = {
    "name": "Gabriela",
    "last_name": "Quezada",
    "age": 26
}

print(my_dict)
print(len(my_dict))

print(my_dict["age"])
print(my_dict["last_name"]) # Detiene la ejecucion
print(my_dict.get("age")) # .get regresa un valor -None-

print("avion" in my_dict)
print("age" in my_dict)
