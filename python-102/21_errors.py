# print(0 / 0)
# print(result)
print("Hola")

sum = lambda x,y: x + y
assert sum(2,2) == 4

age = 10
if age < 18:
  raise Exception("No se permiten menores de edad")