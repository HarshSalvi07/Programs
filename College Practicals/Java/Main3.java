class MyThread extends Thread{
    public void run(){
        System.out.println("Thread runnng: "+Thread.currentThread().getName());
    }
}

public class Main3{
    public static void main(String[] args){
        MyThread t1 = new MyThread(); //Thread 1
        MyThread t2 = new MyThread(); //Thread 2
        t1.start(); //Don't call run now
        t2.start();
    }
}