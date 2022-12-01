items = [
  {
    "product": "t-shirt",
    "price": 100
  },
    {
    "product": "Jeans",
    "price": 200
  },
    {
    "product": "shirt",
    "price": 150
  },
    {
    "product": "t-shirt",
    "price": 300
  },
    {
    "product": "t-shirt",
    "price": 400
  },
]

prices = list(map(lambda item: item["price"], items))
print(prices)

def add_taxes(item):
  item["taxes"] = item["price"] * .19
  return item

new_items = list(map(add_taxes, items))
print(new_items)