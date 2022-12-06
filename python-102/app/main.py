import utils

keys, values = utils.get_population()
print(keys, values)

data = [
  {
    "Country": "Mexico",
    "Population": 50000
  },
  {
    "Country": "Bolivia",
    "Population": 50000
  }
]
country = input("Type a country: ")
result = utils.population_by_country(data, country.title())
print(result)