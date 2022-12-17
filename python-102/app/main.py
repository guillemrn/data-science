import utils

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

def run():
  keys, values = utils.get_population()
  print(keys, values)

  country = input("Type a country: ")
  result = utils.population_by_country(data, country.title())
  print(result)

if __name__ == "__main__":
  run()