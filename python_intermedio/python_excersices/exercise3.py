def run():
    pswd = 'password'
    question = input('What is the password?: ')
    question = question.lower()
    if question == pswd:
        print('Is the same')
    else:
        print('try another')


if __name__ == '__main__':
    run()