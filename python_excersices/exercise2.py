def run():
    usr_age = int(input('How old are you?: '))
    OLD = 18
    if usr_age >= OLD:
        print("You're old")
    else:
        print('Sorry, too young')


if __name__ == '__main__':
    run()