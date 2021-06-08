def main():
    # natural_nums = {}
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         natural_nums[i] = i**3

    my_dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}

    print(my_dict)


if __name__ == '__main__':
    main()