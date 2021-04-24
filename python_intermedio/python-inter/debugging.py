def divisors(num):
    divisors = []
    try:
        if num < 0:
            raise ValueError('You must be write a positive number')
        for i in range(1, num + 1):
            if num % i == 0:
                divisors.append(i)
        return divisors
    except ValueError as ve:
        print(ve)

def run():
    try:
        num = int(input('Write a numer: '))
        print(divisors(num))
        print('Finished')
    except ValueError:
        print('You must be write a number')


if __name__ == '__main__':
    run()