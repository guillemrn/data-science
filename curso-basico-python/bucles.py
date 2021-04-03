def run():
    LIMITE = 100000000

    contador = 0
    potencia_4 = 4**contador
    while potencia_4 < LIMITE:
        print('4 elevado a ' + str(contador) + ' es igual a: ' + str(potencia_4))
        contador += 1
        potencia_4 = 4**contador

if __name__ == '__main__':
    run()