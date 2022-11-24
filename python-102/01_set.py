# --Conjuntos
# Se pueden modificar
# No tiene un orden
# No permite duplicados

set_countries = {"mex", "col", "bol"}
print(set_countries)
print(type(set_countries))

set_numbers = {1, 2, 3, 4, 5}
print(set_numbers)

set_types = {1, "hola", False, 12.12}
print(set_types)

set_from_string = set("hola")
print(set_from_string)

set_from_tuple = set(("abc", "fgh"))
print(set_from_tuple)

numbers = [1, 2, 3, 1, 2, 3, 4]
set_numbers = set(numbers)
print(set_numbers)
unique_numbers = list(set_numbers)
print(unique_numbers)