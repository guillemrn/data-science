def main():
    my_list = [1, 'hello', True, 4.5]
    my_dict = {"firstname": "Guillermo", "lastname": "Moreno"}

    super_list = [
        {"firstname": "Guillermo", "lastname": "Moreno"},
        {"firstname": "Gabriela", "lastname": "Quezada"},
        {"firstname": "Sergio", "lastname": "Mendez"},
        {"firstname": "Ale", "lastname": "RS"}
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "flotating_nums": [1.1, 2.2, 3.3, 4.4]
    }

    # for key, value in super_dict.items():
    #     print(key, "-", value)
    for i in super_list:
        print(i["firstname"], i["lastname"])


if __name__ == '__main__':
    main()