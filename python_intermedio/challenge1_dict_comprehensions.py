import math


def main():
    square_dict = {i: math.sqrt(i) for i in range(1, 1001)}

    print(square_dict)


if __name__ == "__main__":
    main()