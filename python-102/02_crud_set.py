set_countries = {"mex", "col", "bol"}

size = len(set_countries)
print(size)

print("mex" in set_countries)

# add
set_countries.add("peru")
print(set_countries)

# update
set_countries.update({"arg", "ecua", "peru"})
print(set_countries)

# remove
# set_countries.remove("arg")
set_countries.discard("arg")
print(set_countries)

set_countries.clear()
print(set_countries)