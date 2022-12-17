with open("./text.txt", "w+") as file:
  for line in file:
    print(line)
  file.write("=> Texto nuevo\n")
  file.write("=> Texto nuevo\n")
  file.write("=> Texto nuevo\n")