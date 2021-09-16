def main():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Guillermo", "lastname": "Moreno"}

    super_list = [
        {"firstname": "Guillermo", "lastname": "Moreno"},
        {"firstname": "Gaby", "lastname": "Quezada"},
        {"firstname": "Karina", "lastname": "Moreno"},
        {"firstname": "Sergio", "lastname": "Mendez"},
        {"firstname": "Ana", "lastname": "Barba"},
    ]

    super_dict = {
        "natural_nums": [1 , 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 2.8, 3.4, 4.8]
    }

    # for key, value in super_dict.items():
    #     print(f"{key} - {value}")

    for i in super_list:
        print(i)


if __name__ == '__main__':
    main()