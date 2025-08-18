class MethodOverloading {
    int a = 10;
    int b = 20;

    int sum() {
        int c = a + b;
        System.out.println("Sum of C="+c);
        return 0;
    }

    int sum(int x) {
        int y= 0;
        y = x*x;
        System.out.println("Square of y="+y);
        return 0;
    }

    String sum(char x, int y) {
        System.out.println("x="+x);
        System.out.println("y="+y);
        return "";
    }
}




