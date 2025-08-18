abstract class Animal{
    void sound() {}
}

class Dog extends Animal{
    void sound(){
        System.out.println("Bark");
    }
    void show(){
        super.sound();
        System.out.println("Dog shown");
    }
    public static void main(String[] args){
        Dog d = new Dog();
        d.sound();
        d.show();
    }
}
