class Main {
    public static void main(String[] args) {
        Car car = new Car("AMQ123", new Account("Gabriela Quezada", "ANS846"));
        car.passenger = 4;
        car.printDataCar();

        Car car2 = new Car("SHD574", new Account("Guillermo Moreno", "HTK897"));
        car2.passenger = 3;
        car2.printDataCar();
    }
}