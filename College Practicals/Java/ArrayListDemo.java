import java.util.ArrayList;
public class ArrayListDemo {
    public static void main(String[] args) {
        ArrayList<String> fruits = new ArrayList<>();

        fruits.add("Apple");
        fruits.add("Banana");
        fruits.add("Orange");
        fruits.add("Banana");

        System.out.println("Fruits List: "+ fruits);

        //Access by index
        System.out.println("Fruits List: "+ fruits.get(0));

        //Remove an item
        fruits.remove("Banana");

        //Iterate
        for(String fruit : fruits){
            System.out.println(fruit);
        }
    }
}
