import sys
print(sys.path)

import re
text = "Mi numero de telefono es 33 1515 2222, el codigo del pais es 57, mi numero de la suerte es 3"
result = re.findall("[0-9]+", text)
print(result)

import time
timestamp = time.time()
local = time.localtime()
result_time = time.asctime(local)
print(timestamp)
print(result_time)

import collections
numbers = [1, 2, 2, 2, 3, 3, 3, 4, 5]
counter = collections.Counter(numbers)
print(counter)