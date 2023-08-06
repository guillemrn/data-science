text = "Ella sabe programar en Python"

"""
print("JavaScript" in text)
print("Python" in text)
if "Python" in text:
    print("Elegiste bien")
else:
    print("Tambien elegiste bien")
"""

size = len(text)
print(size)

print(f"{text} => {text.upper()} => {text.lower()}")
print(text.count("a"))

print(text.swapcase())
print(text.startswith("Ella"))
print(text.endswith("Rust"))
print(text.replace("Python", "Go"))

text_2 = "this is a title"
print(text_2)
print(text_2.capitalize())
print(text_2.title())
print(text_2.isdigit())