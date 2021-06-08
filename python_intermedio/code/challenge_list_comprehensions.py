def main():
    list_num = [i for i in range(1, 100001) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]

    print(list_num)


if __name__ == '__main__':
    main()