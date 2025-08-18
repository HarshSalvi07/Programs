public class LogicalDemo{
    public static void main(String[] args){
        int age = 18;
        boolean hasLicense = true;

        if(age >= 18 && hasLicense){
            System.out.println("can drive");
        }else{
            System.out.println("can't drive");
        }
        System.out.println(!hasLicense);
    }
}
