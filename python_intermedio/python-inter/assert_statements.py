def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    num = input('Write a number: ')
    assert num.isnumeric() and int(num) > 0, 'You must be write a number'
    print(divisors(int(num)))
    print('Finished')


if __name__ == '__main__':
    run()