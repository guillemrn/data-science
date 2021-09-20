def main():
    # variable = [element for element in iterable if conditio]
    n = [1, 2, 3, 4, 5]
    list_squares = [i**2 for i in n]

    print(list_squares)


if __name__ == "__main__":
    main()