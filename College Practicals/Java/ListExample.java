import java.util.*;
public class ListExample {
    public static void main(String[] args) {
        List<String> animals = new ArrayList<>();
        animals.add("Dog");
        animals.add("Cat");
        animals.add("Elephant");
        animals.add("Cat"); //Duplicate allowed

        for (String animal : animals) {
            System.out.println(animal);
        }

        //Access by index
        System.out.println("First Animal: " + animals.get(0));

        //Remove an element
        animals.remove("Cat");
        System.out.println("After removing cat: " + animals);
    }
}
