public class LoopDemo {
    public static void main(String[] args){
        for(int i=1;i<=5;i++){
            if( i ==3)continue;
            System.out.print(i+"");
        }


        int j = 1;
        while(j<=5){
            System.out.print("\n"+j);
            j++;
        }

        int k = 1;
        do{
            System.out.print("\nDo:"+k);
            k++;
        }while(k<=5);
    }
}
