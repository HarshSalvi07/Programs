import javax.swing.*;
import java.awt.event.ItemEvent;

public class ItemListner {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Item Listners");
        JCheckBox checkBox = new JCheckBox("Accept Terms");

        checkBox.addItemListener(e->{
            if (e.getStateChange()== ItemEvent.SELECTED){
                System.out.println("Checkbox Checked");

            }
            else{
                System.out.println("Checkbox Unchecked");
            }
        });

        frame.add(checkBox);
        frame.setSize(300,300);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}
