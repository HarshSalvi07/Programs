public class ShoppingCart {
    public static void main (String[] args) {
        int applePrice = 40;
        int bananaPrice = 20;
        int quantity = 3;

        int total = (applePrice + bananaPrice) * quantity;
        System.out.println("Total Bill: ₹" + total);
    }
}
