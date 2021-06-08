import math

def main():
    squares = {i: round(math.sqrt(i), 2) for i in range(1, 1001)}

    print(squares)


if __name__ == '__main__':
    main()