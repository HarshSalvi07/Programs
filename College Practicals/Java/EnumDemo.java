package myapp;

import java.util.Scanner;

enum Day{MON,TUE,WED}

public class EnumDemo{
    public static void main(String[] args){
        Day today = Day.MON;
        System.out.println("today is "+today);
    }
}