import java.util.*;

public class SetExample {
    public static void main(String[] args) {
        Set<String>names = new HashSet<>();
        names.add("Raju");
        names.add("Simran");
        names.add("Raju");// Duplicate ignored

        for(String name : names) {
            System.out.println(name);
        }
    }
}
