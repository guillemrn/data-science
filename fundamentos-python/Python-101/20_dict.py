person = {
    "name": "Gaby",
    "last_name": "Quezada",
    "langs": ["Python", "JavaScript"],
    "age": 26
}

print(person)

person["name"] = "Ana"
print(person)
person["langs"].append("Solidity")
print(person)

del person["last_name"]
person.pop("age")

print(person)


print(f"items => {person.items()}")
print(f"keys => {person.keys()}")
print(f"values => {person.values()}")