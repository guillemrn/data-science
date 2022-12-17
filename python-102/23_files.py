file = open("./text.txt")

"""
print(file.read())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
"""

for line in file:
  print(line)

file.close()


# Con esto no nos preocupamos por cerrar el archivo, ya que python lo cierra automaticamente
with open("./text.txt") as file:
  for line in file:
    print(line)