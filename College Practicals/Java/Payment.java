public class Payment{}
class UPI extends Payment{}
class Card extends Payment{}
class demo {
    public static void main(String[] args) {}
        void processPayment (Payment p){
            if (p instanceof UPI) {
                System.out.println("Processing UPI Payment....");
            } else if (p instanceof Card) {
                System.out.println("Processing Card Payment....");
            }
        }
    }



