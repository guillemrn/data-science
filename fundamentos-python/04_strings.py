name = "Guillermo"
last_name = "Moreno"
print(name)
print(last_name)

full_name = name + " " + last_name
print(full_name)

quote = "I'm Guillermo"
print(quote)

# format
template = "Hello, my name is " + name + " and my last name is " + last_name
print(template)

templatev2 = "Hello, my name is {} and my last name is {}".format(name, last_name)
print(templatev2)

templatev3 = f"Hello, my name is {name} and my last name is {last_name}"
print(templatev3)