def increment(x):
  return x + 1

def high_order_func(x, func):
  return x + func(x)

result = high_order_func(2, increment)
print(result)

incrementv2 = lambda x: x + 1
high_order_func_v2 = lambda x, func: x + func(x)
result = high_order_func_v2(2, increment)
print(result)