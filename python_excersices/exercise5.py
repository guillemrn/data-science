def run():
    peso = int(input('¿Cual es tu peso en kilos?: '))
    estatura = float(input('¿Cual es tu estatura en metros?: '))
    imc = peso / estatura**2
    imc = round(imc, 2)
    print(imc)


if __name__ == '__main__':
    run()