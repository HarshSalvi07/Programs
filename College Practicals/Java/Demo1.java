import java.util.*;

public class Demo1 {
    public static void main(String[] args) {
        Properties p = new Properties();
        p.setProperty("username", "admin");
        p.setProperty("password", "12345");

        System.out.println("Username: "+ p.getProperty("username"));
        System.out.println("Password: "+ p.getProperty("password"));
    }
}

