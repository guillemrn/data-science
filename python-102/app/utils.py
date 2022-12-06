def get_population():
  keys = ["col", "bol", "mex"]
  values = [4000, 5000, 6000]
  return keys, values

def population_by_country(data, country):
  result = list(filter(lambda item: item["Country"] == country, data))
  return result
