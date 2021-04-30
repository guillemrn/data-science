def run():
    usr_name = input('What is your name?: ')
    num = input('Write a number: ')
    print((usr_name + '\n') * int(num))

if __name__ == '__main__':
    run()