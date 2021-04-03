def run():
    # for count in range(1000):
    #   if count % 2 != 0:
    #       continue
    #   print(count)

    # for i in range(10000):
    #   print(i)
    #   if i == 7896:
    #       break

    # text = input('Write something: ')
    # for l in text:
    #     if l == 'o':
    #         break
    #     print(l)

    count = 1
    LIMIT = 100
    while count < LIMIT:
        print(count)
        count += 1
        if count == 34:
            break


if __name__ == '__main__':
    run()