//Attributes (Data)
class Car2 {
    String brand;
    int speed;

//Method (Behaviour)
    void start() {
        System.out.println(brand + " is starting.");
    }

    void accelerate() {
        speed += 10;
        System.out.println(brand + "is now running at " + speed + " km/h");
    }
}